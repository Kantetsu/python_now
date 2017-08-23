from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)
from IPython import embed

import settings

app = Flask(__name__)

line_bot_api = LineBotApi(settings.LINE_ACCESS_TOKEN)
handler = WebhookHandler(settings.LINE_CHANNEL_SECRET)


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    if event.message.text == "ハッカソン":
        message = TextSendMessage(text="優勝以上優勝未満なんで")
    elif event.message.text == "社員紹介":
        message = StickerSendMessage(
            package_id='1',
            sticker_id='1'
        )
    else:
        message = StickerSendMessage(
            package_id='1',
            sticker_id='1'
        )

    line_bot_api.reply_message(
        event.reply_token,
        message)


def workers_introduction():
    carousel_template_message = TemplateSendMessage(
        alt_text='Carousel template',
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    thumbnail_image_url='',
                    title='あああ',
                    text='素敵な社長さん',
                    actions=[
                        URITemplateAction(
                            label='参考URL',
                            uri='http://www.nowhere.co.jp/culture/staff/yamadera.html'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='',
                    title='あああ',
                    text='素敵な社長さん',
                    actions=[
                        URITemplateAction(
                            label='参考URL',
                            uri='http://www.nowhere.co.jp/culture/staff/yamadera.html'
                        )
                    ]
                )
            ]
        )
    )
    return carousel_template_message


if __name__ == "__main__":
    app.run()
