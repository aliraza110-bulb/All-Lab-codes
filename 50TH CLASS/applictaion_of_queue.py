"""
Professional Ticket Queue System using Dash + dash-bootstrap-components.

Features:
- Queue class (enqueue, dequeue, peek, clear)
- Add ticket (name or number), Serve (dequeue)
- Shows current queue dynamically and last served ticket
- Operations log and responsive, clean UI
- Run: python3 applictaion_of_queue.py  then open http://127.0.0.1:8050
"""

from collections import deque
import time
import random
from typing import List, Dict, Any

import dash
from dash import html, dcc, Input, Output, State
import dash_bootstrap_components as dbc

# ---------- Queue Data Structure ----------
class TicketQueue:
    """Simple FIFO queue wrapper using deque with helpful utilities."""
    def __init__(self):
        self._q = deque()

    def enqueue(self, ticket: str) -> None:
        self._q.append(ticket)

    def dequeue(self) -> str:
        return self._q.popleft() if self._q else ""

    def peek(self) -> str:
        return self._q[0] if self._q else ""

    def clear(self) -> None:
        self._q.clear()

    def to_list(self) -> List[str]:
        return list(self._q)

    def size(self) -> int:
        return len(self._q)


# ---------- App init ----------
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.FLATLY])

# ---------- Layout ----------
app.layout = dbc.Container(
    [
        dbc.Row(
            dbc.Col(
                html.H2("Ticket Queue System", className="mt-3 mb-1"),
                width=12
            )
        ),
        dbc.Row(
            [
                dbc.Col(
                    dbc.Card(
                        dbc.CardBody(
                            [
                                dbc.Label("Add ticket (name / number)"),
                                dbc.Input(id="ticket-input", placeholder="e.g. Customer 101 or 42", type="text"),
                                html.Div(className="mt-2 d-flex", children=[
                                    dbc.Button("Add Ticket", id="add-btn", color="primary", className="me-2"),
                                    dbc.Button("Serve Ticket", id="serve-btn", color="danger", className="me-2"),
                                    dbc.Button("Peek", id="peek-btn", color="secondary", className="me-2"),
                                    dbc.Button("Clear Queue", id="clear-btn", color="light"),
                                ]),
                                html.Div(className="mt-3", children=[
                                    dbc.Button("Randomize Example", id="rand-btn", color="info", size="sm")
                                ]),
                            ]
                        ),
                        className="shadow-sm",
                    ),
                    md=6,
                ),
                dbc.Col(
                    dbc.Card(
                        dbc.CardBody(
                            [
                                html.H6("Last Served", className="mb-2"),
                                html.Div(id="last-served", className="display-6 text-muted"),
                                html.Hr(),
                                html.H6("Queue Status", className="mb-2"),
                                html.Div(id="queue-size", className="text-muted mb-2"),
                                dbc.ListGroup(id="queue-list", flush=True),
                            ]
                        )
                    ),
                    md=6,
                ),
            ],
            className="g-4",
        ),
        dbc.Row(
            dbc.Col(
                dbc.Card(
                    dbc.CardBody(
                        [
                            html.H6("Operations Log", className="mb-2"),
                            html.Div(id="ops-log", style={"maxHeight": "220px", "overflow": "auto", "fontSize": "14px"}),
                        ]
                    )
                ),
                width=12
            ),
            className="mt-3"
        ),
        # client-side stores for queue data + last served + ops
        dcc.Store(id="queue-store", data=[]),
        dcc.Store(id="last-store", data=""),
        dcc.Store(id="ops-store", data=[]),
        # small footer
        html.Footer("Server: 127.0.0.1:8050 · Debug mode", className="mt-3 text-muted")
    ],
    fluid=True,
    style={"maxWidth": "980px", "paddingTop": "12px"}
)

# ---------- Helper for ops log ----------
def _log_entry(ops: List[Dict[str, Any]], op: str, val: str) -> List[Dict[str, Any]]:
    ops = list(ops or [])
    ops.insert(0, {"op": op, "val": val, "ts": time.time()})
    return ops[:200]


