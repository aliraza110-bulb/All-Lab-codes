import dash
from dash import dcc, html, dash_table
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
import pandas as pd
from datetime import datetime
from reportlab.pdfgen import canvas
import os
import plotly.express as px

# ---------------------------
# Data Setup
# ---------------------------
DATA_DIR = "data"
os.makedirs(DATA_DIR, exist_ok=True)
PRODUCTS_FILE = os.path.join(DATA_DIR, "products.csv")
SALES_FILE = os.path.join(DATA_DIR, "sales.csv")
INVOICE_DIR = os.path.join(DATA_DIR, "invoices")
os.makedirs(INVOICE_DIR, exist_ok=True)

# Create CSVs if not exist
for file, cols in [(PRODUCTS_FILE, ["ID","Name","Price","Stock"]),
                   (SALES_FILE, ["ID","ProductID","ProductName","Quantity","Total","Date"])]:
    if not os.path.exists(file):
        pd.DataFrame(columns=cols).to_csv(file,index=False)

# ---------------------------
# Load/Save functions
# ---------------------------
def load_products(): return pd.read_csv(PRODUCTS_FILE)
def save_products(df): df.to_csv(PRODUCTS_FILE,index=False)
def load_sales(): return pd.read_csv(SALES_FILE)
def save_sales(df): df.to_csv(SALES_FILE,index=False)

# ---------------------------
# Generate PDF invoice
# ---------------------------
def generate_invoice(sale):
    invoice_file = os.path.join(INVOICE_DIR,f"invoice_{sale['ID']}.pdf")
    c = canvas.Canvas(invoice_file)
    c.setFont("Helvetica-Bold",16)
    c.drawString(200,800,"E-Commerce Invoice")
    c.setFont("Helvetica",12)
    c.drawString(50,750,f"Invoice ID: {sale['ID']}")
    c.drawString(50,730,f"Product: {sale['ProductName']}")
    c.drawString(50,710,f"Quantity: {sale['Quantity']}")
    c.drawString(50,690,f"Total: ${sale['Total']}")
    c.drawString(50,670,f"Date: {sale['Date']}")
    c.save()
    return invoice_file

# ---------------------------
# Dash App Initialization
# ---------------------------
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.FLATLY])
app.title = "Professional E-Commerce Dashboard"

# ---------------------------
# Sidebar Layout
# ---------------------------
sidebar = dbc.Nav(
    [
        html.H2("Inventory App", className="text-center text-warning"),
        html.Hr(),
        dbc.NavLink("Dashboard", href="/", id="dashboard-link", active="exact"),
        dbc.NavLink("Products", href="/products", id="products-link", active="exact"),
        dbc.NavLink("Sales", href="/sales", id="sales-link", active="exact")
    ],
    vertical=True,
    pills=True,
    style={"height":"100vh","backgroundColor":"#fdf6e3","padding":20}
)

# ---------------------------
# Content Placeholder
# ---------------------------
content = html.Div(id="page-content", style={"marginLeft":"20%","padding":20})

# ---------------------------
# App Layout
# ---------------------------
app.layout = html.Div([
    dcc.Location(id="url"),
    sidebar,
    content
])

# ---------------------------
# Dashboard Layout
# ---------------------------
def dashboard_layout():
    df_products = load_products()
    df_sales = load_sales()
    total_sales = df_sales["Total"].sum() if not df_sales.empty else 0
    total_products = len(df_products)
    low_stock = len(df_products[df_products["Stock"] < 5])
    top_products = df_sales.groupby("ProductName")["Quantity"].sum().sort_values(ascending=False).head(5)

    # Top selling bar chart
    fig = px.bar(top_products, x=top_products.index, y=top_products.values, 
                 labels={"x":"Product","y":"Quantity Sold"},
                 title="Top 5 Products Sold", color_discrete_sequence=["#FFB300"])
    fig.update_layout(plot_bgcolor="#fffbe6", paper_bgcolor="#fffbe6")

    return dbc.Container([
        dbc.Row([
            dbc.Col(dbc.Card(dbc.CardBody([html.H5("Total Sales",className="card-title text-warning"),
                                           html.H3(f"${total_sales}",className="card-text")]),
                             style={"textAlign":"center","borderRadius":10,"boxShadow":"2px 2px 10px #ccc"}), width=3),
            dbc.Col(dbc.Card(dbc.CardBody([html.H5("Total Products",className="card-title text-warning"),
                                           html.H3(f"{total_products}",className="card-text")]),
                             style={"textAlign":"center","borderRadius":10,"boxShadow":"2px 2px 10px #ccc"}), width=3),
            dbc.Col(dbc.Card(dbc.CardBody([html.H5("Low Stock Items",className="card-title text-warning"),
                                           html.H3(f"{low_stock}",className="card-text")]),
                             style={"textAlign":"center","borderRadius":10,"boxShadow":"2px 2px 10px #ccc"}), width=3),
        ], style={"marginBottom":20}),
        dbc.Row([
            dbc.Col(dcc.Graph(figure=fig), width=12)
        ])
    ], fluid=True, style={"backgroundColor":"#fffbe6","padding":20})

