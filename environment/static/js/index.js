function style() {
    var udata = "{{case.estimate}}";
    if (udata >= 5) {
        document.getElementById("case").style.backgroundColor = '#99C262';
    }
    else if (udata >= 5) {
        document.getElementById("case").style.backgroundColor = '#F8D347';
    }
}