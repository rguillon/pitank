import json

from MicroWebSrv2  import *
from  devices import dimmer1, dimmer2, dimmer3

@WebRoute(GET, '/light1', name='light1')
def RequestTestPost(microWebSrv2, request) :
    content = """\
        <!DOCTYPE html>
        <html>
            <head>
                <title>Light 1</title>
                <link rel="stylesheet" href="style.css" />
            </head>
            <body>
                <h2>Light 1</h2>
                
                <br />
                <form action="/light1" method="post">
                    Dimmer Table  <input type="text" name="table" value="%s", size=100><br />
                    Test slider <input type="range" name="t1", min=0, max=4095>
                    <br>
                    <input type="submit" value="OK">
                </form>
           </body>
        </html>
    """ % json.dumps(dimmer1.get_time_table())
    request.Response.ReturnOk(content)



@WebRoute(POST, '/light1', name='light1 update')
def RequestTestPost(microWebSrv2, request) :
    data = request.GetPostedURLEncodedForm()
    try :
        new_schedule = json.loads(data['table'])
        dimmer1.set_time_table(new_schedule)
        print("OK")
    except :
        request.Response.ReturnBadRequest()
        return
    request.Response.ReturnRedirectGet('/light1')

    
    

def config_mws():
    # All pages not found will be redirected to the home '/',
    mws2.SetEmbeddedConfig()
    mws2.NotFoundURL = '/'

# Instanciates the MicroWebSrv2 class,
mws2 = MicroWebSrv2()