# ---------- Callbacks ----------
@app.callback(
    Output("queue-store", "data"),
    Output("last-store", "data"),
    Output("ops-store", "data"),
    Input("add-btn", "n_clicks"),
    Input("serve-btn", "n_clicks"),
    Input("peek-btn", "n_clicks"),
    Input("clear-btn", "n_clicks"),
    Input("rand-btn", "n_clicks"),
    State("ticket-input", "value"),
    State("queue-store", "data"),
    State("last-store", "data"),
    State("ops-store", "data"),
    prevent_initial_call=True,
)
def modify_queue(add_n, serve_n, peek_n, clear_n, rand_n, value, queue_data, last_data, ops_data):
    """
    Central callback to mutate the queue. Uses stores to keep client-side state.
    Buttons:
     - add-btn: enqueue (value required)
     - serve-btn: dequeue -> update last served
     - peek-btn: log the current front without removing
     - clear-btn: clear the queue
     - rand-btn: populate with sample tickets
    """
    ctx = dash.callback_context
    if not ctx.triggered:
        raise dash.exceptions.PreventUpdate

    triggered = ctx.triggered[0]["prop_id"].split(".")[0]
    qlist = list(queue_data or [])
    last = last_data or ""
    ops = list(ops_data or [])
    tq = TicketQueue()
    for item in qlist:
        tq.enqueue(item)

    if triggered == "add-btn":
        v = (value or "").strip()
        if v == "":
            # ignore empty adds
            ops = _log_entry(ops, "add_failed", "empty")
            return tq.to_list(), last, ops
        # enqueue and record
        tq.enqueue(v)
        ops = _log_entry(ops, "enqueue", v)
        return tq.to_list(), last, ops

    if triggered == "serve-btn":
        if tq.size() == 0:
            ops = _log_entry(ops, "serve_failed", "empty")
            return tq.to_list(), last, ops
        served = tq.dequeue()
        last = served
        ops = _log_entry(ops, "dequeue", served)
        return tq.to_list(), last, ops

    if triggered == "peek-btn":
        p = tq.peek()
        ops = _log_entry(ops, "peek", p or "none")
        return tq.to_list(), last, ops

    if triggered == "clear-btn":
        tq.clear()
        ops = _log_entry(ops, "clear", "")
        last = ""
        return tq.to_list(), last, ops

    if triggered == "rand-btn":
        # generate example tickets
        sample = [f"Ticket-{random.randint(100,999)}" for _ in range(random.randint(3, 8))]
        tq.clear()
        for s in sample:
            tq.enqueue(s)
        ops = _log_entry(ops, "randomize", ",".join(sample))
        return tq.to_list(), last, ops

    return tq.to_list(), last, ops


@app.callback(
    Output("queue-list", "children"),
    Output("queue-size", "children"),
    Output("last-served", "children"),
    Output("ops-log", "children"),
    Input("queue-store", "data"),
    Input("last-store", "data"),
    Input("ops-store", "data"),
)
def render_ui(queue_data, last, ops):
    """
    Render queue list, size, last served and operations log.
    """
    qlist = list(queue_data or [])
    # build list: base at top, front (next to serve) at top of list display? show front at top for clarity
    if not qlist:
        items = [dbc.ListGroupItem("(empty queue)", color="light")]
    else:
        items = []
        # show front (to be served) at top
        for idx, val in enumerate(qlist):
            # visually highlight the front (first element in list)
            if idx == 0:
                items.append(dbc.ListGroupItem(html.Span([html.Strong(str(val)), " — next"]), color="primary"))
            else:
                items.append(dbc.ListGroupItem(str(val)))

    size_text = f"Queue size: {len(qlist)}"
    last_text = last or "(none served yet)"

    # ops log lines (limit 50)
    ops_lines = []
    for entry in (ops or [])[:50]:
        ts = time.strftime("%H:%M:%S", time.localtime(entry.get("ts", time.time())))
        ops_lines.append(html.Div(f"[{ts}] {entry.get('op')}: {entry.get('val')}", style={"marginBottom":"4px"}))

    if not ops_lines:
        ops_lines = [html.Div("No operations yet", className="text-muted")]

    return items, size_text, last_text, ops_lines


if __name__ == "__main__":
    # run server on localhost:8050 in debug mode
    app.run(host="127.0.0.1", port=8050, debug=True)