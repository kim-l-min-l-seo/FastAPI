from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

@app.get("/test")
def hello():
    return {"message": "FastAPI Test Page"}

@app.get("/theme/base", response_class=HTMLResponse)
def index(request: Request):
    return templates.TemplateResponse(name="theme/base.html", context={"request": request, "title": "test"})

@app.get("/theme/index", response_class=HTMLResponse)
def index(request: Request):
    return templates.TemplateResponse(name="theme/index.html", context={"request": request, "title": "Dashboard", "subtitle" : "Control panel"})

@app.get("/theme/index2", response_class=HTMLResponse)
def index2(request: Request):
    return templates.TemplateResponse(name="theme/index2.html", context={"request": request, "title": "Dashboard2", "subtitle" : "Control panel"})


# Layout Option
@app.get("/theme/pages/layout/top-nav", response_class=HTMLResponse)
def topnav(request: Request):
    return templates.TemplateResponse(name="theme/pages/layout/top-nav.html", context={"request": request, "title": "Top Navigation","subtitle" : "Example 2.0"})

@app.get("/theme/pages/layout/boxed", response_class=HTMLResponse)
def boxed(request: Request):
    return templates.TemplateResponse(name="theme/pages/layout/boxed.html", context={"request": request, "title": "Boxed Layout","subtitle" : "Blank example to the boxed layout"})

@app.get("/theme/pages/layout/fixed", response_class=HTMLResponse)
def fixed(request: Request):
    return templates.TemplateResponse(name="theme/pages/layout/fixed.html", context={"request": request, "title": "Fixed Layout","subtitle" : "Blank example to the fixed layout"})

@app.get("/theme/pages/layout/collapsed-sidebar", response_class=HTMLResponse)
def collapsedsidebar(request: Request):
    return templates.TemplateResponse(name="theme/pages/layout/collapsed-sidebar.html", context={"request": request, "title": "Sidebar Collapsed","subtitle" : "Layout with collapsed sidebar on load"})


# Widgets
@app.get("/theme/pages/widgets", response_class=HTMLResponse)
def widgets(request: Request):
    return templates.TemplateResponse(name="theme/pages/widgets.html", context={"request": request, "title": "Widgets","subtitle" : "Preview page"})


# Charts
@app.get("/theme/pages/charts/chartjs", response_class=HTMLResponse)
def widgets(request: Request):
    return templates.TemplateResponse(name="theme/pages/charts/chartjs.html", context={"request": request, "title": "ChartJS","subtitle" : "Preview sample"})
@app.get("/theme/pages/charts/morris", response_class=HTMLResponse)
def morris(request: Request):
    return templates.TemplateResponse(name="theme/pages/charts/morris.html", context={"request": request, "title": "Morris Charts","subtitle" : "Preview sample"})
@app.get("/theme/pages/charts/flot", response_class=HTMLResponse)
def flot(request: Request):
    return templates.TemplateResponse(name="theme/pages/charts/flot.html", context={"request": request, "title": "Flot Charts","subtitle" : "Preview sample"})
@app.get("/theme/pages/charts/inline", response_class=HTMLResponse)
def inline(request: Request):
    return templates.TemplateResponse(name="theme/pages/charts/inline.html", context={"request": request, "title": "Inline Charts","subtitle" : "multiple types of charts"})


# UI Elements
@app.get("/theme/pages/UI/general", response_class=HTMLResponse)
def general(request: Request):
    return templates.TemplateResponse(name="theme/pages/UI/general.html", context={"request": request, "title": "General UI","subtitle" : "Preview of UI elements"})

@app.get("/theme/pages/UI/icons", response_class=HTMLResponse)
def icons(request: Request):
    return templates.TemplateResponse(name="theme/pages/UI/icons.html", context={"request": request, "title": "Icons","subtitle" : "a set of beautiful icons"})

@app.get("/theme/pages/UI/buttons", response_class=HTMLResponse)
def buttons(request: Request):
    return templates.TemplateResponse(name="theme/pages/UI/buttons.html", context={"request": request, "title": "Buttons","subtitle" : "Control panel"})

@app.get("/theme/pages/UI/sliders", response_class=HTMLResponse)
def sliders(request: Request):
    return templates.TemplateResponse(name="theme/pages/UI/sliders.html", context={"request": request, "title": "Sliders","subtitle" : "range sliders"})

@app.get("/theme/pages/UI/timeline", response_class=HTMLResponse)
def timeline(request: Request):
    return templates.TemplateResponse(name="theme/pages/UI/timeline.html", context={"request": request, "title": "Timeline","subtitle" : "example"})

@app.get("/theme/pages/UI/modals", response_class=HTMLResponse)
def modals(request: Request):
    return templates.TemplateResponse(name="theme/pages/UI/modals.html", context={"request": request, "title": "Modals","subtitle" : "new"})

# Forms
@app.get("/theme/pages/forms/general", response_class=HTMLResponse)
def general2(request: Request):
    return templates.TemplateResponse(name="theme/pages/forms/general.html", context={"request": request, "title": "General Form Elements","subtitle" : "Preview"})

