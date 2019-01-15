/**
 * Created by tarena on 19-1-7.
 */
function createXhr() {
    var xhr = null;
    if (window.XMLHttpRequest) {
        xhr = new XMLHttpRequest();
    } else {
        xhr = new ActiveXObject("Microsoft.XMLHTTP");
    }
    return xhr;
}