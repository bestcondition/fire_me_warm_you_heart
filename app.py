from flask import Flask, render_template, request

from config import config

app = Flask(__name__, template_folder='template')


@app.route('/')
def index():
    kwargs = dict(
        first=config.FIRST,
        second=config.SECOND,
        title=config.TITLE,
        alert=config.ALERT,
    )
    kwargs.update(request.args)
    kwargs.update(alert=kwargs['alert'] != config.NOT_ALERT_VALUE)
    return render_template(
        template_name_or_list='index.html',
        **kwargs,
    )


def main():
    app.run()


if __name__ == '__main__':
    main()
