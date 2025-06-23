from admin.routers import admin_routers

from interactives.routers import interactives_routers

routers = [
    *admin_routers,
    *interactives_routers
]
