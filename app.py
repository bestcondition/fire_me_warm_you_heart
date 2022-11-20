from flask import Flask, render_template, request

app = Flask(__name__, template_folder='template')


@app.route('/')
def index():
    kwargs = dict(
        first='AA',
        second='BB',
        title='heart',
        alert=True,
    )
    kwargs.update(request.args)
    kwargs.update(alert=kwargs['alert'] != '0')
    return render_template(
        template_name_or_list='index.html',
        **kwargs,
    )


def main():
    app.run()


if __name__ == '__main__':
    main()