# ---------------------------
# Products Layout
# ---------------------------
def products_layout():
    df = load_products()
    return dbc.Container([
        html.H3("Products", className="text-warning"),
        dbc.Row([
            dbc.Col([
                dbc.Input(id="product-name",placeholder="Name", type="text", style={"marginBottom":10}),
                dbc.Input(id="product-price",placeholder="Price", type="number", style={"marginBottom":10}),
                dbc.Input(id="product-stock",placeholder="Stock", type="number", style={"marginBottom":10}),
                dbc.Input(id="sell-quantity",placeholder="Sell Quantity", type="number", style={"marginBottom":10}),
                dbc.Button("Add",id="add-product-btn",color="warning",className="me-2"),
                dbc.Button("Update",id="update-product-btn",color="info",className="me-2"),
                dbc.Button("Delete",id="delete-product-btn",color="danger",className="me-2"),
                dbc.Button("Sell",id="sell-product-btn",color="success",className="mt-2"),
                html.Div(id="product-msg", style={"marginTop":10,"fontWeight":"bold"})
            ], width=3),
            dbc.Col([
                dash_table.DataTable(
                    id="product-table",
                    columns=[{"name":i,"id":i} for i in df.columns],
                    data=df.to_dict("records"),
                    row_selectable="single",
                    filter_action="native",
                    style_table={"overflowX":"auto"},
                    style_cell={"textAlign":"left","padding":5,"backgroundColor":"#fffbe6"},
                    style_header={"backgroundColor":"#FFB300","color":"white","fontWeight":"bold"}
                )
            ], width=9)
        ])
    ], fluid=True)

# ---------------------------
# Sales Layout
# ---------------------------
def sales_layout():
    df = load_sales()
    return dbc.Container([
        html.H3("Sales", className="text-warning"),
        dash_table.DataTable(
            id="sales-table",
            columns=[{"name":i,"id":i} for i in df.columns],
            data=df.to_dict("records"),
            filter_action="native",
            style_table={"overflowX":"auto"},
            style_cell={"textAlign":"left","padding":5,"backgroundColor":"#fffbe6"},
            style_header={"backgroundColor":"#FFB300","color":"white","fontWeight":"bold"}
        )
    ], fluid=True)

# ---------------------------
# URL Routing
# ---------------------------
@app.callback(
    Output("page-content","children"),
    [Input("url","pathname")]
)
def display_page(pathname):
    if pathname == "/products": return products_layout()
    elif pathname == "/sales": return sales_layout()
    else: return dashboard_layout()

# ---------------------------
# Product Actions Callbacks
# ---------------------------
@app.callback(
    Output("product-table","data"),
    Output("product-msg","children"),
    Output("sales-table","data"),
    Input("sell-product-btn","n_clicks"),
    State("product-table","data"),
    State("product-table","selected_rows"),
    State("sell-quantity","value"),
    State("sales-table","data")
)
def sell_product(n,rows,selected,qty,sales_rows):
    if n is None or not selected or qty is None: return rows,"",sales_rows
    df = pd.DataFrame(rows)
    s_df = pd.DataFrame(sales_rows) if sales_rows else pd.DataFrame(columns=["ID","ProductID","ProductName","Quantity","Total","Date"])
    idx = selected[0]
    product = df.iloc[idx]
    if qty > int(product["Stock"]): return rows,"Not enough stock!",sales_rows
    total = qty * float(product["Price"])
    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    df.at[idx,"Stock"] -= qty
    save_products(df)
    new_id = 1 if s_df.empty else s_df["ID"].max()+1
    sale = {"ID":new_id,"ProductID":product["ID"],"ProductName":product["Name"],"Quantity":qty,"Total":total,"Date":date}
    s_df = pd.concat([s_df,pd.DataFrame([sale])],ignore_index=True)
    save_sales(s_df)
    generate_invoice(sale)
    return df.to_dict("records"),f"Sold {qty} x {product['Name']} = ${total} (Invoice generated)",s_df.to_dict("records")

# ---------------------------
# Run App
# ---------------------------
if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0",port=8050)
