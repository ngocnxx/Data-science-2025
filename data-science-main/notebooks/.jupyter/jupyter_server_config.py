c = get_config()
c.ServerApp.token = ''     ## Disable token authentication
c.ServerApp.password = ''  ## Optional: Disable password (not recommended for public servers)
c.ServerApp.allow_origin = '*'         ## Allow access from any origin
c.ServerApp.disable_check_xsrf = True  ## Disable XSRF checks
c.ServerApp.cookie_options = {"SameSite": "None", "Secure": True}
