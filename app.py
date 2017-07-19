import logging

import click
from flask import Flask, redirect

log = logging.getLogger(__name__)

PEP_URL_TPL = "https://www.python.org/dev/peps/pep-{:04d}/"


app = Flask(__name__)


@app.route("/")
def index():
    return "<h1>pep.fyi</h1><p>Usage: go to <b>https://pep.fyi/&lt;pep-number&gt;</b> to be redirected to the corresponding <a href='https://www.python.org/dev/peps/pep-0001/'>PEP</a></p><p>Alternatively enter the pep number below:<br><input type='text' id='number'><button id='go'>Go</button><script>document.getElementById('go').onclick=function() {window.location.href=window.location.href + document.getElementById('number').value}</script>"


@app.route("/<int:number>")
def pep(number):
    log.info("PEP: %d", number)
    return redirect(PEP_URL_TPL.format(number))

@click.command()
@click.option("--bind-host", default="127.0.0.1")
@click.option("--bind-port", default=5000)
def main(bind_host, bind_port):
    app.run(host=bind_host, port=bind_port)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s: %(message)s")
    main()
