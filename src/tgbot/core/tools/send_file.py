from typing import Optional

from pydantic import BaseModel, Field

from . import register_tool


@register_tool(name="send_file")
class SendFile(BaseModel):
    file: int = Field(
        ...,
        description="Index of the list of used functions, used to get the file object from it",
    )
    caption: Optional[str] = Field(
        None,
        description="Optional caption for the sent media message. When sending an album, the caption may be a list of strings, which will be assigned to the files pairwise.",
    )
    force_document: Optional[bool] = Field(
        None,
        description="If left to False and the file is a path that ends with the extension of an image file or a video file, it will be sent as such. Otherwise always as a document.",
    )
    file_size: Optional[int] = Field(
        None,
        description="The size of the file to be uploaded if it needs to be uploaded, which will be determined automatically if not specified. If the file size can’t be determined beforehand, the entire file will be read in-memory to find out how large it is.",
    )
    reply_to: Optional[int] = Field(
        None, description="Same as reply_to from send_message."
    )
    voice_note: Optional[bool] = Field(
        None, description="If True the audio will be sent as a voice note."
    )
    video_note: Optional[bool] = Field(
        None,
        description="If True the video will be sent as a video note, also known as a round video message.",
    )
    silent: Optional[bool] = Field(
        None,
        description="Whether the message should notify people with sound or not. Defaults to False (send with a notification sound unless the person has the chat muted). Set it to True to alter this behaviour.",
    )
    background: Optional[bool] = Field(
        None, description="Whether the message should be send in background."
    )
    supports_streaming: Optional[bool] = Field(
        None,
        description="Whether the sent video supports streaming or not. Note that Telegram only recognizes as streamable some formats like MP4, and others like AVI or MKV will not work. You should convert these to MP4 before sending if you want them to be streamable. Unsupported formats will result in VideoContentTypeError.",
    )
    comment_to: Optional[int] = Field(
        None,
        description="Similar to reply_to, but replies in the linked group of a broadcast channel instead (effectively leaving a “comment to” the specified message). This parameter takes precedence over reply_to. If there is no linked chat, telethon.errors.sgIdInvalidError is raised.",
    )
    nosound_video: Optional[bool] = Field(
        None,
        description="Only applicable when sending a video file without an audio track. If set to True, the video will be displayed in Telegram as a video. If set to False, Telegram will attempt to display the video as an animated gif. (It may still display as a video due to other factors.) The value is ignored if set on non-video files. This is set to True for albums, as gifs cannot be sent in albums.",
    )
