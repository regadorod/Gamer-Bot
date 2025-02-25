import discord
from utils import logging, colors


def get_platform_colors(platform):
    color_data = {}
    match platform:
        case "Spotify":
            color_data["platform_logo"] = (
                "https://upload.wikimedia.org/wikipedia/commons/thumb/1/19/Spotify_logo_without_text.svg/2048px-Spotify_logo_without_text.svg.png"
            )
            color_data["notes"] = "<:notes_green:1217928189070807202>"
            color_data["color"] = int(
                colors.SPOTIFY_GREEN, 16
            )  # #25d865 green | Have to convert hex to decimal form for Discord.py embed
            color_data["emoji"] = "<:spotify:1220523061778845746>"
        case "Youtube":
            color_data["platform_logo"] = (
                "https://1000logos.net/wp-content/uploads/2017/05/Red-YouTube-logo.png"
            )
            color_data["notes"] = "<:notes_solid_red:1217928191507697805>"
            color_data["color"] = int(colors.YOUTUBE_RED, 16)  # #ed5c5c red
            color_data["emoji"] = "<:YouTube:1220522718680846376>"
        case _:
            # color_data['platform_logo'] = "https://listen.moe/_nuxt/img/logo-square-64.248c1f3.png"
            color_data["platform_logo"] = (
                "https://upload.wikimedia.org/wikipedia/en/thumb/9/9e/Flag_of_Japan.svg/1280px-Flag_of_Japan.svg.png"
            )
            color_data["notes"] = ":notes:"
            color_data["color"] = int(colors.RADIO_BLUE, 16)  # #5dadec blue
            color_data["emoji"] = "<:google:1220523203978596413>"

    return color_data


def queue_song(
    requester: discord.Member,
    queue_size=0,
    song_title="Song Title",
    song_artist="",
    song_url="",
    duration_string="",
    thumbnail="",
    platform="Spotify",
):
    """Creates embed with the song data and queue postion."""

    color_data = get_platform_colors(platform)
    color = color_data["color"]
    emoji = color_data["emoji"]

    if platform == "Youtube":
        embed = discord.Embed(title="Added Youtube song to queue!", color=color)
    else:
        embed = discord.Embed(
            title=f"{song_title}",
            description=(f"by {song_artist} | " if song_artist else "")
            + (f"`{duration_string}` | " if duration_string else "")
            + f"[{emoji} Song Link]({song_url})",
            color=color,
        )
        embed.set_author(
            name=f"| @{requester.display_name} Added to Queue ~",
            icon_url="https://images.emojiterra.com/google/noto-emoji/unicode-15/color/512px/1f338.png",
        )
        embed.set_thumbnail(url=f"{thumbnail}")
        embed.set_footer(
            text="Will play soon!" if queue_size <= 1 else f"Position #{queue_size}",
            icon_url="https://imgur.com/PKi66Gs.png",
        )
    return embed


def now_playing(
    requester: discord.Member,
    song_title="Song Title",
    song_artist="",
    song_url="",
    duration_string="",
    platform="Spotify",
    thumbnail="",
):
    """Creates embed with the currently playing song's data."""

    # Change color of embed depending on platform
    color_data = get_platform_colors(platform)
    color = color_data["color"]
    notes = color_data["notes"]
    emoji = color_data["emoji"]
    platform_logo = color_data["platform_logo"]

    # Build embed
    embed = discord.Embed(
        title=f"{notes} {song_title} {notes}",
        description=(f"by {song_artist}  |  " if song_artist else "")
        + (
            f"`{duration_string}` | "
            if duration_string and duration_string != "00:00"
            else ""
        )
        + f"[{emoji} Song Link]({song_url})",
        color=color,
    )
    embed.set_author(name=f"Now Playing")
    if thumbnail:
        embed.set_thumbnail(url=thumbnail)
    embed.set_footer(
        text=(
            f"{platform} (c) 2024"
            if platform == "listen.moe"
            else f"| Requested by: @{requester.display_name}"
        ),
        icon_url=(
            platform_logo if platform == "listen.moe" else f"{requester.display_avatar}"
        ),
    )
    return embed
