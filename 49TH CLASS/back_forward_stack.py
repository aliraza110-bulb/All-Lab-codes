import time
import random
from typing import List, Dict, Any

import dash
from dash import html, dcc, Input, Output, State
import dash_bootstrap_components as dbc

# Improved Back / Forward Stack Visualizer (styles live in assets/styles.css)
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.DARKLY])
server = app.server

app.layout = html.Div(
    [
        # top header
        html.Header(
            [
                html.Div(className="brand", children=[
                    html.H1("Stack Navigator", className="app-title"),
                    html.P("Back / Forward visualizer — professional, responsive UI", className="app-sub"),
                ])
            ],
            className="app-header",
        ),

        # controls + stores
        html.Main(
            [
                html.Section(
                    [
                        dcc.Input(id="input-value", className="input", placeholder="Enter page name or URL (e.g. Page 1)", type="text"),
                        html.Div(className="controls-row", children=[
                            html.Button("Visit", id="visit-btn", className="btn primary"),
                            html.Button("Back", id="back-btn", className="btn ghost"),
                            html.Button("Forward", id="forward-btn", className="btn ghost"),
                            html.Button("Peek", id="peek-btn", className="btn ghost"),
                            html.Button("Clear", id="clear-btn", className="btn neutral"),
                            html.Button("Randomize", id="rand-btn", className="btn accent"),
                        ]),
                    ],
                    className="controls",
                ),
                dcc.Store(id="back-store", data=[]),
                dcc.Store(id="forward-store", data=[]),
                dcc.Store(id="current-store", data=""),
                dcc.Store(id="ops-store", data=[]),

                # visual layout
                html.Section(
                    className="layout",
                    children=[
                        html.Div(className="panel",
                                 children=[
                                     html.Div("Back Stack", className="panel-title"),
                                     html.Div(id="back-box", className="stack-box"),
                                 ]),
                        html.Div(className="panel center",
                                 children=[
                                     html.Div("Current Page", className="panel-title"),
                                     html.Div(id="current-card", className="current-card", children="—"),
                                     html.Div(id="top-indicator", className="status-line"),
                                 ]),
                        html.Aside(className="side",
                                   children=[
                                       html.Div("Forward Stack", className="panel-title"),
                                       html.Div(id="forward-box", className="stack-box"),
                                       html.Div("Operations Log", className="panel-title", style={"marginTop": 12}),
                                       html.Div(id="ops-log", className="log", children="No operations yet."),
                                   ])
                    ]
                ),
                html.Div(className="footer", children="Responsive · Press Enter to Visit · Professional UI"),
            ],
            className="container",
        ),
    ]
)


def _log_entry(ops: List[Dict[str, Any]], op: str, val: str):
    ops = list(ops or [])
    ops.insert(0, {"op": op, "val": val, "ts": time.time()})
    return ops[:200]


@app.callback(
    Output("back-store", "data"),
    Output("forward-store", "data"),
    Output("current-store", "data"),
    Output("ops-store", "data"),
    Input("input-value", "n_submit"),
    Input("visit-btn", "n_clicks"),
    Input("back-btn", "n_clicks"),
    Input("forward-btn", "n_clicks"),
    Input("peek-btn", "n_clicks"),
    Input("clear-btn", "n_clicks"),
    Input("rand-btn", "n_clicks"),
    State("input-value", "value"),
    State("back-store", "data"),
    State("forward-store", "data"),
    State("current-store", "data"),
    State("ops-store", "data"),
    prevent_initial_call=True,
)
def modify_stacks(submit_n, visit_n, back_n, forward_n, peek_n, clear_n, rand_n, value, back_data, forward_data, current, ops):
    ctx = dash.callback_context
    if not ctx.triggered:
        raise dash.exceptions.PreventUpdate
    btn = ctx.triggered[0]["prop_id"].split(".")[0]
    back = list(back_data or [])
    forward = list(forward_data or [])
    ops = list(ops or [])
    current = current if current is not None else ""

    # treat Enter (input-value.n_submit) same as Visit
    if btn == "input-value":
        btn = "visit-btn"

    if btn == "visit-btn":
        v = (value or "").strip()
        if v == "":
            return back, forward, current, ops
        if current:
            back.append(current)
        current = v
        forward = []
        ops = _log_entry(ops, "visit", v)
        return back, forward, current, ops

    if btn == "back-btn":
        if not back:
            ops = _log_entry(ops, "back", "none")
            return back, forward, current, ops
        prev = back.pop()
        if current:
            forward.append(current)
        current = prev
        ops = _log_entry(ops, "back", prev)
        return back, forward, current, ops

    if btn == "forward-btn":
        if not forward:
            ops = _log_entry(ops, "forward", "none")
            return back, forward, current, ops
        nxt = forward.pop()
        if current:
            back.append(current)
        current = nxt
        ops = _log_entry(ops, "forward", nxt)
        return back, forward, current, ops

    if btn == "peek-btn":
        ops = _log_entry(ops, "peek", current or "none")
        return back, forward, current, ops

    if btn == "clear-btn":
        ops = _log_entry(ops, "clear", "")
        return [], [], "", ops

    if btn == "rand-btn":
        count = random.randint(3, 7)
        pages = [f"Page {i}" for i in range(1, count + 1)]
        back = pages[:-1]
        current = pages[-1]
        forward = []
        ops = _log_entry(ops, "randomize", ",".join(pages))
        return back, forward, current, ops

    return back, forward, current, ops


@app.callback(
    Output("back-box", "children"),
    Output("forward-box", "children"),
    Output("current-card", "children"),
    Output("top-indicator", "children"),
    Output("ops-log", "children"),
    Input("back-store", "data"),
    Input("forward-store", "data"),
    Input("current-store", "data"),
    Input("ops-store", "data"),
)
def render_visuals(back_data, forward_data, current, ops):
    back = list(back_data or [])
    forward = list(forward_data or [])
    # build DOM for back stack: bottom is first element, top is last
    back_children = []
    for idx, v in enumerate(back):
        cls = "item"
        if idx == len(back) - 1:
            cls += " top"
        back_children.append(html.Div(className=cls, children=[html.Span(str(v)), html.Span("◀")]))
    if not back_children:
        back_children = [html.Div(className="item empty", children="(empty)")]
    # forward stack (top is last)
    forward_children = []
    for idx, v in enumerate(forward):
        cls = "item"
        if idx == len(forward) - 1:
            cls += " top"
        forward_children.append(html.Div(className=cls, children=[html.Span(str(v)), html.Span("▶")]))
    if not forward_children:
        forward_children = [html.Div(className="item empty", children="(empty)")]

    current_display = current if current else "—"
    top_ind = f"Back: {len(back)} · Forward: {len(forward)}"

    # build ops log display (recent 12)
    ops_divs = []
    for entry in (ops or [])[:12]:
        ts = time.strftime("%H:%M:%S", time.localtime(entry.get("ts", time.time())))
        ops_divs.append(html.Div(f"[{ts}] {entry.get('op')} {entry.get('val')}", className="op-line"))
    if not ops_divs:
        ops_divs = [html.Div("No operations yet.", className="op-muted")]

    return back_children, forward_children, current_display, top_ind, ops_divs


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8050)