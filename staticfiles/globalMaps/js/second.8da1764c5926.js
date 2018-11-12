var k = 0.5;
var hexW = 108*k;
var hexH = 123*k;
var countO = 100;




var imgs = [
    'desert_plain.png',
    'desrt_hill.png',
    'grass_fertility.png',
    'grass_forest.png',
    'grass_hill.png',
    'grass_hunt.png',
    'grass_plain.png',
    'grass_swamp.png',
    'snow_fertility.png',
    'snow_forest.png',
    'snow_hill.png',
    'snow_hunt.png',
    'snow_mountain.png',
    'snow_plain.png',
]




var select_img = imgs[0];




function Hex(i,j) {
    var _img = imgs[ getRandomInt(0,imgs.length) ];
    var _y=i;
    var _x=j;
    var _class="hex "+(_y%2==0?"even":"odd");
    var _html = '<span>'+_x+"-"+_y+'</span>';
    var _w = hexW;
    var _h = hexH;
    var _top = _h * 0.75 * _y ;
    var _left = _w * _x + (_y%2==0? 0 : _w * 0.5);
    var _data = {
        img:_img,
            x:_x,
            y:_y
    }


    return {
        rendered: false,
        getElement : function () {
            var el = document.createElement('div');
            //el.innerHTML = _html;
            el.className = _class;

            el.style.backgroundImage = 'url(static/global_maps/img/'+_img+')'; //ГОВНОКОД - ПЕРЕДЕЛАТЬ
            el.style.width = _w+'px';
            el.style.height = _h+'px';
            el.style.top = _top+'px';
            el.style.left = _left+'px';
            el.data = _data;
            el.addEventListener('click', function () {
				//el.style.backgroundImage = 'url(img/' + select_img + ')';

                //alert(this.data.x+"-"+this.data.y);
                //console.log(this.data);
            })
            return el;
        }
    };
}




var cont = document.getElementById("container");

cont.style.height=hexH*.75*countO+'px';
cont.style.width=hexW*countO+'px';
var posX = 0;
var posY = 0;
var R;
var windowH = window.innerHeight;
var windowW = window.innerWidth;
var scrollX = 0;
var scrollY = 0;

window.addEventListener('scroll',function() {
  clearTimeout(R);
  R=setTimeout(render, 300);
});

var render = function() {
    scrollY = window.pageYOffset || document.documentElement.scrollTop;
    scrollX = window.pageXOffset || document.documentElement.scrollLeft;
    windowW = window.innerWidth;
    windowH = window.innerHeight;

    cont.innerHTML = "";
    var obj;

	posX = Math.ceil(scrollX/hexW-1);
    posY = Math.ceil(scrollY/(hexH*0.75));

	var countX = Math.ceil(windowW / hexW * 1.2);
    var countY = Math.ceil(windowH / hexH * 1.2);

	for (var i = -2; i < countY ; i++) {
		for (var j = -2; j < countX ; j++) {
			if(posY+i>=0 && posX+j>=0 && posY+i<countO && posX+j<countO){
				obj = objects[posY+i][posX+j];
				cont.appendChild(obj.getElement());
			}
		}
	}
}

var eventScroll = new Event('scroll');
window.dispatchEvent(eventScroll);

function getRandomInt(min, max) {
  return Math.floor(Math.random() * (max - min)) + min;
}
