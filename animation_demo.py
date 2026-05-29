import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter


steps = [

    {
        "title": "Initial states",
        "left": [1, 2, 3, 4],
        "right": [5, 6, 7, 8],
        "result": None,
        "states": 24
    },

    {
        "title": "First weighing",
        "left": [1, 2, 3, 4],
        "right": [5, 6, 7, 8],
        "result": "LEFT HEAVIER",
        "states": 8
    },

    {
        "title": "Second weighing",
        "left": [1, 2, 5],
        "right": [3, 6, 9],
        "result": "BALANCE",
        "states": 2
    },

    {
        "title": "Third weighing",
        "left": [3],
        "right": [1],
        "result": "LEFT HEAVIER",
        "states": 1
    },

    {
        "title": "FOUND",
        "left": [],
        "right": [],
        "result": "3 HEAVY",
        "states": 1
    }
]


fig, ax = plt.subplots(figsize=(12, 7))

fig.patch.set_facecolor("#1e1e1e")


def draw_coin(x, y, label, color):

    circle = plt.Circle(
        (x, y),
        0.35,
        color=color
    )

    ax.add_patch(circle)

    ax.text(
        x,
        y,
        str(label),
        ha="center",
        va="center",
        fontsize=14,
        color="black",
        fontweight="bold"
    )


def draw_scale(result):

    left_y = 3
    right_y = 3

    if result == "LEFT HEAVIER":
        left_y = 2.5
        right_y = 3.5

    elif result == "RIGHT HEAVIER":
        left_y = 3.5
        right_y = 2.5

    ax.plot(
        [3, 9],
        [left_y, right_y],
        color="white",
        linewidth=4
    )

    ax.plot(
        [6, 6],
        [1, 4],
        color="white",
        linewidth=4
    )

    ax.plot(
        [2, 4],
        [left_y, left_y],
        color="#F8BBD0",
        linewidth=6
    )

    ax.plot(
        [8, 10],
        [right_y, right_y],
        color="#F8BBD0",
        linewidth=6
    )

    return left_y, right_y


def update(frame):

    ax.clear()

    ax.set_facecolor("#1e1e1e")

    ax.set_xlim(0, 12)
    ax.set_ylim(0, 8)

    ax.axis("off")

    step = steps[frame]

    title = step["title"]

    ax.set_title(
        title,
        fontsize=24,
        color="white",
        pad=20
    )

    result = step["result"]

    if title != "FOUND":

        left_y, right_y = draw_scale(result)

        # left coins
        x = 2.3

        for coin in step["left"]:

            draw_coin(
                x,
                left_y + 0.7,
                coin,
                "#98FB98"
            )

            x += 0.5

        # right coins
        x = 8.3

        for coin in step["right"]:

            draw_coin(
                x,
                right_y + 0.7,
                coin,
                "#FFB6C1"
            )

            x += 0.5

    # result text
    if result:

        color = "#77DD77"

        if "HEAVIER" in result:
            color = "#FFD580"

        ax.text(
            6,
            6,
            result,
            fontsize=22,
            color=color,
            ha="center",
            fontweight="bold"
        )

    # states
    ax.text(
        6,
        0.7,
        f"Remaining states: {step['states']}",
        fontsize=18,
        color="#C8E6C9",
        ha="center"
    )


animation = FuncAnimation(
    fig,
    update,
    frames=len(steps),
    interval=4000,
    repeat=False
)

animation.save(
    "fake_coin_demo.gif",
    writer=PillowWriter(fps=1)
)

print("Saved: fake_coin_demo.gif")

plt.show()