@app.get("/theme/pages/forms/advanced", response_class=HTMLResponse)
def advanced(request: Request):
    return templates.TemplateResponse(name="theme/pages/forms/advanced.html", context={"request": request, "title": "Advanced Form Elements","subtitle" : "Preview"})

@app.get("/theme/pages/forms/editors", response_class=HTMLResponse)
def editors(request: Request):
    return templates.TemplateResponse(name="theme/pages/forms/editors.html", context={"request": request, "title": "Text Editors","subtitle" : "Advanced form element"})


# Tables
@app.get("/theme/pages/tables/simple", response_class=HTMLResponse)
def simple(request: Request):
    return templates.TemplateResponse(name="theme/pages/tables/simple.html", context={"request": request, "title": "Simple Tables","subtitle" : "preview of simple tables"})

@app.get("/theme/pages/tables/data", response_class=HTMLResponse)
def editors(request: Request):
    return templates.TemplateResponse(name="theme/pages/tables/data.html", context={"request": request, "title": "Data Tables","subtitle" : "advanced tables"})


# Calandar
@app.get("/theme/pages/calendar", response_class=HTMLResponse)
def calendar(request: Request):
    return templates.TemplateResponse(name="theme/pages/calendar.html", context={"request": request, "title": "Calendar","subtitle" : "Control panel"})

# Mailbox
@app.get("/theme/pages/mailbox/mailbox", response_class=HTMLResponse)
def mailbox(request: Request):
    return templates.TemplateResponse(name="theme/pages/mailbox/mailbox.html", context={"request": request, "title": "Mailbox","subtitle" : "13 new messages"})
@app.get("/theme/pages/mailbox/read-mail", response_class=HTMLResponse)
def read_mail(request: Request):
    return templates.TemplateResponse(name="theme/pages/mailbox/read-mail.html", context={"request": request, "title": "Read Mail","subtitle" : ""})
@app.get("/theme/pages/mailbox/compose", response_class=HTMLResponse)
def compose(request: Request):
    return templates.TemplateResponse(name="theme/pages/mailbox/compose.html", context={"request": request, "title": "Compose Mail","subtitle" : "13 new messages"})

# Examples
@app.get("/theme/pages/examples/invoice", response_class=HTMLResponse)
def invoice(request: Request):
    return templates.TemplateResponse(name="theme/pages/examples/invoice.html", context={"request": request, "title": "Invoice","subtitle" : "#007612"})

@app.get("/theme/pages/examples/invoice-print", response_class=HTMLResponse)
def invoice_print(request: Request):
    return templates.TemplateResponse(name="theme/pages/examples/invoice-print.html", context={"request": request, "title": "","subtitle" : ""})

@app.get("/theme/pages/examples/profile", response_class=HTMLResponse)
def profile(request: Request):
    return templates.TemplateResponse(name="theme/pages/examples/profile.html", context={"request": request, "title": "User Profile","subtitle" : ""})

@app.get("/theme/pages/examples/login", response_class=HTMLResponse)
def login(request: Request):
    return templates.TemplateResponse(name="theme/pages/examples/login.html", context={"request": request, "title": "login","subtitle" : ""})

@app.get("/theme/pages/examples/register", response_class=HTMLResponse)
def register(request: Request):
    return templates.TemplateResponse(name="theme/pages/examples/register.html", context={"request": request, "title": "register","subtitle" : ""})

@app.get("/theme/pages/examples/lockscreen", response_class=HTMLResponse)
def lockscreen(request: Request):
    return templates.TemplateResponse(name="theme/pages/examples/lockscreen.html", context={"request": request, "title": "lockscreen","subtitle" : ""})

@app.get("/theme/pages/examples/404", response_class=HTMLResponse)
def error404(request: Request):
    return templates.TemplateResponse(name="theme/pages/examples/404.html", context={"request": request, "title": "404 Error Page","subtitle" : ""})

@app.get("/theme/pages/examples/500", response_class=HTMLResponse)
def error500(request: Request):
    return templates.TemplateResponse(name="theme/pages/examples/500.html", context={"request": request, "title": "500 Error Page","subtitle" : ""})

@app.get("/theme/pages/examples/blank", response_class=HTMLResponse)
def blank(request: Request):
    return templates.TemplateResponse(name="theme/pages/examples/blank.html", context={"request": request, "title": "Blank page","subtitle" : "it all starts here"})

@app.get("/theme/pages/examples/pace", response_class=HTMLResponse)
def pace(request: Request):
    return templates.TemplateResponse(name="theme/pages/examples/pace.html", context={"request": request, "title": "Pace page","subtitle" : "Loading example"})


# Multilevel


# Documentation
@app.get("/theme/documentation/index", response_class=HTMLResponse)
def documantation(request: Request):
    return templates.TemplateResponse(name="theme/documentation/index.html", context={"request": request, "title": "AdminLTE Documentation","subtitle" : "Version 2.3"})