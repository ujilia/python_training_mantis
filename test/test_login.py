
def test_login(app):
    # if app.session.is_logged_in_as == "administrator":
    #     app.session.logout()
    # app.session.login("administrator", "root")
    print(app.session.get_logged_user())
    assert app.session.is_logged_in_as("administrator")
