
import click
from process.singleprocess import single_main_steam
from process.multiprocess import multi_main_stream

def print_explanation():
    help_str = """
    This is stream demo application.
    Use following parameters to activate it
    single - to activate single process data stream demo
    multi - to activate multi process data stream demo

    Any other options will show this help message
    """
    print(help_str)

@click.command()
@click.argument("streamtype", default="help")
def activate_stream_flow(streamtype:str):
    if streamtype == "single":
        single_main_steam()
    elif streamtype == "multi":
        multi_main_stream()
    else:
        print_explanation()

    
if __name__ == "__main__":

    activate_stream_flow() 