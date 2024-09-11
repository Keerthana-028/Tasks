random_value={
    "h1": "welocome to the page",
    "h2": "Hi i am keerthana"
}
def jquery_command(command):
    if command =="$('h1').text()":
        return random_value["h1"]
    elif command =="$('h2').text()":
        return random_value["h2"]
    elif command.startswith("$('h1').text("):
        new_text = command.split("text('")[1].rstrip("')")
        random_value["h1"] = new_text
        return f"Updated h1 text to: {new_text}"

if __name__=='__main__':
    print(jquery_command("$('h1').text()"))
    print(jquery_command("$('h2').text()"))
    print(jquery_command("$('h1').text('this page is being updated')"))
    