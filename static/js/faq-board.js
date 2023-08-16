$('dl').each( function() { 
        var dl = $(this);
        var alldd = dl.find("dd");
        var alldt = dl.find("dt");
        alldd.hide();
        alldt.css("cursor","pointer");
        alldt.click(function(){
            alldd.hide();
            var dt = $(this);
            var dd = dt.next();
            dd.show();
            alldt.css("cursor","pointer");
            closeAll();
            open(dt , dd);
        })
        function closeAll() {
            alldd.addClass("closed");
            alldt.addClass("closed");
        }
        function open(dt, dd) {
            dt.removeClass("closed");
            dd.removeClass("closed");
        }
    });
