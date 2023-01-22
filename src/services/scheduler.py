from rocketry import Rocketry


app = Rocketry(execution="async")


@app.task("every 5 seconds")
async def do_things():
    print("Task done")


if __name__ == "__main__":
    app.run()
