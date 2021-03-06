from django.shortcuts import render
from django.shortcuts import render_to_response
from global_maps.models import Landscape, Cell
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, 'globalmaps/maps.html')

@login_required(login_url="/account/login/")
def global_maps_view(request):
    list_of_cells = Cell.objects.all()
    list_of_hex = [];

    for cell in list_of_cells:
      #  my_landscape = Landscape.objects.filter(id__contains = cell.landscape_id)
        my_landscape = Landscape.objects.get(id__contains=cell.landscape_id)
        hex = Hex(cell.coord_x, cell.coord_y, my_landscape.img)
        list_of_hex.append(hex)

    return render_to_response('globalMaps/maps.html', {'list': list_of_hex})



class Hex:
    img = "desert_hill.png";
    coord_x = 1;
    coord_y = 0;
    hex_width = 105;
    hex_height = 123;

    #_class = "hex " + (_y % 2 == 0?"even":"odd");
    #_html = '<span>' + _x + "-" + _y + '</span>';

    def __init__(self, x, y, img="desrt_hill.png"):
        self.coord_x = x
        self.coord_y = y
        self.img = img

    def top(self):
        return self.hex_height * 0.75 * self.coord_y

    def left(self):
        if(self.coord_y %2 ==0):
            return self.hex_width * self.coord_x
        else:
            return self.hex_width * self.coord_x + self.hex_width*0.5



