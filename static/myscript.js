function gizle() {

    var x = document.getElementById("yuk_dur").value;

    if (x == "1") {

        document.getElementById("resim1").style.opacity = 1;
        document.getElementById("resim2").style.opacity = 0.3;
        document.getElementById("resim3").style.opacity = 0.3;
        document.getElementById("resim4").style.opacity = 0.3;

        document.getElementById("ww").style.display = "block";
        document.getElementById("ww2").style.display = "block";
        document.getElementById("p_degeri").style.display = "none";
        document.getElementById("p_degeri2").style.display = "none";
        document.getElementById("qq").style.display = "none";
        document.getElementById("qq2").style.display = "none";

    }

    else if (x == "7") {
        document.getElementById("resim2").style.opacity = 1;
        document.getElementById("resim1").style.opacity = 0.3;
        document.getElementById("resim3").style.opacity = 0.3;
        document.getElementById("resim4").style.opacity = 0.3;

        document.getElementById("ww").style.display = "none";
        document.getElementById("ww2").style.display = "none";
        document.getElementById("p_degeri").style.display = "block";
        document.getElementById("p_degeri2").style.display = "block";
        document.getElementById("qq").style.display = "block";
        document.getElementById("qq2").style.display = "block";
    }

    else if (x == "19") {

        document.getElementById("resim3").style.opacity = 1;
        document.getElementById("resim1").style.opacity = 0.3;
        document.getElementById("resim2").style.opacity = 0.3;
        document.getElementById("resim4").style.opacity = 0.3;

        document.getElementById("ww").style.display = "block";
        document.getElementById("ww2").style.display = "block";
        document.getElementById("p_degeri").style.display = "none";
        document.getElementById("p_degeri2").style.display = "none";
        document.getElementById("qq").style.display = "none";
        document.getElementById("qq2").style.display = "none";
    }

    else if (x == "22") {

        document.getElementById("resim4").style.opacity = 1;
        document.getElementById("resim1").style.opacity = 0.3;
        document.getElementById("resim2").style.opacity = 0.3;
        document.getElementById("resim3").style.opacity = 0.3;

        document.getElementById("ww").style.display = "none";
        document.getElementById("ww2").style.display = "none";
        document.getElementById("p_degeri").style.display = "block";
        document.getElementById("p_degeri2").style.display = "block";
        document.getElementById("qq").style.display = "block";
        document.getElementById("qq2").style.display = "block";
    }

}

function printDiv() {
    var divContents = document.getElementById("aciklama").innerHTML;
    var a = window.open('', '', 'height=500, width=500');
    a.document.write('<html>');
    a.document.write('<body ><br>');
    a.document.write(divContents);
    a.document.write('</body></html>');
    a.document.close();
    a.print();
}

