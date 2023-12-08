from playwright.sync_api import Page, expect, TimeoutError 



# Tests for your routes go here


def test_get_goodbye(page, test_web_address):
    page.goto(f"http://{test_web_address}/goodbye")
    strong_tag = page.locator("strong")
    expect(strong_tag).to_have_text("Bye!")

def test_get_albums(page, test_web_address, db_connection):
    db_connection.seed('seeds/music_library2.sql')
    page.goto(f"http://{test_web_address}/albums")
    # strong_tag = page.locator("strong")
    paragraph_tag1 = page.locator("li")
    # expect(strong_tag).to_have_text("Title:Doolittle Released:1989 Title:Surfer Rosa Released:1988 Title:Waterloo Released:1974 Title:Super Trouper Released:1980")
    expect(paragraph_tag1).to_have_text([
        "Doolittle",
        "Surfer Rosa",
        "Waterloo",
        "Super Trouper"
    ])

def test_album_link(page, test_web_address, db_connection):
    db_connection.seed('seeds/music_library2.sql')
    page.goto(f"http://{test_web_address}/albums")
    page.click("text='Surfer Rosa'", timeout = 5000)
    h1_tag = page.locator("h1")
    expect(h1_tag).to_have_text("Surfer Rosa")
    p1_tag = page.locator("p1")
    expect(p1_tag).to_have_text("1988")
    
def test_add_new_album(page, test_web_address, db_connection):
    


# === Example Code Below ===

"""
We can get an emoji from the /emoji page
"""
def test_get_emoji(page, test_web_address): # Note new parameters
    # We load a virtual browser and navigate to the /emoji page
    page.goto(f"http://{test_web_address}/emoji")

    # We look at the <strong> tag
    strong_tag = page.locator("strong")

    # We assert that it has the text ":)"
    expect(strong_tag).to_have_text(":)")

# === End Example Code ===
