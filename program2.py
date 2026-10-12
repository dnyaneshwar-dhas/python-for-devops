
#(2)
def checking_server(name, status):
    print("Server Name:", name)
    print("Server Status:", status)

    check_server("web_server", "running")
    check_server("db_server", "stopped")
