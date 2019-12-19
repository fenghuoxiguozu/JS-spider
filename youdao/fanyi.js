// const jsdom = require("jsdom");
// const { JSDOM } = jsdom;
// const dom = new JSDOM(`<!DOCTYPE html><p>Hello world</p>`);
// window = dom.window;
// document = window.document;
// XMLHttpRequest = window.XMLHttpRequest;
//
//
var md5 = require('md5-node');

r = "" + (new Date).getTime()
i = r + parseInt(10 * Math.random(), 10);
salt = i;

i = r + parseInt(10 * Math.random(), 10);
sign= md5("fanyideskweb"  + i + "n%A-rKaT5fb[Gy?;N5@Tj")

function get_salt(){
    return salt
}

function get_sign(){
    return sign
}