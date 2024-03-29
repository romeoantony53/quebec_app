from . import __version__ as app_version

app_name = "quebec_app"
app_title = "Quebec App"
app_publisher = "Romeo"
app_description = "App custom"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "romeorealist@gmail.com"
app_license = "MIT"



# Includes in <head>
# ------------------
web_include_js = ["/assets/quebec_app/js/main.js","/assets/quebec_app/vendor/bootstrap/js/bootstrap.bundle.min.js","/assets/quebec_app/vendor/glightbox/js/glightbox.min.js","/assets/quebec_app/vendor/isotope-layout/isotope.pkgd.min.js","/assets/quebec_app/vendor/swiper/swiper-bundle.min.js","/assets/quebec_app/vendor/waypoints/noframework.waypoints.js","/assets/quebec_app/vendor/php-email-form/validate.js"]
web_include_css = ["/assets/quebec_app/css/style.css","/assets/quebec_app/vendor/animate.css/animate.min.css","/assets/quebec_app/vendor/bootstrap/css/bootstrap.min.css","/assets/quebec_app/vendor/bootstrap-icons/bootstrap-icons.css","/assets/quebec_app/vendor/boxicons/css/boxicons.min.css","/assets/quebec_app/vendor/glightbox/css/glightbox.min.css","/assets/quebec_app/vendor/remixicon/remixicon.css","/assets/quebec_app/vendor/swiper/swiper-bundle.min.css"]

# include js, css files in header of desk.html
# app_include_css = "/assets/quebec_app/css/quebec_app.css"
# app_include_js = "/assets/quebec_app/js/quebec_app.js"

# include js, css files in header of web template
# web_include_css = "/assets/quebec_app/css/quebec_app.css"
# web_include_js = "/assets/quebec_app/js/quebec_app.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "quebec_app/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "quebec_app.install.before_install"
# after_install = "quebec_app.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "quebec_app.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"quebec_app.tasks.all"
# 	],
# 	"daily": [
# 		"quebec_app.tasks.daily"
# 	],
# 	"hourly": [
# 		"quebec_app.tasks.hourly"
# 	],
# 	"weekly": [
# 		"quebec_app.tasks.weekly"
# 	]
# 	"monthly": [
# 		"quebec_app.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "quebec_app.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "quebec_app.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "quebec_app.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]


# User Data Protection
# --------------------

user_data_fields = [
	{
		"doctype": "{doctype_1}",
		"filter_by": "{filter_by}",
		"redact_fields": ["{field_1}", "{field_2}"],
		"partial": 1,
	},
	{
		"doctype": "{doctype_2}",
		"filter_by": "{filter_by}",
		"partial": 1,
	},
	{
		"doctype": "{doctype_3}",
		"strict": False,
	},
	{
		"doctype": "{doctype_4}"
	}
]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"quebec_app.auth.validate"
# ]

