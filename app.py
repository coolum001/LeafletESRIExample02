'''
Web app to display water quality measurement sites via Leaflet

Map will be positioned and zoomed so that all sites are visible

'''

from flask import Flask
from flask import render_template
from flask import flash

# import object holding app-specific configuration
from config import Config

app = Flask(__name__)
app.config.from_object(Config)


def entry_render(link: str, title: str = " ", salutation: str = "Friend"):
    '''
    entry_render: render Flask template, to display map
    
    The Leaflet and Mapbox Javascript is different, so a different
    template is used for each. However they all take the same parameters
    
    Parameters:
    link: str holding the name of the Flask template to be rendered
    title: str holding HTML title to be included in generated HTML
    salutation: str holding greeting displayed to user
    
    Returns:
    whatever render_template returns (str holding HTML?)

    Side Effects:
    creates page to be displayed in browser via Flask @app.route
    '''
    return render_template(link, title=title, salutation=salutation)


# end entry_render


@app.route('/')
def hello():
    '''
    hello: create initial html page of app
    '''
    # entry from url
    return entry_render(
        link='index.html', title='Web Mapping Example', salutation='Buddy'
    )


# end index


@app.route('/index')
def index():
    '''
    index: create app page html after "ESRI Map" menu choice selection
    '''
    # back to initial screen via Leaflet menu choice
    flash('Home request seen')
    return entry_render('index.html', title='Web Mapping Example', salutation='Chum')


# end index


@app.route('/esrimap')
def esrimap():
    '''
    esrimap: create html to display a esri map in browser
    '''
    # back to initial screen via Mapbox menu choice
    flash('ESRI request seen')
    return entry_render('esrimap.html', title='ESRI Map Example', salutation='Friend')


# end esrimap


if __name__ == "__main__":
    app.run()
# end if
