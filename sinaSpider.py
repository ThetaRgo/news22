#!/usr/bin/env python
# encoding:utf-8
# @Time   : 2018/6/4
# @Author : 茶葫芦
# @Site   : 
# @File   : sinaSpider.py

import requests
from USER_AGENT import USER_AGENT_LIST
import random
from lxml import etree

"""新浪爬虫"""
class sina():
    """
    1.拿到新浪首页,取得指定模块的新闻链接4
    2.打开新闻链接,爬取内容(已经爬过的网页不再爬取)
    3.爬取的内容入库,爬取过的网页入库
    """
    def getNews(self):
        # mainPage=requests.get("http://news.sina.com.cn/",headers={"User-Agent":random.choice(USER_AGENT_LIST)})


        contexthtml='''
        <!DOCTYPE html>
<!-- [ published at 2018-06-04 22:20:01 ] -->
<html>
<head>
<meta http-equiv="Content-type" content="text/html; charset=utf-8" />
<title>新闻中心首页_新浪网</title>
<meta name="keywords" content="新闻,时事,时政,国际,国内,社会,法治,聚焦,评论,文化,教育,新视点,深度,网评,专题,环球,传播,论坛,图片,军事,焦点,排行,环保,校园,法治,奇闻,真情">
<meta name="description" content="新浪网新闻中心是新浪网最重要的频道之一，24小时滚动报道国内、国际及社会新闻。每日编发新闻数以万计。">
<meta name="robots" content="noarchive">
<meta name="Baiduspider" content="noarchive">
<meta http-equiv="Cache-Control" content="no-transform">
<meta http-equiv="Cache-Control" content="no-siteapp">
<meta name="applicable-device" content="pc,mobile">
<meta name="MobileOptimized" content="width">
<meta name="HandheldFriendly" content="true">
<link rel="mask-icon" sizes="any" href="//www.sina.com.cn/favicon.svg" color="red">
	<script charset="utf8" type="text/javascript" src="//int.dpool.sina.com.cn/iplookup/iplookup.php?format=js"></script>
	     <script charset="utf8" type="text/javascript" src="//n.sinaimg.cn/news/components/switch_cookie.js"></script>
<link rel="alternate" type="application/rss+xml" href="http://rss.sina.com.cn/news/marquee/ddt.xml" title="新闻中心_新浪网" />
<meta name="stencil" content="PGLS000023" />
<meta name="publishid" content="1,912,1" />
<meta name="verify-v1" content="6HtwmypggdgP1NLw7NOuQBI2TW8+CfkYCoyeB8IDbn8=" />
<meta name="msvalidate.01" content="0EBC6AF737F6405C0F32D73B4AA6A640" />
<meta name="apple-mobile-web-app-status-bar-style" content="black">
<meta name="viewport" content="width=device-width, initial-scale=1.0, minimum-scale=1.0, maximum-scale=1.0, user-scalable=no"/>
<link rel="apple-touch-icon" href="http://i0.sinaimg.cn/dy/news3.png" />

<!-- id="news_web_index_v2015_style" -->
<link rel="stylesheet" href="//n2.sinaimg.cn/news/project/index-2018-nc.css" type="text/css">
<link rel="stylesheet" href="//n3.sinaimg.cn/news/project/index.css?20180209012" type="text/css">

<!-- AD_cross_domain -->
<script type="text/javascript">
  document.domain = "sina.com.cn";
</script>
<!-- AD_cross_domain -->

<!--<script type="text/javascript" src="http://news.sina.com.cn/js/268/index2015/jsloader.js"></script>-->
<script charset="gb2312" type="text/javascript" src="//int.dpool.sina.com.cn/iplookup/iplookup.php?format=js"></script>
<!-- <script src="//news.sina.com.cn/js/pctianyi/sima.js"></script> -->
	<script src="//n.sinaimg.cn/news/components/common.js" ></script>
<script>
//js地址
var ARTICLE_JSS = {
		//swit
    jq: {url:'//i0.sinaimg.cn/dy/js/jquery/jquery-1.7.2.min.js', charset:'utf-8'},
    common: {url:'//news.sina.com.cn/js/268/index2015/common.js', charset:'utf-8'},
    ssologin: {url:'//i.sso.sina.com.cn/js/ssologin.js', charset:'utf-8'},
    base: {url:'//news.sina.com.cn/js/268/index2015/base.js', charset:'utf-8'},
		user_panel : {url:'//i.sso.sina.com.cn/js/user_panel.js', charset:'utf-8'},
		sinalib : '//news.sina.com.cn/js/87/20110714/205/sinalib.js',
		weibo_all :'//news.sina.com.cn/js/268/2011/1110/16/weibo-all.js'
};

jsLoader(ARTICLE_JSS.ssologin)
//jsLoader(ARTICLE_JSS.iplookup)

</script>
	<script>
    	jsLoader(ARTICLE_JSS.jq,function(){
			(function($) {
    $(function() {
    	if (typeof remote_ip_info.city !== 'undefined') {
    	    if (remote_ip_info.province !== '北京') {
    	        var jsStr = 'http://n.sinaimg.cn/news/components/switchVersion.min.js?20171201';
    	        $.getScript(jsStr, function() {
    	            var lickOldVersion = switchVersionSima.getCookie('lickOldVersion');

    	            if (lickOldVersion) {
    	                switchVersionSima.delCookie({ key: 'lickOldVersion' })
    	                switchVersionSima.setCookie({ key: 'switchVersion', value: lickOldVersion })
    	            }

    	            $('.new_version').css('display', 'block');

    	            $('.new_version').click(function() {
    	                var obj = {
    	                    switchVersion: 'ab',
    	                    time: 500,
    	                };
    	                switchVersionSima.click(obj);
    	            });
    	        });

    	    }
    	}
    })
    

})(jQuery)
		})
    </script>

<!-- SinaDotTop begin -->
<script type="text/javascript" src="//news.sina.com.cn/js/792/2012-08-09/41/headnews.js" charset="gbk"></script>
<!-- SinaDotTop end -->
<!--新闻中心轮播新浪广告js-->
<script type="text/javascript" src="//news.sina.com.cn/pfpnews/js/libweb.js" charset="gbk"></script>
<!-- 乐居广告js start-->
<script charset="utf-8" src="//d5.sina.com.cn/litong/zhitou/leju/leju.js"></script>
<script>
  //不安全
  leju.conf.url = 'http://adm.leju.sina.com.cn/get_ad_list/PG_514AC4246D2142';
  leju.conf.defaultUrl = '//d3.sina.com.cn/litong/zhitou/leju/news.js';
  var lejuMedia = leju.getData();
</script>
<!-- 乐居广告js end -->

<script type="text/javascript" src="//d1.sina.com.cn/litong/zhitou/sspnew.js"></script>

<script type="text/javascript">
/**
 * sina flash class
 * @version 1.1.4.3
 * @update 2012-6-26 
 */ 
if(typeof(sina)!="object"){var sina={}}
sina.$=function(i){if(!i){return null}
return document.getElementById(i)};var sinaFlash=function(V,x,X,Z,v,z,i,c,I,l,o){var w=this;if(!document.createElement||!document.getElementById){return}
w.id=x?x:'';var O=function(I,i){for(var l=0;l<I.length;l++){if(I[l]==i){return l}}
return-1},C='8.0.42.0';if(O(['eladies.sina.com.cn','ent.sina.com.cn'],document.domain)>-1){w.ver=C}else{w.ver=v?v:C}
w.ver=w.ver.replace(/\./g,',');w.__classid="clsid:D27CDB6E-AE6D-11cf-96B8-444553540000";w.__codebase="http://download.macromedia.com/pub/shockwave/cabs/flash/swflash.cab#version="+w.ver;w.width=X;w.height=Z;w.movie=V;w.src=w.movie;w.bgcolor=z?z:'';w.quality=c?c:"high";w.__pluginspage="http://www.macromedia.com/go/getflashplayer";w.__type="application/x-shockwave-flash";w.useExpressInstall=(typeof(i)=="boolean")?i:false;w.xir=I?I:window.location;w.redirectUrl=l?l:window.location;w.detectKey=(typeof(o)=="boolean")?o:true;w.escapeIs=false;w.__objAttrs={};w.__params={};w.__embedAttrs={};w.__flashVars=[];w.__flashVarsStr="";w.__forSetAttribute("id",w.id);w.__objAttrs["classid"]=w.__classid;w.__forSetAttribute("codebase",w.__codebase);w.__forSetAttribute("width",w.width);w.__forSetAttribute("height",w.height);w.__forSetAttribute("movie",w.movie);w.__forSetAttribute("quality",w.quality);w.__forSetAttribute("pluginspage",w.__pluginspage);w.__forSetAttribute("type",w.__type);w.__forSetAttribute("bgcolor",w.bgcolor)}
sinaFlash.prototype={getFlashHtml:function(){var I=this;
if(/\((iPhone|iPad|iPod)/i.test(navigator.userAgent) && I.width>=930 && I.height<100 && /^http\:\/\/d\d\./i.test(I.movie)){return '';}//iOS不投放通栏flash广告
var i='<object ';for(var l in I.__objAttrs){i+=l+'="'+I.__objAttrs[l]+'"'+' '}
i+='>\n';for(var l in I.__params){i+='	<param name="'+l+'" value="'+I.__params[l]+'" \/>\n'}
if(I.__flashVarsStr!=""){i+='	<param name="flashvars" value="'+I.__flashVarsStr+'" \/>\n'}
i+='	<embed ';for(var l in I.__embedAttrs){i+=l+'="'+I.__embedAttrs[l]+'"'+' '}
i+='><\/embed>\n<\/object>';return i},__forSetAttribute:function(I,i){var l=this;if(typeof(I)=="undefined"||I==''||typeof(i)=="undefined"||i==''){return}
I=I.toLowerCase();switch(I){case "classid":break;case "pluginspage":l.__embedAttrs[I]=i;break;case "onafterupdate":case "onbeforeupdate":case "onblur":case "oncellchange":case "onclick":case "ondblClick":case "ondrag":case "ondragend":case "ondragenter":case "ondragleave":case "ondragover":case "ondrop":case "onfinish":case "onfocus":case "onhelp":case "onmousedown":case "onmouseup":case "onmouseover":case "onmousemove":case "onmouseout":case "onkeypress":case "onkeydown":case "onkeyup":case "onload":case "onlosecapture":case "onpropertychange":case "onreadystatechange":case "onrowsdelete":case "onrowenter":case "onrowexit":case "onrowsinserted":case "onstart":case "onscroll":case "onbeforeeditfocus":case "onactivate":case "onbeforedeactivate":case "ondeactivate":case "codebase":l.__objAttrs[I]=i;break;case "src":case "movie":l.__embedAttrs["src"]=i;l.__params["movie"]=i;break;case "width":case "height":case "align":case "vspace":case "hspace":case "title":case "class":case "name":case "id":case "accesskey":case "tabindex":case "type":l.__objAttrs[I]=l.__embedAttrs[I]=i;break;default:l.__params[I]=l.__embedAttrs[I]=i}},__forGetAttribute:function(i){var I=this;i=i.toLowerCase();if(typeof I.__objAttrs[i]!="undefined"){return I.__objAttrs[i]}else if(typeof I.__params[i]!="undefined"){return I.__params[i]}else if(typeof I.__embedAttrs[i]!="undefined"){return I.__embedAttrs[i]}else{return null}},setAttribute:function(I,i){this.__forSetAttribute(I,i)},getAttribute:function(i){return this.__forGetAttribute(i)},addVariable:function(I,i){var l=this;if(l.escapeIs){I=escape(I);i=escape(i)}
if(l.__flashVarsStr==""){l.__flashVarsStr=I+"="+i}else{l.__flashVarsStr+="&"+I+"="+i}
l.__embedAttrs["FlashVars"]=l.__flashVarsStr},getVariable:function(I){var o=this,i=o.__flashVarsStr;if(o.escapeIs){I=escape(I)}
var l=new RegExp(I+"=([^\\&]*)(\\&?)","i").exec(i);if(o.escapeIs){return unescape(RegExp.$1)}
return RegExp.$1},addParam:function(I,i){this.__forSetAttribute(I,i)},getParam:function(i){return this.__forGetAttribute(i)},write:function(i){var I=this;if(typeof i=="string"){document.getElementById(i).innerHTML=I.getFlashHtml()}else if(typeof i=="object"){i.innerHTML=I.getFlashHtml()}}};
</script>

<script type="text/javascript">
// added by chenchen
String.prototype.gbCut = function(n){
  if(!(/^[0-9]*[1-9][0-9]*$/).test(n)){return this};
  if(n == 0){return this};
  var k = 0;
  for (var i=0; i<this.length; i++) {
    if (this.charCodeAt(i)<=127) {
      k += 1;
    } else {
      k += 2;
    }
    if (k>n) {
      var ns = this.substr(0,i);
      return (ns);
    }
  }
  return (this);
};

function commafy(num){
  num = num+"";
  var re=/(-?\d+)(\d{3})/
  while(re.test(num)){
    num=num.replace(re,"$1,$2")
  }
  return num;
}
</script>

<script>
    (function (d, s, id) {
        var s, n = d.getElementsByTagName(s)[0];
        if (d.getElementById(id)) return;
        s = d.createElement(s);
        s.id = id;
        s.setAttribute('charset', 'utf-8');
        s.src = '//d' + Math.floor(0 + Math.random() * (9 - 0 + 1)) + '.sina.com.cn/litong/zhitou/sinaads/release/sinaads.js';
        n.parentNode.insertBefore(s, n);
    })(document, 'script', 'sinaads-script');
</script>
	
<script type="text/javascript">	
	var SUDA = SUDA || []; 
	SUDA.push(["setGatherInfo", '', '2017_old']);  //old version
</script>
	
</head>

<body><!-- body code begin -->

<!-- SUDA_CODE_START --> 
<script type="text/javascript"> 
//<!--
(function(){var an="V=2.1.16";var ah=window,F=document,s=navigator,W=s.userAgent,ao=ah.screen,j=ah.location.href;var aD="https:"==ah.location.protocol?"https://s":"http://",ay="beacon.sina.com.cn";var N=aD+ay+"/a.gif?",z=aD+ay+"/g.gif?",R=aD+ay+"/f.gif?",ag=aD+ay+"/e.gif?",aB=aD+"beacon.sinauda.com/i.gif?";var aA=F.referrer.toLowerCase();var aa="SINAGLOBAL",Y="FSINAGLOBAL",H="Apache",P="ULV",l="SUP",aE="UOR",E="_s_acc",X="_s_tentry",n=false,az=false,B=(document.domain=="sina.com.cn")?true:false;var o=0;var aG=false,A=false;var al="";var m=16777215,Z=0,C,K=0;var r="",b="",a="";var M=[],S=[],I=[];var u=0;var v=0;var p="";var am=false;var w=false;function O(){var e=document.createElement("iframe");e.src=aD+ay+"/data.html?"+new Date().getTime();e.id="sudaDataFrame";e.style.height="0px";e.style.width="1px";e.style.overflow="hidden";e.frameborder="0";e.scrolling="no";document.getElementsByTagName("head")[0].appendChild(e)}function k(){var e=document.createElement("iframe");e.src=aD+ay+"/ckctl.html";e.id="ckctlFrame";e.style.height="0px";e.style.width="1px";e.style.overflow="hidden";e.frameborder="0";e.scrolling="no";document.getElementsByTagName("head")[0].appendChild(e)}function q(){var e=document.createElement("script");e.src=aD+ay+"/h.js";document.getElementsByTagName("head")[0].appendChild(e)}function h(aH,i){var D=F.getElementsByName(aH);var e=(i>0)?i:0;return(D.length>e)?D[e].content:""}function aF(){var aJ=F.getElementsByName("sudameta");var aR=[];for(var aO=0;aO<aJ.length;aO++){var aK=aJ[aO].content;if(aK){if(aK.indexOf(";")!=-1){var D=aK.split(";");for(var aH=0;aH<D.length;aH++){var aP=aw(D[aH]);if(!aP){continue}aR.push(aP)}}else{aR.push(aK)}}}var aM=F.getElementsByTagName("meta");for(var aO=0,aI=aM.length;aO<aI;aO++){var aN=aM[aO];if(aN.name=="tags"){aR.push("content_tags:"+encodeURI(aN.content))}}var aL=t("vjuids");aR.push("vjuids:"+aL);var e="";var aQ=j.indexOf("#");if(aQ!=-1){e=escape(j.substr(aQ+1));aR.push("hashtag:"+e)}return aR}function V(aK,D,aI,aH){if(aK==""){return""}aH=(aH=="")?"=":aH;D+=aH;var aJ=aK.indexOf(D);if(aJ<0){return""}aJ+=D.length;var i=aK.indexOf(aI,aJ);if(i<aJ){i=aK.length}return aK.substring(aJ,i)}function t(e){if(undefined==e||""==e){return""}return V(F.cookie,e,";","")}function at(aI,e,i,aH){if(e!=null){if((undefined==aH)||(null==aH)){aH="sina.com.cn"}if((undefined==i)||(null==i)||(""==i)){F.cookie=aI+"="+e+";domain="+aH+";path=/"}else{var D=new Date();var aJ=D.getTime();aJ=aJ+86400000*i;D.setTime(aJ);aJ=D.getTime();F.cookie=aI+"="+e+";domain="+aH+";expires="+D.toUTCString()+";path=/"}}}function f(D){try{var i=document.getElementById("sudaDataFrame").contentWindow.storage;return i.get(D)}catch(aH){return false}}function ar(D,aH){try{var i=document.getElementById("sudaDataFrame").contentWindow.storage;i.set(D,aH);return true}catch(aI){return false}}function L(){var aJ=15;var D=window.SUDA.etag;if(!B){return"-"}if(u==0){O();q()}if(D&&D!=undefined){w=true}ls_gid=f(aa);if(ls_gid===false||w==false){return false}else{am=true}if(ls_gid&&ls_gid.length>aJ){at(aa,ls_gid,3650);n=true;return ls_gid}else{if(D&&D.length>aJ){at(aa,D,3650);az=true}var i=0,aI=500;var aH=setInterval((function(){var e=t(aa);if(w){e=D}i+=1;if(i>3){clearInterval(aH)}if(e.length>aJ){clearInterval(aH);ar(aa,e)}}),aI);return w?D:t(aa)}}function U(e,aH,D){var i=e;if(i==null){return false}aH=aH||"click";if((typeof D).toLowerCase()!="function"){return}if(i.attachEvent){i.attachEvent("on"+aH,D)}else{if(i.addEventListener){i.addEventListener(aH,D,false)}else{i["on"+aH]=D}}return true}function af(){if(window.event!=null){return window.event}else{if(window.event){return window.event}var D=arguments.callee.caller;var i;var aH=0;while(D!=null&&aH<40){i=D.arguments[0];if(i&&(i.constructor==Event||i.constructor==MouseEvent||i.constructor==KeyboardEvent)){return i}aH++;D=D.caller}return i}}function g(i){i=i||af();if(!i.target){i.target=i.srcElement;i.pageX=i.x;i.pageY=i.y}if(typeof i.layerX=="undefined"){i.layerX=i.offsetX}if(typeof i.layerY=="undefined"){i.layerY=i.offsetY}return i}function aw(aH){if(typeof aH!=="string"){throw"trim need a string as parameter"}var e=aH.length;var D=0;var i=/(\u3000|\s|\t|\u00A0)/;while(D<e){if(!i.test(aH.charAt(D))){break}D+=1}while(e>D){if(!i.test(aH.charAt(e-1))){break}e-=1}return aH.slice(D,e)}function c(e){return Object.prototype.toString.call(e)==="[object Array]"}function J(aH,aL){var aN=aw(aH).split("&");var aM={};var D=function(i){if(aL){try{return decodeURIComponent(i)}catch(aP){return i}}else{return i}};for(var aJ=0,aK=aN.length;aJ<aK;aJ++){if(aN[aJ]){var aI=aN[aJ].split("=");var e=aI[0];var aO=aI[1];if(aI.length<2){aO=e;e="$nullName"}if(!aM[e]){aM[e]=D(aO)}else{if(c(aM[e])!=true){aM[e]=[aM[e]]}aM[e].push(D(aO))}}}return aM}function ac(D,aI){for(var aH=0,e=D.length;aH<e;aH++){aI(D[aH],aH)}}function ak(i){var e=new RegExp("^http(?:s)?://([^/]+)","im");if(i.match(e)){return i.match(e)[1].toString()}else{return""}}function aj(aO){try{var aL="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/=";var D="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-_=";var aQ=function(e){var aR="",aS=0;for(;aS<e.length;aS++){aR+="%"+aH(e[aS])}return decodeURIComponent(aR)};var aH=function(e){var i="0"+e.toString(16);return i.length<=2?i:i.substr(1)};var aP=function(aY,aV,aR){if(typeof(aY)=="string"){aY=aY.split("")}var aX=function(a7,a9){for(var a8=0;a8<a7.length;a8++){if(a7[a8]==a9){return a8}}return -1};var aS=[];var a6,a4,a1="";var a5,a3,a0,aZ="";if(aY.length%4!=0){}var e=/[^A-Za-z0-9\+\/\=]/g;var a2=aL.split("");if(aV=="urlsafe"){e=/[^A-Za-z0-9\-_\=]/g;a2=D.split("")}var aU=0;if(aV=="binnary"){a2=[];for(aU=0;aU<=64;aU++){a2[aU]=aU+128}}if(aV!="binnary"&&e.exec(aY.join(""))){return aR=="array"?[]:""}aU=0;do{a5=aX(a2,aY[aU++]);a3=aX(a2,aY[aU++]);a0=aX(a2,aY[aU++]);aZ=aX(a2,aY[aU++]);a6=(a5<<2)|(a3>>4);a4=((a3&15)<<4)|(a0>>2);a1=((a0&3)<<6)|aZ;aS.push(a6);if(a0!=64&&a0!=-1){aS.push(a4)}if(aZ!=64&&aZ!=-1){aS.push(a1)}a6=a4=a1="";a5=a3=a0=aZ=""}while(aU<aY.length);if(aR=="array"){return aS}var aW="",aT=0;for(;aT<aS.lenth;aT++){aW+=String.fromCharCode(aS[aT])}return aW};var aI=[];var aN=aO.substr(0,3);var aK=aO.substr(3);switch(aN){case"v01":for(var aJ=0;aJ<aK.length;aJ+=2){aI.push(parseInt(aK.substr(aJ,2),16))}return decodeURIComponent(aQ(aP(aI,"binnary","array")));break;case"v02":aI=aP(aK,"urlsafe","array");return aQ(aP(aI,"binnary","array"));break;default:return decodeURIComponent(aO)}}catch(aM){return""}}var ap={screenSize:function(){return(m&8388608==8388608)?ao.width+"x"+ao.height:""},colorDepth:function(){return(m&4194304==4194304)?ao.colorDepth:""},appCode:function(){return(m&2097152==2097152)?s.appCodeName:""},appName:function(){return(m&1048576==1048576)?((s.appName.indexOf("Microsoft Internet Explorer")>-1)?"MSIE":s.appName):""},cpu:function(){return(m&524288==524288)?(s.cpuClass||s.oscpu):""},platform:function(){return(m&262144==262144)?(s.platform):""},jsVer:function(){if(m&131072!=131072){return""}var aI,e,aK,D=1,aH=0,i=(s.appName.indexOf("Microsoft Internet Explorer")>-1)?"MSIE":s.appName,aJ=s.appVersion;if("MSIE"==i){e="MSIE";aI=aJ.indexOf(e);if(aI>=0){aK=window.parseInt(aJ.substring(aI+5));if(3<=aK){D=1.1;if(4<=aK){D=1.3}}}}else{if(("Netscape"==i)||("Opera"==i)||("Mozilla"==i)){D=1.3;e="Netscape6";aI=aJ.indexOf(e);if(aI>=0){D=1.5}}}return D},network:function(){if(m&65536!=65536){return""}var i="";i=(s.connection&&s.connection.type)?s.connection.type:i;try{F.body.addBehavior("#default#clientCaps");i=F.body.connectionType}catch(D){i="unkown"}return i},language:function(){return(m&32768==32768)?(s.systemLanguage||s.language):""},timezone:function(){return(m&16384==16384)?(new Date().getTimezoneOffset()/60):""},flashVer:function(){if(m&8192!=8192){return""}var aK=s.plugins,aH,aL,aN;if(aK&&aK.length){for(var aJ in aK){aL=aK[aJ];if(aL.description==null){continue}if(aH!=null){break}aN=aL.description.toLowerCase();if(aN.indexOf("flash")!=-1){aH=aL.version?parseInt(aL.version):aN.match(/\d+/);continue}}}else{if(window.ActiveXObject){for(var aI=10;aI>=2;aI--){try{var D=new ActiveXObject("ShockwaveFlash.ShockwaveFlash."+aI);if(D){aH=aI;break}}catch(aM){}}}else{if(W.indexOf("webtv/2.5")!=-1){aH=3}else{if(W.indexOf("webtv")!=-1){aH=2}}}}return aH},javaEnabled:function(){if(m&4096!=4096){return""}var D=s.plugins,i=s.javaEnabled(),aH,aI;if(i==true){return 1}if(D&&D.length){for(var e in D){aH=D[e];if(aH.description==null){continue}if(i!=null){break}aI=aH.description.toLowerCase();if(aI.indexOf("java plug-in")!=-1){i=parseInt(aH.version);continue}}}else{if(window.ActiveXObject){i=(new ActiveXObject("JavaWebStart.IsInstalled")!=null)}}return i?1:0}};var ad={pageId:function(i){var D=i||r,aK="-9999-0-0-1";if((undefined==D)||(""==D)){try{var aH=h("publishid");if(""!=aH){var aJ=aH.split(",");if(aJ.length>0){if(aJ.length>=3){aK="-9999-0-"+aJ[1]+"-"+aJ[2]}D=aJ[0]}}else{D="0"}}catch(aI){D="0"}D=D+aK}return D},sessionCount:function(){var e=t("_s_upa");if(e==""){e=0}return e},excuteCount:function(){return SUDA.sudaCount},referrer:function(){if(m&2048!=2048){return""}var e=/^[^\?&#]*.swf([\?#])?/;if((aA=="")||(aA.match(e))){var i=V(j,"ref","&","");if(i!=""){return escape(i)}}return escape(aA)},isHomepage:function(){if(m&1024!=1024){return""}var D="";try{F.body.addBehavior("#default#homePage");D=F.body.isHomePage(j)?"Y":"N"}catch(i){D="unkown"}return D},PGLS:function(){return(m&512==512)?h("stencil"):""},ZT:function(){if(m&256!=256){return""}var e=h("subjectid");e.replace(",",".");e.replace(";",",");return escape(e)},mediaType:function(){return(m&128==128)?h("mediaid"):""},domCount:function(){return(m&64==64)?F.getElementsByTagName("*").length:""},iframeCount:function(){return(m&32==32)?F.getElementsByTagName("iframe").length:""}};var av={visitorId:function(){var i=15;var e=t(aa);if(e.length>i&&u==0){return e}else{return}},fvisitorId:function(e){if(!e){var e=t(Y);return e}else{at(Y,e,3650)}},sessionId:function(){var e=t(H);if(""==e){var i=new Date();e=Math.random()*10000000000000+"."+i.getTime()}return e},flashCookie:function(e){if(e){}else{return p}},lastVisit:function(){var D=t(H);var aI=t(P);var aH=aI.split(":");var aJ="",i;if(aH.length>=6){if(D!=aH[4]){i=new Date();var e=new Date(window.parseInt(aH[0]));aH[1]=window.parseInt(aH[1])+1;if(i.getMonth()!=e.getMonth()){aH[2]=1}else{aH[2]=window.parseInt(aH[2])+1}if(((i.getTime()-e.getTime())/86400000)>=7){aH[3]=1}else{if(i.getDay()<e.getDay()){aH[3]=1}else{aH[3]=window.parseInt(aH[3])+1}}aJ=aH[0]+":"+aH[1]+":"+aH[2]+":"+aH[3];aH[5]=aH[0];aH[0]=i.getTime();at(P,aH[0]+":"+aH[1]+":"+aH[2]+":"+aH[3]+":"+D+":"+aH[5],360)}else{aJ=aH[5]+":"+aH[1]+":"+aH[2]+":"+aH[3]}}else{i=new Date();aJ=":1:1:1";at(P,i.getTime()+aJ+":"+D+":",360)}return aJ},userNick:function(){if(al!=""){return al}var D=unescape(t(l));if(D!=""){var i=V(D,"ag","&","");var e=V(D,"user","&","");var aH=V(D,"uid","&","");var aJ=V(D,"sex","&","");var aI=V(D,"dob","&","");al=i+":"+e+":"+aH+":"+aJ+":"+aI;return al}else{return""}},userOrigin:function(){if(m&4!=4){return""}var e=t(aE);var i=e.split(":");if(i.length>=2){return i[0]}else{return""}},advCount:function(){return(m&2==2)?t(E):""},setUOR:function(){var aL=t(aE),aP="",i="",aO="",aI="",aM=j.toLowerCase(),D=F.referrer.toLowerCase();var aQ=/[&|?]c=spr(_[A-Za-z0-9]{1,}){3,}/;var aK=new Date();if(aM.match(aQ)){aO=aM.match(aQ)[0]}else{if(D.match(aQ)){aO=D.match(aQ)[0]}}if(aO!=""){aO=aO.substr(3)+":"+aK.getTime()}if(aL==""){if(t(P)==""){aP=ak(D);i=ak(aM)}at(aE,aP+","+i+","+aO,365)}else{var aJ=0,aN=aL.split(",");if(aN.length>=1){aP=aN[0]}if(aN.length>=2){i=aN[1]}if(aN.length>=3){aI=aN[2]}if(aO!=""){aJ=1}else{var aH=aI.split(":");if(aH.length>=2){var e=new Date(window.parseInt(aH[1]));if(e.getTime()<(aK.getTime()-86400000*30)){aJ=1}}}if(aJ){at(aE,aP+","+i+","+aO,365)}}},setAEC:function(e){if(""==e){return}var i=t(E);if(i.indexOf(e+",")<0){i=i+e+","}at(E,i,7)},ssoInfo:function(){var D=unescape(aj(t("sso_info")));if(D!=""){if(D.indexOf("uid=")!=-1){var i=V(D,"uid","&","");return escape("uid:"+i)}else{var e=V(D,"u","&","");return escape("u:"+unescape(e))}}else{return""}},subp:function(){return t("SUBP")}};var ai={CI:function(){var e=["sz:"+ap.screenSize(),"dp:"+ap.colorDepth(),"ac:"+ap.appCode(),"an:"+ap.appName(),"cpu:"+ap.cpu(),"pf:"+ap.platform(),"jv:"+ap.jsVer(),"ct:"+ap.network(),"lg:"+ap.language(),"tz:"+ap.timezone(),"fv:"+ap.flashVer(),"ja:"+ap.javaEnabled()];return"CI="+e.join("|")},PI:function(e){var i=["pid:"+ad.pageId(e),"st:"+ad.sessionCount(),"et:"+ad.excuteCount(),"ref:"+ad.referrer(),"hp:"+ad.isHomepage(),"PGLS:"+ad.PGLS(),"ZT:"+ad.ZT(),"MT:"+ad.mediaType(),"keys:","dom:"+ad.domCount(),"ifr:"+ad.iframeCount()];return"PI="+i.join("|")},UI:function(){var e=["vid:"+av.visitorId(),"sid:"+av.sessionId(),"lv:"+av.lastVisit(),"un:"+av.userNick(),"uo:"+av.userOrigin(),"ae:"+av.advCount(),"lu:"+av.fvisitorId(),"si:"+av.ssoInfo(),"rs:"+(n?1:0),"dm:"+(B?1:0),"su:"+av.subp()];return"UI="+e.join("|")},EX:function(i,e){if(m&1!=1){return""}i=(null!=i)?i||"":b;e=(null!=e)?e||"":a;return"EX=ex1:"+i+"|ex2:"+e},MT:function(){return"MT="+aF().join("|")},V:function(){return an},R:function(){return"gUid_"+new Date().getTime()}};function ax(){var aK="-",aH=F.referrer.toLowerCase(),D=j.toLowerCase();if(""==t(X)){if(""!=aH){aK=ak(aH)}at(X,aK,"","weibo.com")}var aI=/weibo.com\/reg.php/;if(D.match(aI)){var aJ=V(unescape(D),"sharehost","&","");var i=V(unescape(D),"appkey","&","");if(""!=aJ){at(X,aJ,"","weibo.com")}at("appkey",i,"","weibo.com")}}function d(e,i){G(e,i)}function G(i,D){D=D||{};var e=new Image(),aH;if(D&&D.callback&&typeof D.callback=="function"){e.onload=function(){clearTimeout(aH);aH=null;D.callback(true)}}SUDA.img=e;e.src=i;aH=setTimeout(function(){if(D&&D.callback&&typeof D.callback=="function"){D.callback(false);e.onload=null}},D.timeout||2000)}function x(e,aH,D,aI){SUDA.sudaCount++;if(!av.visitorId()&&!L()){if(u<3){u++;setTimeout(x,500);return}}var i=N+[ai.V(),ai.CI(),ai.PI(e),ai.UI(),ai.MT(),ai.EX(aH,D),ai.R()].join("&");G(i,aI)}function y(e,D,i){if(aG||A){return}if(SUDA.sudaCount!=0){return}x(e,D,i)}function ab(e,aH){if((""==e)||(undefined==e)){return}av.setAEC(e);if(0==aH){return}var D="AcTrack||"+t(aa)+"||"+t(H)+"||"+av.userNick()+"||"+e+"||";var i=ag+D+"&gUid_"+new Date().getTime();d(i)}function aq(aI,e,i,aJ){aJ=aJ||{};if(!i){i=""}else{i=escape(i)}var aH="UATrack||"+t(aa)+"||"+t(H)+"||"+av.userNick()+"||"+aI+"||"+e+"||"+ad.referrer()+"||"+i+"||"+(aJ.realUrl||"")+"||"+(aJ.ext||"");var D=ag+aH+"&gUid_"+new Date().getTime();d(D,aJ)}function aC(aK){var i=g(aK);var aI=i.target;var aH="",aL="",D="";var aJ;if(aI!=null&&aI.getAttribute&&(!aI.getAttribute("suda-uatrack")&&!aI.getAttribute("suda-actrack")&&!aI.getAttribute("suda-data"))){while(aI!=null&&aI.getAttribute&&(!!aI.getAttribute("suda-uatrack")||!!aI.getAttribute("suda-actrack")||!!aI.getAttribute("suda-data"))==false){if(aI==F.body){return}aI=aI.parentNode}}if(aI==null||aI.getAttribute==null){return}aH=aI.getAttribute("suda-actrack")||"";aL=aI.getAttribute("suda-uatrack")||aI.getAttribute("suda-data")||"";sudaUrls=aI.getAttribute("suda-urls")||"";if(aL){aJ=J(aL);if(aI.tagName.toLowerCase()=="a"){D=aI.href}opts={};opts.ext=(aJ.ext||"");aJ.key&&SUDA.uaTrack&&SUDA.uaTrack(aJ.key,aJ.value||aJ.key,D,opts)}if(aH){aJ=J(aH);aJ.key&&SUDA.acTrack&&SUDA.acTrack(aJ.key,aJ.value||aJ.key)}}if(window.SUDA&&Object.prototype.toString.call(window.SUDA)==="[object Array]"){for(var Q=0,ae=SUDA.length;Q<ae;Q++){switch(SUDA[Q][0]){case"setGatherType":m=SUDA[Q][1];break;case"setGatherInfo":r=SUDA[Q][1]||r;b=SUDA[Q][2]||b;a=SUDA[Q][3]||a;break;case"setPerformance":Z=SUDA[Q][1];break;case"setPerformanceFilter":C=SUDA[Q][1];break;case"setPerformanceInterval":K=SUDA[Q][1]*1||0;K=isNaN(K)?0:K;break;case"setGatherMore":M.push(SUDA[Q].slice(1));break;case"acTrack":S.push(SUDA[Q].slice(1));break;case"uaTrack":I.push(SUDA[Q].slice(1));break}}}aG=(function(D,i){if(ah.top==ah){return false}else{try{if(F.body.clientHeight==0){return false}return((F.body.clientHeight>=D)&&(F.body.clientWidth>=i))?false:true}catch(aH){return true}}})(320,240);A=(function(){return false})();av.setUOR();var au=av.sessionId();window.SUDA=window.SUDA||[];SUDA.sudaCount=SUDA.sudaCount||0;SUDA.log=function(){x.apply(null,arguments)};SUDA.acTrack=function(){ab.apply(null,arguments)};SUDA.uaTrack=function(){aq.apply(null,arguments)};U(F.body,"click",aC);window.GB_SUDA=SUDA;GB_SUDA._S_pSt=function(){};GB_SUDA._S_acTrack=function(){ab.apply(null,arguments)};GB_SUDA._S_uaTrack=function(){aq.apply(null,arguments)};window._S_pSt=function(){};window._S_acTrack=function(){ab.apply(null,arguments)};window._S_uaTrack=function(){aq.apply(null,arguments)};window._S_PID_="";if(!window.SUDA.disableClickstream){y()}try{k()}catch(T){}})();
//-->
</script> 
<noScript> 
<div style='position:absolute;top:0;left:0;width:0;height:0;visibility:hidden'><img width=0 height=0 src='http://beacon.sina.com.cn/a.gif?noScript' border='0' alt='' /></div> 
</noScript> 
<!-- SUDA_CODE_END -->

<!-- SSO_GETCOOKIE_START -->
<script type="text/javascript">var sinaSSOManager=sinaSSOManager||{};sinaSSOManager.getSinaCookie=function(){function dc(u){if(u==undefined){return""}var decoded=decodeURIComponent(u);return decoded=="null"?"":decoded}function ps(str){var arr=str.split("&");var arrtmp;var arrResult={};for(var i=0;i<arr.length;i++){arrtmp=arr[i].split("=");arrResult[arrtmp[0]]=dc(arrtmp[1])}return arrResult}function gC(name){var Res=eval("/"+name+"=([^;]+)/").exec(document.cookie);return Res==null?null:Res[1]}var sup=dc(gC("SUP"));if(!sup){sup=dc(gC("SUR"))}if(!sup){return null}return ps(sup)};</script>
<!-- SSO_GETCOOKIE_END -->

<script type="text/javascript">new function(r,s,t){this.a=function(n,t,e){if(window.addEventListener){n.addEventListener(t,e,false);}else if(window.attachEvent){n.attachEvent("on"+t,e);}};this.b=function(f){var t=this;return function(){return f.apply(t,arguments);};};this.c=function(){var f=document.getElementsByTagName("form");for(var i=0;i<f.length;i++){var o=f[i].action;if(this.r.test(o)){f[i].action=o.replace(this.r,this.s);}}};this.r=r;this.s=s;this.d=setInterval(this.b(this.c),t);this.a(window,"load",this.b(function(){this.c();clearInterval(this.d);}));}(/http:\/\/www\.google\.c(om|n)\/search/, "http://keyword.sina.com.cn/searchword.php", 250);</script>
<!-- body code end -->



<!--设为书签背景缓存-->
<div id="preload_bookmark"><div id="sprite"></div></div>
<!--设为书签背景缓存-->

<script>
jsLoader(ARTICLE_JSS.base,function(){
	SHM.register('news.head', function($) {
		var tab = $.app.tab;
		tab.init();
	});
	SHM.register('home.app.viewData',function(){
		return function(){
			var W=0, H=0, SL=0, ST=0, SW=0, SH=0;
			var w=window, d=document, dd=d.documentElement;
			W=dd.clientWidth||d.body.clientWidth;
			H=w.innerHeight||dd.clientHeight||d.body.clientHeight;
			ST=d.body.scrollTop||dd.scrollTop||w.pageYOffset;
			SL=d.body.scrollLeft||dd.scrollLeft||w.pageXOffset;
			SW=Math.max(d.body.scrollWidth, dd.scrollWidth ||0);
			SH=Math.max(d.body.scrollHeight,dd.scrollHeight||0, H);
			return {
				"scrollTop":ST,
				"scrollLeft":SL,
				"documentWidth":SW,
				"documentHeight":SH,
				"viewWidth":W,
				"viewHeight":H
			};
		}

	});

});

</script>

<!--  -->

	
<!-- ** first screen begin ** -->

<!-- 频道标准头 begin -->
<div class="channelHead">
	<div class="cheadTopbar" id="blk_cheadTopbar_01" data-sudaclick="newsstdhead">
		<div class="cheadTopbarLink">
			<a href="http://www.sina.com.cn/">新浪首页</a>&nbsp;&gt;&gt;
			<script charset="utf-8" src="//news.sina.com.cn/js/tophead/tgnews_data.js"></script>
		</div>
		<!-- 搜索css start -->
					<style type="text/css">
					.inp-txt-wrap{position: relative;}
					.top-suggest-wrap{top:21px; position: absolute;border: 1px solid #E1E1E1;background: #fff;width:148px;margin:0 0 0 1px;z-index:99999;filter:Alpha(Opacity=99); zoom:1; left: -1px;font-family: "Arial","SimSun","宋体";overflow: hidden;}
					.top-suggest-wrap .top-suggest-item,.top-suggest-wrap .top-suggest-tip,.top-suggest-wrap .top-suggest-more{height: 26px;line-height: 26px;padding-left: 14px;overflow: hidden;}
					.top-suggest-wrap .top-suggest-item{cursor: pointer;}
					.top-suggest-wrap .top-suggest-mover{background-color: #ddd;color: #000;}
					.top-suggest-wrap .top-suggest-tip{color: #000;line-height: 30px;height: 30px;border-bottom: 1px dashed #eee;}
					.top-suggest-wrap .top-suggest-more{font-size: 12px;border-top: 1px dashed #eee;height: 30px;line-height: 30px;}
					.top-suggest-more a{display: inline;line-height: 30px;}
					/*.top-suggest-more a:link, .top-suggest-more a:visited{color: #000;}
					.top-suggest-more a:hover, .top-suggest-more a:active, .top-suggest-more a:focus{color: #ff8400}*/
					.top-suggest-more .top-suggest-hotAll{float: left;margin-left: 0px;}
					.top-suggest-more .top-suggest-toHomePage{float:right;margin-right: 10px;}
					</style>
					<!-- 搜索css end -->

		<div class="cheadSearch">
			<form name="cheadSearchForm" method="get" onsubmit="return formSubmit();" action="//search.sina.com.cn/" target="_blank">
				<input type="text" name="q" class="cheadSeaKey" value="请输入关键词" onfocus="if(this.value=='请输入关键词'){this.value='';}" onblur="if(this.value==''){this.value='请输入关键词';}"/>
				<select name="c" id="slt_01" class="cheadSeaType">
					<option value="news" selected>新闻</option>
					<option value="img">图片</option>
					<option value="blog">博客</option>
					<option value="video">视频</option>
				</select>
				<input type="hidden" name="from" value="channel"/>
				<input type="hidden" name="ie" value="utf-8"/>
				<input style="margin-right:10px;" type="submit" class="cheadSeaSmt" value="搜索"/>
				<div class="new_version" style="float:right; width:84px; height:22px;background:url('http://n.sinaimg.cn/news/643213b9/20171127/bg.png') 0 0 no-repeat; color:#fff; text-align:center; line-height:22px; cursor:pointer; display:none; ">
                    体验新版首页
                </div>
			</form>
		</div>
		<style>
			.tn-user-greet{display:none;}
			.tn-title-login-custom{width:70px;}
			.cheadSearch form{float:right;}
			.cheadSearch{width:auto;}
		</style>
		
		

		<!-- 搜索js start -->
					<script charset="gb2312" src="//ent.sina.com.cn/470/2014/0328/search_suggest.js"></script>

					<script type="text/javascript">
					(function(){
							// 表单
							var frm = document.cheadSearchForm;
							// 下拉选择
							var select = frm.c;
							// 输入框
							var input = frm.q;
							// 提交按钮
							var submit = function(){
								frm.submit();
							};
							// 是否新闻
							var isNews = function(){
								return select.value==='news';
							};
							// 提交
							new searchsUggest({
						        input : input,
						        maxLen : 10,
						        placeholderStr:'请输入关键词',
						        showHotList:isNews,
						        showSuggestList:isNews,
								onSelect: submit
						    });
					})();
					</script>
					<!-- 搜索js end -->

		<script type="text/javascript">

      function trim_str(str) {
        return str.replace(/(^[\s\u3000]*)|([\s\u3000]*$)/g, "");
      }
      function formSubmit() {
        var form = document.cheadSearchForm;
        var input = form.q;
        var val = input.value;
        if (val === '请输入关键词' || trim_str(val) === "") {
          input.value = "";
          input.className = 'cheadSeaKey cheadSeaKeyClick';
          var temp_time_handler = setTimeout(function(){input.className='cheadSeaKey';clearTimeout(temp_time_handler)},500);
          input.focus();
          return false;
        } else if (form.c.value === 'video') {        
          window.open('//search.sina.com.cn/?c=video&range=title&q=' + val);
          return false;    
        }
        return true;
      }

			jsLoader(ARTICLE_JSS.common,function(){
				var searchType1 = new DivSelect('slt_01');
			})

		</script>
		<div class="cheadUserInfo" id="userLogin">
		</div>
	</div>
</div>

<!-- 频道标准头 end -->
<!-- top end -->


	
<script>
jsLoader(ARTICLE_JSS.ssologin).jsLoader(ARTICLE_JSS.user_panel, function(){

	var userPanel = window.SINA_USER_PANEL;
	var $ = userPanel.STK;

	if(userPanel){
		$.Ready(function(){

			/* 配置用户面板的额外文件
			 * set方法可级联设置，也可以单独设置，最后调用init()方法即可
			 userPanel.set('extra',{
			 css: '',	//额外样式文件，可选
			 outlogin: '',	//登录浮层JS，可选
			 weibo: ''	//读取微博信息接口，可选
			 })
			 */
			userPanel.set('outloginLayer', {//配置登录浮层相关内容
				ready : function(){//登录浮层渲染成功后执行的方法，必选
					var loginLayer = window.SINA_OUTLOGIN_LAYER;//获取登录浮层
					if(loginLayer){
						loginLayer.set('extra',{
							css: '//i.sso.sina.com.cn/css/outlogin/v1/outlogin_skin_finance.css'
						});
						//配置登录选项，并初始化登录浮层
						//登录浮层具体参数说明请参考登录浮层文档
						loginLayer.set('sso', {
							entry : 'news'
						}).set('styles',{
							'z-index': '99999'
						}).init();

					}
				},
				triggerEvent: 'hover'//触发显示登录浮层的事件，可选择hover或click

//					setPos: true
			}).set('container',{//设置用户面板的父节点，不设置则为body
				node: $.E("userLogin")
			}).register('plugin_ready',function(){
				//注册用户面板初始化完成后触发事件，可选

				//console.log("plugin_ready");
			}).init();// 初始化用户面板，必选
		});
	}

})

</script>

<style>
/* 修正登录名高度问题 */
.tn-title-login-custom .tn-tab-custom{padding:10px 0 !important; height:21px !important; line-height:21px !important; }
	.tn-title-login-custom .tn-topmenulist-custom{right:-17px !important;}
</style>

	
<!-- 背景广告 begin -->
<style type="text/css">
    #bgLeftAd, #bgRightAd {
        overflow: hidden;
    }
</style>
<div id="bgAdWrap"></div>
<ins class="sinaads" data-ad-pdps="D5F1BC2DF4C2"></ins>
<script>
    (sinaads = window.sinaads || []).push({
        params: {
            "sinaads_ad_width": 1600,
            "sinaads_bg_top": 45,
            "sinaads_bg_asideClick": 1//0是顶部可点击，1是全部可点击
        }
    });
</script>
<!-- 背景广告 end -->

<div class="wrap" id="wrap">

<a href="#jump0" class="JumpTo"><img src="http://i0.sinaimg.cn/cha/images/c.gif" width="1" height="1" alt="跳过导航栏" /></a>

<!-- 频道导航 begin -->

<!--X07start07X-->
<!--XAD_STARTX-->
<div class="main-nav" data-sudaclick="blk_mainnav">
	<div class="nav-mod-1">
                <ul>
                    <li><a href="http://news.sina.com.cn/" target="_blank"><b>新闻</b></a></li>
					<li><a href="http://mil.news.sina.com.cn/" target="_blank">军事</a></li>
                    <li><a href="http://news.sina.com.cn/society/" target="_blank">社会</a></li>
                    <li><a href="http://news.sina.com.cn/world/" target="_blank">国际</a></li>
                </ul>
                <ul>
                    <li><a href="http://finance.sina.com.cn/" target="_blank"><b>财经</b></a></li>
                    <li><a href="http://finance.sina.com.cn/stock/" target="_blank">股票</a></li>
                    <li><a href="http://finance.sina.com.cn/fund/" target="_blank">基金</a></li>
                    <li><a href="http://finance.sina.com.cn/forex/" target="_blank">外汇</a></li>
                </ul>
                <ul>
                    <li><a href="http://tech.sina.com.cn/" target="_blank"><b>科技</b></a></li>
                    <li><a href="http://mobile.sina.com.cn/" target="_blank">手机</a></li>
                    <li><a href="http://tech.sina.com.cn/discovery/" target="_blank">探索</a></li>
                    <li><a href="http://zhongce.sina.com.cn/" target="_blank">众测</a></li>
                </ul>
            </div>
            <div class="nav-mod-1 nav-w">
                <ul>
					<li><a href="http://sports.sina.com.cn/" target="_blank"><b>体育</b></a></li>
					<li style="width:36px;"><a href="http://sports.sina.com.cn/nba/" target="_blank">NBA</a></li>
					<li><a href="http://sports.sina.com.cn/g/premierleague/" target="_blank">英超</a></li>
                    <li><a href="http://sports.sina.com.cn/csl/" target="_blank">中超</a></li>

                    
                </ul>
                <ul>
                    <li><a href="http://ent.sina.com.cn/" target="_blank"><b>娱乐</b></a></li>
                    <li style="width:36px;"><a href="http://ent.sina.com.cn/star/" target="_blank">明星</a></li>
                    <li><a href="http://ent.sina.com.cn/film/" target="_blank">电影</a></li>
                    <li><a href="http://astro.sina.com.cn/" target="_blank">星座</a></li>
                </ul>
                <ul>
                    <li><a href="http://auto.sina.com.cn/" target="_blank"><b>汽车</b></a></li>
                    <li style="width:36px;"><a href="http://dealer.auto.sina.com.cn/price/" target="_blank">报价</a></li>
                    <li><a href="http://db.auto.sina.com.cn/" target="_blank">买车</a></li>
                    <li><a href="http://auto.sina.com.cn/newcar/index.d.html" target="_blank">新车</a></li>
                </ul>
            </div>
            <div class="nav-mod-1 nav-w">
                <ul>
                    <li><a href="http://blog.sina.com.cn/" target="_blank"><b>博客</b></a></li>
                    <li style="width:36px;"><a href="http://zhuanlan.sina.com.cn/" target="_blank">专栏</a></li>
                    <li><a href="http://blog.sina.com.cn/lm/history" target="_blank">历史</a></li>
                    <li><a href="http://weather.sina.com.cn/" target="_blank">天气</a></li>
                </ul>
                <ul>
                    <li><a href="http://video.sina.com.cn/" target="_blank"><b>视频</b></a></li>
                    <li style="width:36px;"><a href="http://ent.sina.com.cn/zongyi/" target="_blank">综艺</a></li>
                    <li><a href="http://vr.sina.com.cn/" target="_blank">VR</a></li>
                    <li><a href="http://video.sina.com.cn/l/pub" target="_blank">直播</a></li>
                </ul>
                <ul>
					<li><a href="http://www.leju.com/#source=pc_sina_tydh1&source_ext=pc_sina" target="_blank"><b>房产</b></a></li>
                    <li style="width:36px;"><a href="http://esf.leju.com/?bi=tg&type=sina-pc&pos=index-dh" target="_blank">二手房</a></li>
                    <li><a href="http://jiaju.sina.com.cn/" target="_blank">家居</a></li>
                    <li><a href="http://collection.sina.com.cn/" target="_blank">收藏</a></li>
                </ul>
            </div>
            <div class="nav-mod-1">
                <ul>
                    <li><a href="http://fashion.sina.com.cn/" target="_blank"><b>时尚</b></a></li>
                    <li><a href="http://eladies.sina.com.cn/" target="_blank">女性</a></li>
                    <li><a href="http://health.sina.com.cn/" target="_blank">健康</a></li>
                    <li><a href="http://baby.sina.com.cn/" target="_blank">育儿</a></li>
                </ul>
                <ul>
                    <li><a href="http://edu.sina.com.cn/" target="_blank"><b>教育</b></a></li>
					<li><a href="http://edu.sina.com.cn/gaokao" target="_blank">高考</a></li>
                    <li><a href="http://gongyi.sina.com.cn/" target="_blank">公益</a></li>
                    <li><a href="http://fo.sina.com.cn/" target="_blank">佛学</a></li>
                </ul>
                <ul>
                    <li><a href="http://photo.sina.com.cn/" target="_blank"><b>图片</b></a></li>
                    <li><a href="http://book.sina.com.cn/" target="_blank">读书</a></li>
                    <li><a href="http://tousu.sina.com.cn/" target="_blank">投诉</a></li>
                    <li><a href="http://sifa.sina.com.cn/" target="_blank">司法</a></li>
                </ul>
            </div>
            <div class="nav-mod-1 nav-mod-s">
                <ul>
                    <li><a href="https://weibo.com/" target="_blank"><b>微博</b></a></li>
                    <li><a href="http://city.sina.com.cn/" target="_blank">城市</a></li>
                    <li><a href="http://www.51xiancheng.com/" target="_blank">鲜城</a></li>
                    <li id="SI_Nav_City"><a href="http://sh.sina.com.cn/" target="_blank">上海</a></li>
                </ul>
                <ul>
                    <li><a href="http://travel.sina.com.cn/" target="_blank"><b>旅游</b></a></li>
                    <li><a href="http://cul.news.sina.com.cn/" target="_blank">文化</a></li>
                    <li><a href="http://lottery.sina.com.cn/" target="_blank">彩票</a></li>
                    <li><a href="http://golf.sina.com.cn/" target="_blank">高尔夫</a></li>
                </ul>
                <ul>
                    <li><a href="http://games.sina.com.cn/" target="_blank"><b>游戏</b></a></li>
                    <li><a href="http://www.97973.com" target="_blank">手游</a></li>
                    <li><a href="http://mail.sina.com.cn/" target="_blank">邮箱</a></li>
                    <li><a href="http://english.sina.com/" target="_blank">English</a></li>
                </ul>
            </div>
            <div class="nav-mod-1 nav-w nav-hasmore">
                <ul class="nav-out">
                    <li><a href="http://jiaoyi.sina.com.cn/jy/" target="_blank">交易</a></li>
                    <li><a href="https://trade.xincai.com/web/promote" target="_blank">理财</a></li>
                    <li class="more">
                        <a href="javascript:;">更多<i></i></a>
                        <ul class="more-list">
							<li><a href="http://gov.sina.com.cn/" target="_blank">政务</a></li>
                            <li><a href="http://chexian.sina.com/" target="_blank">车险</a></li>
                            <li><a href="http://game.weibo.com/" target="_blank">页游</a></li>
                           <li><a id="navLinkShow" href="http://show.sina.com.cn/" target="_blank">SHOW</a></li>
                            <li><a href="http://search.sina.com.cn/?c=more" target="_blank">搜索</a></li>
                            <li><a href="http://help.sina.com.cn/" target="_blank">客服</a></li>
                            <li><a href="http://news.sina.com.cn/guide/" target="_blank">导航</a></li>
                        </ul>
                    </li>
                </ul>
            </div></div>
<!--XAD_ENDX-->
<!--X07end07X-->
<!-- 频道导航 end -->

<a name="jump0"></a>

<!-- QP begin -->
<!--XAD_STARTX-->
<!--_SINA_ADS_BEGIN_-->
<div style="margin-top:0px;text-align:center;">
<!--全屏开始 勿动-->
<script type="text/javascript">document.write('<span id="FullScreenWrap"></span>');</script>
<!--全屏结束 勿动-->
</div>
<!--_SINA_ADS_END_-->
<!--XAD_ENDX-->	
<!-- QP end -->

<!--XAD_STARTX-->
<!--_SINA_ADS_BEGIN_-->
<!-- 背景广告 begin -->

<!-- 背景广告 end -->

<!--_SINA_ADS_END_-->
<!--XAD_ENDX-->

<!--XAD_STARTX-->
<!--_SINA_ADS_BEGIN_-->


<!-- 1000x90顶通 begin -->
<script>
//设置本页面的富媒体类型的顺序
 
var _SINAADS_CONF_PAGE_MEDIA_ORDER = ["PDPS000000059668", "PDPS000000047195", "PDPS000000047198", "PDPS000000056023,PDPS000000057465"];
 
//var sinaadsPageMediaOrder = ['stream', 'fullscreen', 'couplet', 'videoWindow/fuceng'];
</script>

	

<!--US_banner_468x95_start-->

<!-- 1000x90轮播顶部通栏广告 开始 -->
<div id="ad_47200"><script async charset="utf-8" src="//d5.sina.com.cn/litong/zhitou/sinaads/release/sinaads.js"></script><ins class="sinaads" data-ad-pdps="PDPS000000047200"></ins><script>(sinaads = window.sinaads || []).push({});</script></div>
<!-- 1000x90轮播顶部通栏广告 结束 -->
<!-- 1000x90顶通 end -->
	
<!--US_banner_468x95_end-->
	

<!--_SINA_ADS_END_-->
<!--XAD_ENDX-->


	
<!-- publish_helper name='新闻频道导航' p_id='1' t_id='908' d_id='2' -->
	<div class="cNav1" id="blk_cNav1_01" data-sudaclick="newsnav01">
        <div class="cNavLogo"><img src="http://i2.sinaimg.cn/dy/deco/2012/0613/yocc20120613img01/news_logo.png" alt="新浪新闻中心"></div>
        <div class="cNavLinks">
            <h4 suda-uatrack="key=news_index_new_topapp&value=1"><a href="http://m.sina.com.cn/m/sinahome.shtml" target="_blank">新浪新闻客户端</a></h4><a class="more_btn" href="javascript:;"></a>
            <div class="more_list">
            	<ul>
                	 <li suda-uatrack="key=news_index_new_topapp&value=2"><a class="app_01" href="http://finance.sina.com.cn/mobile/comfinanceweb.shtml" target="_blank">新浪财经客户端</a></li>
                  <li suda-uatrack="key=news_index_new_topapp&value=3"><a class="app_02" href="http://m.sina.com.cn/m/sinaent.shtml" target="_blank">新浪娱乐客户端</a></li>
                  <li suda-uatrack="key=news_index_new_topapp&value=4"><a class="app_03" href="http://m.sina.com.cn/m/sinasport.shtml" target="_blank">新浪体育客户端</a></li>
                  <li suda-uatrack="key=news_index_new_topapp&value=6"><a class="app_04" href="http://zhongce.sina.com.cn/about/app" target="_blank">新浪众测客户端</a></li>
                  <li class="last" suda-uatrack="key=news_index_new_topapp&value=5"><a class="app_05" href="http://m.sina.com.cn/m/sinaopencourse.shtml" target="_blank">新浪公开课</a></li>
                </ul>
            </div>
        </div>
        <div class="cNavLive">
        	    <style>
a.cNavLive1{ margin-left: 5px;}
.btn_addfav_w{ position: relative; display: inline-block; *top:-2px; width: 50px; padding-left: 18px; height: 21px; line-height: 21px; text-align: left; background: url(http://i3.sinaimg.cn/dy/sinatag/btn_addfav_news.png) left center no-repeat; _background: url(http://i0.sinaimg.cn/dy/sinatag/btn_addfav_news.gif) left center no-repeat; font-family: "Microsoft YaHei", "微软雅黑", "黑体";}
.btn_addfav_w a.btn_addfav, .btn_addfav_w a.btn_addfav:visited{ font-size: 12px; color: #656565; font-family: "宋体";}
.btn_addfav_w a.btn_addfav:hover{ color: #264791}
.btn_addfav_w span.addfav_key{ font-weight: bold; color: #0A75C7; padding-right: 5px;}
.addfav_pop{ position: absolute; display: none; visibility: hidden; top: 20px; left: -32px; z-index: 9995; width: 282px; height: 123px; overflow: hidden;}
.addfav_pop_bg0{ position: absolute; top: 0px; left: 0px; z-index: 9997; width: 282px; height: 123px; background: url(http://i2.sinaimg.cn/dy/sinatag/addfav_pop_bg.png) 0 0 no-repeat; _background:none; _filter:progid:DXImageTransform.Microsoft.AlphaImageLoader(src='http://i2.sinaimg.cn/dy/sinatag/addfav_pop_bg.png');}
.addfav_pop_nowin{ height: 80px;}
.addfav_pop_nowin .addfav_pop_bg0{ background: url(http://i0.sinaimg.cn/dy/sinatag/addfav_pop_nowin_bg.png) 0 0 no-repeat; _background:none; _filter:progid:DXImageTransform.Microsoft.AlphaImageLoader(src='http://i0.sinaimg.cn/dy/sinatag/addfav_pop_nowin_bg.png');}
.addfav_pop_nowin .addfav_pop_p1{ display: none;}
.addfav_pop a.addfav_close, .addfav_pop a.addfav_close:visited{ position: absolute; z-index: 9999; top: 18px; right: 12px; width: 10px; height: 10px; background: url(http://i1.sinaimg.cn/dy/sinatag/btns_addfav_spirite.png) -38px 1px no-repeat; transition: all ease 0.3s;overflow:hidden;}
.addfav_pop a.addfav_close:hover{ background-position: -54px 1px;}
.btn_addfav_w .addfav_pop_p0{ display: block; position: relative; z-index: 9998; padding: 20px 20px 0 20px; color: #101010; font-size: 14px; line-height: 22px;}
.btn_addfav_w .addfav_pop_p1{ display: block; zoom:1;position: relative; z-index: 9998; padding: 20px 20px 0 20px; color: #656565; font-size: 14px; line-height: 22px;}
.btn_addfav_w a.addfav_dl, .btn_addfav_w a.addfav_dl:visited{ display: inline-block; vertical-align: top; _vertical-align: 1px; margin-top: 1px; margin-left: 8px; width: 66px; height: 22px; overflow: hidden; text-indent: -99em; line-height: 22px; text-align: center; color: #fff; background: url(http://i1.sinaimg.cn/dy/sinatag/btns_addfav_spirite.png) 0px -15px no-repeat; transition: all ease 0.3s;}
.btn_addfav_w a.addfav_dl:hover{ background-position: 0 -43px;}

.pullDown{display:block;visibility:visible;animation-name:pullDown;-webkit-animation-name:pullDown;animation-duration:0.3s;-webkit-animation-duration:0.3s;animation-timing-function:ease-out;-webkit-animation-timing-function:ease-out;transform-origin:50% 0%;-ms-transform-origin:50% 0%;-webkit-transform-origin:50% 0%;}@keyframes pullDown{0%{transform:scaleY(0.1);}100%{transform:scaleY(1);}}@-webkit-keyframes pullDown{0%{-webkit-transform:scaleY(0.1);}100%{-webkit-transform:scaleY(1);}}
    </style>
    <span class="btn_addfav_w">
        <a href="javascript:" class="btn_addfav" suda-uatrack="key=index_addfav&value=addfav_click" id="btn_addfav">设为书签</a>
        <span class="addfav_pop" id="addfav_pop">
            <span class="addfav_pop_bg0"></span>
            <span class="addfav_pop_bg1"></span>
            <a class="addfav_close" id="addfav_close" title="关闭" href="javascript:"></a>
            <span class="addfav_pop_p0"><span class="addfav_key" id="addfav_key">Ctrl+D</span>将本页面保存为书签，全面了解最新资讯，方便快捷。</span>
            <span class="addfav_pop_p1" id="addfav_pop_p1">您也可下载桌面快捷方式。<a suda-uatrack="key=index_addfav&value=download_click" class="addfav_dl" id="addfav_dl" href="http://i3.sinaimg.cn/dy/home/desktop/news.exe">点击下载</a></span>
        </span>
    </span>
    <script charset="gb2312" src="//news.sina.com.cn/js/87/20140221/addfavorite.js"></script>
            <a href="http://sina.cn/?from=sinacom" target="_blank" class="cNavLive1">手机新浪网</a>
        </div>
    </div>
	

<style>
.cNav2 .cNavLinks a{width:43px;}
.ptn_51{width:62px;height:15px;background-position:-799px -150px;}
a:hover .ptn_51{background-position:-799px -175px;filter:Alpha(opacity=100);opacity:1;}
.cNavlinks2{width:62px !important;}
.cNavlinks2:hover{background:url(http://n.sinaimg.cn/default/d3f34f8d/20160427/news_navbanner03.png) no-repeat 0 -254px !important;}
.cNav2{padding-left: 9px;}
	
</style>

    <div class="cNav2" id="blk_cNav2_01">
    	<div class="cNavLinks" data-sudaclick="newsnav">
            <a href="http://news.sina.com.cn/roll/" style="margin-left:8px;"><span class="titName ptn_19">滚动</span></a>
            <a href="http://news.sina.com.cn/live/"><span class="titName ptn_17">直播</span></a>
            <a href="http://survey.news.sina.com.cn/"><span class="titName ptn_160">调查</span></a>
            <a href="http://news.sina.com.cn/hotnews/"><span class="titName ptn_18">排行</span></a>

          <span class="sp_v01"></span>

            <!-- <a href="http://news.sina.com.cn/"><span class="titName ptn_01">首页</span></a> -->
            <a href="http://news.sina.com.cn/china/"><span class="titName ptn_02">国内</span></a>
            <a href="http://news.sina.com.cn/world/"><span class="titName ptn_03">国际</span></a>
            <a href="http://news.sina.com.cn/society/"><span class="titName ptn_04">社会</span></a>
            <a href="http://mil.news.sina.com.cn/"><span class="titName ptn_05">军事</span></a>
            <a href="http://news.sina.com.cn/opinion/"><span class="titName ptn_15">评论</span></a>

          <span class="sp_v01"></span>
        
            <a href="http://news.sina.com.cn/gov/"><span class="titName ptn_08">政务</span></a>
			<style>
				.cNav2 .cNavLinks .ptn_50_wap:hover .ptn_50{
					    background:url(http://n.sinaimg.cn/news/643213b9/20171114/news_navbanner04_hover.png) no-repeat 0 0;
				}
				.cNav2 .cNavLinks .ptn_50{
					background:url(http://n.sinaimg.cn/news/643213b9/20171114/news_navbanner04_normal.png) 0 0 no-repeat
				}
				.cNav2 .cNavLinks .cNavlinks2:hover{
					background-color: #a41303 !important;
    background-image: none !important;
				}
				.cNav2 .cNavLinks .cNavlinks2:hover .ptn_51{
					    background:url(http://n.sinaimg.cn/news/project/heimao_hove.png?20180211) no-repeat 0 0;
					
				}
				.cNav2 .cNavLinks .ptn_51{
					background:url(http://n.sinaimg.cn/news/project/heimao.png?20180211) 0 0 no-repeat
				}
			</style>
			<a class="ptn_50_wap" href="http://cul.news.sina.com.cn/"><span class="titName ptn_50" style='margin-left: 3px;margin-top: 15px;'>文化</span></a>
			
			<a href="http://tousu.sina.com.cn/" class="cNavlinks2"><span class="titName ptn_51" style='margin-top: 15px;'>黑猫投诉</span></a>

			
            <a href="http://photo.sina.com.cn/"><span class="titName ptn_16" style='margin-right: 3px;'>图片</span></a>
            <a href="http://video.sina.com.cn/news/"><span class="titName ptn_14">视频</span></a>
            <!-- <a href="http://weather.sina.com.cn/"><span class="titName ptn_09">天气</span></a> -->

            <span class="sp_v01"></span>

            <a href="http://sports.sina.com.cn/"><span class="titName ptn_10">体育</span></a>
            <a href="http://ent.sina.com.cn/"><span class="titName ptn_11">娱乐</span></a>
            <a href="http://finance.sina.com.cn/"><span class="titName ptn_12">财经</span></a>
            <a href="http://tech.sina.com.cn/"><span class="titName ptn_13">科技</span></a>
            <a href="http://news.sina.com.cn/zt/"><span class="titName ptn_20">专题</span></a>
        </div>

   </div>
	
	


    <script>
    	jsLoader(ARTICLE_JSS.jq,function(){
			(function($){
				$(function(){
					var $moreBtn = $('.cNav1 .more_btn');
					var $moreList = $('.cNav1 .more_list')
					$moreBtn.mouseover(function(){
						$moreList.show()
					})
					$moreBtn.mouseout(function(){
						$moreList.hide()	
					})
					$moreList.mouseover(function(){
						$moreList.show()
					})
					$moreList.mouseout(function(){
						$moreList.hide()
					})
				})
				
			})(jQuery)
		})
    </script>
	
    <div class="part_01 clearfix">
    	<div class="p_left">

<!-- 抓站_焦点图 begin -->
<!--t id="news_web_get_gspsdata" pid="1" tid="912" did="1" fid="sp_f28349"-->

<div class="blk_01" tab-type="tab-wrap" action-type="auto_focus">
<div class="blk_tit mb_10" style="/*height:76px;*/">
	
<style>
	/*
.clearfix:after{display: block;clear: both;content: '';}
.clearfix{zoom:1;}
.pic{display:block;position:absolute;top:0;left:0;}
.blk_01 .blk_main li{height:240px !important;position:relative;overflow:hidden;}
.blk_01 .blk_main .text{position:absolute;bottom:0;left:0;background:url(http://n.sinaimg.cn/a15ac274/20150921/opa.png);width:100%;}
	*/
</style>

<!--
        <div style="height:38px;border-bottom:1px solid #ccc;">
			<a href="" target="_blank"><img src="" width="100%"></a>
        </div>
-->
	
	<ol id="Blk01_Focus_Nav">
		<li tab-type="tab-nav" class="selected"><a href="http://photo.sina.com.cn/" target="_blank">热点</a></li><li tab-type="tab-nav" class=""><a href="http://photo.sina.com.cn/" target="_blank">聚焦</a></li><li tab-type="tab-nav" class=""><a href="http://photo.sina.com.cn/" target="_blank">天下</a></li><li tab-type="tab-nav" class=""><a href="http://photo.sina.com.cn/" target="_blank">现场</a></li><li tab-type="tab-nav" class="last"><a href="http://photo.sina.com.cn/" target="_blank">军事</a></li>	</ol>
</div>

<div class="blk_main" data-sudaclick="focuspic" action-type="auto_focus_cont"><div id="Blk01_Focus_Arr"><a class="scrArrAbsLeft" href="javascript:void(0)"></a>
<a class="scrArrAbsRight" href="javascript:void(0)"></a></div>

		<ul id="Blk01_Focus_Cont">
			<li style="" tab-type="tab-cont" suda-uatrack="key=news_index_new_focuspic&value=1">
<a href="http://slide.news.sina.com.cn/s/slide_1_2841_280603.html" target="_blank" class="pic"><img  width="338" height="238" src="http://n.sinaimg.cn/news/579/w340h239/20180604/N5XK-hcmurvh3020126.jpg" /></a>
<div class="text"><a href="http://slide.news.sina.com.cn/s/slide_1_2841_280603.html" target="_blank">云南陨石坠落房屋被击穿 村民纷纷寻宝</a></div>
</li><li style="display:none;" tab-type="tab-cont" suda-uatrack="key=news_index_new_focuspic&value=2">
<a href="http://slide.news.sina.com.cn/s/slide_1_2841_280558.html" target="_blank" class="pic"><img  width="338" height="238" src="http://n.sinaimg.cn/news/579/w340h239/20180604/G0by-hcmurvh2865648.jpg" /></a>
<div class="text"><a href="http://slide.news.sina.com.cn/s/slide_1_2841_280558.html" target="_blank">陪读夫妻毛坦厂中学门口卖盒饭6年 年入10万</a></div>
</li><li style="display:none;" tab-type="tab-cont" suda-uatrack="key=news_index_new_focuspic&value=3">
<a href="http://slide.news.sina.com.cn/w/slide_1_2841_280667.html" target="_blank" class="pic"><img  width="338" height="238" src="http://n.sinaimg.cn/news/579/w340h239/20180604/yKqJ-hcmurvh3471382.jpg" /></a>
<div class="text"><a href="http://slide.news.sina.com.cn/w/slide_1_2841_280667.html" target="_blank">危地马拉少女偷渡 被美国边防警察射杀</a></div>
</li><li style="display:none;" tab-type="tab-cont" suda-uatrack="key=news_index_new_focuspic&value=4">
<a href="http://slide.news.sina.com.cn/s/slide_1_2841_280548.html" target="_blank" class="pic"><img  width="338" height="238" src="http://n.sinaimg.cn/news/579/w340h239/20180604/QQj7-hcmurvh3056359.jpg" /></a>
<div class="text"><a href="http://slide.news.sina.com.cn/s/slide_1_2841_280548.html" target="_blank">浙江警方摧毁特大套路贷团伙 8辆大客运嫌犯</a></div>
</li><li style="display:none;" tab-type="tab-cont" suda-uatrack="key=news_index_new_focuspic&value=5">
<a href="http://slide.mil.news.sina.com.cn/k/slide_8_62085_64176.html" target="_blank" class="pic"><img  width="338" height="238" src="http://n.sinaimg.cn/mil/transform/579/w340h239/20180602/4XEb-hcikcew5457437.jpg" /></a>
<div class="text"><a href="http://slide.mil.news.sina.com.cn/k/slide_8_62085_64176.html" target="_blank">出鞘：中国为何至今仍需发展新一代核武器</a></div>
</li>		</ul>
</div>
</div>

<!-- 抓站_焦点图 end -->

            <script type="text/javascript">
                jsLoader(ARTICLE_JSS.base, function(){
                    var byId = SHM.dom.byId,
                        addEvent = SHM.evt.addEvent,
                        contains = SHM.dom.contains,
                        fixEvent = SHM.evt.fixEvent,
                        delegatedEvent = SHM.evt.delegatedEvent,
                        switchByEle = SHM.app.tab.switchByEle,
                        BODY = document.getElementsByTagName('BODY')[0],
                        delegatedBODY = delegatedEvent(BODY),
                        delegatedWrapType = 'auto_focus',
                        delegatedContType = 'auto_focus_cont',
                        nav = byId('Blk01_Focus_Nav').getElementsByTagName('LI'),
                        arrWrap = byId('Blk01_Focus_Arr'),
                        arrLeft = arrWrap.getElementsByTagName('A')[0],
                        arrRight = arrWrap.getElementsByTagName('A')[1],
                        cont = byId('Blk01_Focus_Cont').getElementsByTagName('LI');

                    var index, focusTimeHandler, len = cont.length;
                    var getCurIndex = function() {
                        for(var i = 0, l = nav.length; i < l; i++) {
                            if (nav[i].className.indexOf('selected') !=-1) {
                                return i;
                            }
                        }
                    }
                    var move = function(flag) {
                        index = getCurIndex();
                        if (!flag) {
                            index++;
                            if (index > (len - 1)) {index = 0}
                        } else {
                            index--;
                            if (index < 0) {index = len - 1}
                        }
                        switchByEle(cont[index]);
                    }
                    var autoTabStart = function() {
                        focusTimeHandler = setInterval(function(){
                            move(false);
                        },3000);
                    }
                    var autoTabStop = function() {
                        clearInterval(focusTimeHandler);
                    }
                    var showORHidden = function(flag) {
                        var tempTimeHandler = setTimeout(function(){
                            flag ? arrWrap.style.display = 'block' : arrWrap.style.display = 'none';
                            clearTimeout(tempTimeHandler);
                        },0);
                    }
                    var init = function() {
                        autoTabStart();
                        showORHidden(false);
                        delegatedBODY.add(delegatedWrapType,'mouseover',function(e){
                            autoTabStop();
                        });
                        delegatedBODY.add(delegatedWrapType,'mouseout',function(e){
                            autoTabStart();
                        });
                        delegatedBODY.add(delegatedContType,'mouseover',function(e){
                            showORHidden(true);
                        });
                        delegatedBODY.add(delegatedContType,'mouseout',function(e){
                            showORHidden(false);
                        });
                        addEvent(arrLeft,'mousedown',function(){
                            move(true);
                        });
                        addEvent(arrRight,'mousedown',function(){
                            move(false);
                        });
                    }
                    init();
                });
            </script>


            <div class="blk_02">
            	<div class="blk_tit vd_show_tit">
                    <ol>
                        <li class="selected"><a href="http://video.sina.com.cn/news/" target="_blank">新闻放映厅</a></li>
                    </ol>
                    <div class="tit_more"><a href="http://video.sina.com.cn/news/" target="_blank">更多</a></div>
                </div>
                <ul class="vd_show">
                	<li data-sudaclick="blk_zxt">
                    	<div class="pic_info clearfix">
                        <div class="l_pic"><a class="zt_pic_w" href="http://news.sina.com.cn/zxt/#258534302" target="_blank"><img src="http://n.sinaimg.cn/video/588/w372h216/20180602/7wiq-hcikcew7015292.gif" width="160" height="90"><span class="zt_txt"><s class="play_icon"></s></span></a></div>
                        	<div class="r_txt">
                            	<h3 class="show_tit"><a href="http://news.sina.com.cn/zxt/#258534302" target="_blank">新浪资讯台</a></h3>

                            	<p class="thumb_active"><a href="http://news.sina.com.cn/zxt/#258534302" target="_blank">罕见！20米长蓝鲸首度现身红海</a></p>
                            </div>
                        </div>
                    </li>
<li data-sudaclick="blk_jqs">
	<div class="pic_info clearfix">
		<div class="l_pic"><a class="zt_pic_w" href="http://video.sina.com.cn/p/mil/doc/2018-05-04/092268229690.html" target="_blank"><img src="http://n.sinaimg.cn/news/transform/250/w160h90/20180412/9JE4-fyzeyqc2624630.jpg" width="160" height="90"><span class="zt_txt"><s class="play_icon"></s></span></a></div>
		<div class="r_txt">
			<h3 class="show_tit"><a href="http://video.sina.com.cn/p/mil/doc/2018-05-04/092268229690.html" target="_blank">军事视频</a></h3>
			<p class="thumb_active"><a href="http://video.sina.com.cn/p/mil/doc/2018-05-04/092268229690.html" target="_blank">解放军南海大阅兵一镜到底 48艘战舰铁流澎湃</a></p>
		</div>
	</div>
</li>
                	<li data-sudaclick="blk_gtx">
                    	<div class="pic_info clearfix">
                        <div class="l_pic"><a class="zt_pic_w" href="http://video.sina.com.cn/news/spj/topvideoes20180603/#258570298" target="_blank"><img src="http://n.sinaimg.cn/news/transform/250/w160h90/20180603/Qr2z-hcmurvf7754238.png" width="160" height="90"><span class="zt_txt"><s class="play_icon"></s></span></a></div>
                        	<div class="r_txt">
                            	<h3 class="show_tit"><a href="http://news.sina.com.cn/voice/" target="_blank">嘘！你听</a></h3>
                            	<p class="thumb_active"><a href="http://video.sina.com.cn/news/spj/topvideoes20180603/#258570298" target="_blank">小伙球场打篮球 被广场舞大妈抓成大花脸</a></p>
                            </div>
                        </div>
                    </li>
				</ul>
            </div>

            <div class="blk_03">
            	<div class="blk_tit mb_10">
                    <ol>
                		<li class="selected "><a href="http://photo.sina.com.cn/" target="_blank">新闻图片</a></li>
                	</ol>
                    <div class="tit_more"><a href="http://photo.sina.com.cn/" target="_blank">更多</a></div>
                </div>
                <div class="blk_main clearfix" data-sudaclick="topnewspic">
                	<ul>
<li><a  class="zt_pic_w" href="http://slide.news.sina.com.cn/c/slide_1_2841_280685.html" target="_blank"><img  src="http://n.sinaimg.cn/news/transform/250/w160h90/20180604/G9aV-hcmurvh3786637.jpg" /><span class="zt_txt">县城高中举行高考壮行仪式</span></a></li><li><a  class="zt_pic_w" href="http://slide.news.sina.com.cn/c/slide_1_2841_280602.html" target="_blank"><img  src="http://n.sinaimg.cn/news/transform/250/w160h90/20180604/chMO-hcmurvh3793503.jpg" /><span class="zt_txt">峰会临近 青岛之夜成网红</span></a></li><li><a  class="zt_pic_w" href="http://slide.news.sina.com.cn/w/slide_1_86058_280538.html#p=1" target="_blank"><img  src="http://n.sinaimg.cn/news/transform/250/w160h90/20180604/613T-hcmurvh3933243.jpg" /><span class="zt_txt">英国纪念伦敦恐袭事件一周年</span></a></li><li><a  class="zt_pic_w" href="http://slide.news.sina.com.cn/slide_1_86058_280376.html" target="_blank"><img  src="http://n.sinaimg.cn/news/transform/250/w160h90/20180604/yPKO-hcmurvh3952033.jpg" /><span class="zt_txt">中式古典美衣鉴赏会现场</span></a></li>
                    </ul>
                </div>

            </div>
        </div>
  		<div class="p_middle">
          <!-- middle begin -->
          <!-- 要闻 begin -->
            <!-- wapnewstop browser begin 勿删 -->			

<!--t id="news_web_index_v2015_headline_gsps"-->
			<!-- 要闻 begin -->
<!-- wapnewstop browser begin 勿删 -->
            <!-- 1 -->
            <div class="blk_04" id="blk_yw_01" data-client="important" style="">
              <!-- wap_sina_news_yaowen begin 勿删 -->
<!-- 抓站_要闻 begin -->
<div class="b_tit">
  <div class="b_tname">要闻</div>
  <div class="b_time">北京时间：2018.6.4 周一</div>
</div>

<!-- 新闻中心要闻区 begin -->
<!--重点新闻1号位 开始-->

<div class="ct_t_01" id="syncad_1" data-sudaclick="yaowen" style="padding-bottom: 3px;overflow: hidden;">

<h1 data-client="headline"><a target="_blank" href="http://news.sina.com.cn/c/xl/2018-06-03/doc-ihcmurvf7992548.shtml">习近平为何把这个区域组织称为“典范”</a></h1>

<h1 data-client="headline"><a target="_blank" href="http://news.sina.com.cn/o/2018-06-04/doc-ihcmurvh6404104.shtml">刘鹤是否赴美继续推进经贸磋商？中方回应</a></h1>

<h1 data-client="headline"><a target="_blank" href="http://news.sina.com.cn/c/zj/2018-06-04/doc-ihcmurvh4586462.shtml">下个月你的住房公积金或将调整 将如何变动</a></h1>

<h1 data-client="headline"><a target="_blank" href="http://news.sina.com.cn/c/2018-06-04/doc-ihcmurvh5113597.shtml">周永康令计划后 又有人因“秘密文件”被查</a></h1>
 <p data-client="throw">[<a target="_blank" href="http://news.sina.com.cn/o/2018-06-04/doc-ihcmurvh3397095.shtml">对抗审查</a> <a target="_blank" href="http://news.sina.com.cn/c/2018-06-04/doc-ihcmurvh5113597.shtml">任职仅3年多给所在单位政治生态造成不小的负面影响</a>]</p>




<h1 data-client="headline"><a target="_blank" href="http://news.sina.com.cn/s/2018-06-04/doc-ihcmurvh2107739.shtml">崔永元范冰冰互撕结局难料 一个赢家已产生</a></h1>






<p data-client="throw">[<a target="_blank" href="http://news.sina.com.cn/s/2018-06-04/doc-ihcmurvh2225167.shtml">4天6千万合同刷爆网络 崔永元却犯低级错误</a> <a target="_blank" href="http://news.sina.com.cn/s/2018-06-04/doc-ihcmurvh5758543.shtml">阴阳合同过时了</a>]</p>

<p data-client="throw">[<a target="_blank" href="http://news.sina.com.cn/s/2018-06-04/doc-ihcmurvh1800529.shtml">崔永元道歉：4天6000万与她无关</a> <a target="_blank" href="http://news.sina.com.cn/s/2018-06-04/doc-ihcmurvh4790999.shtml">人民日报官方微博也发话了</a>]</p>







</div>


<div id="ad_entry_b2">


<ul class="list_14" data-sudaclick="blk_news_1">

<li class="topli14"><a target="_blank" href="http://news.sina.com.cn/c/2018-06-04/doc-ihcmurvh4760383.shtml">王主任被儿媳举报有17处房产 中纪委机关刊点名了</a></li>

<li><a target="_blank" href="http://news.sina.com.cn/c/2018-06-04/doc-ihcmurvh6709960.shtml">从中央空降近1年 重庆公安局长在做这件事</a></li>



<li><a target="_blank" href="http://news.sina.com.cn/c/2018-06-04/doc-ihcmurvh4206815.shtml">美媒对这事很不爽但也只能建议：别踩中国的雷</a></li><li><a target="_blank" href="http://news.sina.com.cn/c/2018-06-04/doc-ihcmurvh4318613.shtml">美防长香会发言就南海问题指责中国 罕见无人捧场</a></li><li><a target="_blank" href="http://news.sina.com.cn/c/2018-06-04/doc-ihcmurvh6264059.shtml">副市长暗访便民服务中心 女同志做了这事当天被辞</a></li>








</ul>


<!-- 虚线开始 -->
<div class="line_01"></div>
<!-- 虚线结束 -->

<ul class="list_14" data-sudaclick="blk_news_2"><li class="topli14"><a target="_blank" href="http://news.sina.com.cn/c/2018-06-04/doc-ihcmurvh3537515.shtml">著名播音员离世5年后 声音在央视纪录片“复活”</a></li>









<li><a target="_blank" href="http://news.sina.com.cn/o/2018-06-04/doc-ihcmurvh2273003.shtml">官员接通知后睡觉不去现场被免职 4名领导被处分</a></li>

<li><a target="_blank" href="http://news.sina.com.cn/w/sy/2018-06-04/doc-ihcmurvh5890539.shtml">杜特尔特在韩国公开亲吻女菲侨 网友：真恶心(图)</a></li>


<li><a target="_blank" href="http://news.sina.com.cn/c/2018-06-04/doc-ihcmurvh7415961.shtml">南通市通州区纪委副书记在家自缢身亡 已排除他杀</a></li>

</ul>

<!-- 虚线开始 -->
<div class="line_01"></div>
<!-- 虚线结束 -->

<ul class="list_14" data-sudaclick="blk_news_3"><li class="topli14"><a target="_blank" href="http://news.sina.com.cn/s/2018-06-04/doc-ihcmurvh1451029.shtml">妻子睡觉这个特殊癖好 新婚丈夫被迫分床睡想离婚</a></li>




<li><a target="_blank" href="http://video.sina.com.cn/p/news/c/doc/2018-06-04/192968752712.html" class="videoNewsLeft">保姆纵火案女主人报警录音曝光 大喊“我出不来”</a></li>

<li><a target="_blank" href="http://news.sina.com.cn/s/2018-06-04/doc-ihcmurvh4418049.shtml">81岁大爷坚持健身60年 一身肌肉堪比史泰龙(图)</a></li>

<li><a target="_blank" href="http://news.sina.com.cn/o/2018-06-03/doc-ihcmurvf9447248.shtml">两女子深夜点外卖 要外卖小哥干这事(图)</a> <a target="_blank" href="http://sifa.sina.com.cn/">司法频道</a></li>





</ul>

<!-- 虚线开始 -->

<div class="line_01"></div>
<!-- 虚线结束 -->
<ul class="list_14" data-sudaclick="blk_news_4"><li class="topli14"><a target="_blank" href="http://news.sina.com.cn/w/2018-06-04/doc-ihcmurvh4483741.shtml">韩国出土镶26枚中国五铢钱的铜戈 专家：堪称国宝</a></li>




<li><a target="_blank" href="http://finance.sina.com.cn/chanjing/cyxw/2018-06-04/doc-ihcmurvh4547572.shtml">新华社半月谈：对“大企业排污特权”不能姑息迁就</a></li>


<li><a target="_blank" href="http://finance.sina.com.cn/review/jcgc/2018-06-04/doc-ihcmurvh2140104.shtml">检察日报：爆料者有义务把材料拿出来配合税务调查</a></li>
<li data-client="throw" id="sinaDynContBlockID" charslen="19">
<a href="http://video.sina.com.cn/news/spj/topvideoes20180603/#258592518" target="_blank" class="videoNewsLeft">情侣住宾馆 男子睡梦中舌头被蜈蚣咬伤</a>
</li>

</ul></div>

<!-- 重点新闻1号位 结束 -->
<!-- 新闻中心要闻区 end -->

<!-- 抓站_要闻 end -->
              <!-- wap_sina_news_yaowen end 勿删 -->
              <a href="javascript:void(0)" class="more_news" id="tab_yw_01" style=" bottom:17px;">更多要闻&gt;</a> 
            </div>

            <!-- 2 -->
            <div class="blk_04" id="blk_yw_02" style="display: none; ">


<div class="b_tit">
  <div class="b_tname">要闻</div>
  <div class="b_time">北京时间：2018.6.4 周一</div>
</div>

<div class="ct_t_01" id="syncad_1_b" data-sudaclick="yaowen" style="padding-bottom: 3px;overflow: hidden;">

<h1 ><a target="_blank" href="http://news.sina.com.cn/c/xl/2018-06-03/doc-ihcmurvf9585028.shtml">习近平的足迹：指引中国特色大国外交</a></h1>
<h1 ><a target="_blank" href="http://news.sina.com.cn/o/2018-06-03/doc-ihcmurvh0375881.shtml">欧盟向WTO状告中国 商务部回应</a></h1>
 <h1 ><a target="_blank" href="http://news.sina.com.cn/c/2018-06-04/doc-ihcmurvh1165221.shtml">怕美不懂 新华社这篇中美经贸文章太直白</a></h1>

<p data-client="throw">[<a target="_blank" href="http://news.sina.com.cn/c/2018-06-03/doc-ihcmurvf8592913.shtml">谈判最新成果释放三个重磅信号</a> <a target="_blank" href="http://news.sina.com.cn/o/2018-06-03/doc-ihcmurvh0588166.shtml">中方声明让美放下“大棒”威胁</a>]</p>

<h1 ><a target="_blank" href="http://news.sina.com.cn/c/2018-06-04/doc-ihcmurvh1609843.shtml">岛内水果价格暴跌 果农怒挂横幅抗议民进党</a></h1>

<h1 ><a target="_blank" href="http://news.sina.com.cn/s/2018-06-04/doc-ihcmurvh1800529.shtml">反转?崔永元道歉：4天6000万与范冰冰无关</a></h1>

<p data-client="throw">[<a target="_blank" href="http://news.sina.com.cn/s/2018-06-04/doc-ihcmurvh2321594.shtml">范冰冰的税为何在无锡查</a> <a target="_blank" href="http://news.sina.com.cn/s/2018-06-04/doc-ihcmurvh2107739.shtml">崔范互撕结局难料 可一个赢家已产生</a>]</p>

<p data-client="throw">[<a target="_blank" href="http://news.sina.com.cn/s/2018-06-04/doc-ihcmurvh2225167.shtml">4天6千万合同爆活 崔永元却犯了低级错误</a> <a target="_blank" href="http://news.sina.com.cn/c/2018-06-04/doc-ihcmurvh1443413.shtml">侠客岛:背后藏大问题</a>]</p>

</div>

<div id="ad_entry_b2_b">

<ul class="list_14" data-sudaclick="blk_news_1">

<li class="topli14"><a target="_blank" href="http://news.sina.com.cn/c/nd/2018-06-03/doc-ihcmurvh0646913.shtml">中将领队 解放军将领们到新加坡出席这个会(图)</a></li>

<li><a target="_blank" href="http://news.sina.com.cn/o/2018-06-04/doc-ihcmurvh2146763.shtml">国地税合并加速 养老医疗等社保费用将由税务征管</a></li>

<li><a target="_blank" href="http://news.sina.com.cn/c/nd/2018-06-03/doc-ihcmurvh0615973.shtml">财政部原副部长补选全国人大代表 有啥特殊之处？</a></li><li><a target="_blank" href="http://news.sina.com.cn/c/nd/2018-06-03/doc-ihcmurvh0806881.shtml">副市长暗访便民中心 有工作人员戴耳机听歌被辞退</a></li><li><a target="_blank" href="http://news.sina.com.cn/o/2018-06-03/doc-ihcmurvf9895293.shtml">美媒不爽美企频向中国道歉 但只能建议：多雇专家</a></li>

</ul>

<div class="line_01"></div>

<ul class="list_14" data-sudaclick="blk_news_2"><li class="topli14"><a target="_blank" href="http://mil.news.sina.com.cn/china/2018-06-04/doc-ihcmurvh2218784.shtml">歼20已满天飞 蔡英文却想用这款飞机留住台湾青年</a></li>

<li><a target="_blank" href="http://news.sina.com.cn/c/zj/2018-06-04/doc-ihcmurvh2224794.shtml">1个县卖小龙虾1年能挣多少钱?这个数字或让你吃惊</a></li>

<li><a target="_blank" href="http://news.sina.com.cn/o/2018-06-03/doc-ihcmurvh0206303.shtml">范冰冰代言企业被查封数十亿 三三集团多高管被抓</a></li>

<li><a target="_blank" href="http://news.sina.com.cn/w/2018-06-04/doc-ihcmurvh2338678.shtml">克林顿不满特朗普“打嘴炮”:我这样 我妈会打我</a></li>

</ul>

<div class="line_01"></div>

<ul class="list_14" data-sudaclick="blk_news_3"><li class="topli14"><a target="_blank" href="http://news.sina.com.cn/s/2018-06-04/doc-ihcmurvh1451029.shtml">妻子睡觉这个特殊癖好 新婚丈夫被迫分床睡想离婚</a></li>

<li><a target="_blank" href="http://news.sina.com.cn/o/2018-06-03/doc-ihcmurvf9447248.shtml">两女子深夜点外卖 要求外卖小哥干这事(图)</a></li>

<li><a target="_blank" href="http://news.sina.com.cn/s/2018-06-03/doc-ihcmurvf9393039.shtml">37岁美女每天至少敷两片面膜 去医院一查后悔不已</a></li>

<li><a target="_blank" href="http://news.sina.com.cn/s/2018-06-03/doc-ihcmurvf9057758.shtml">中国人死亡第一元凶不是癌症 想不到是它</a> <a target="_blank" href="http://sifa.sina.com.cn/">司法频道</a></li>

</ul>

<div class="line_01"></div>

<ul class="list_14" data-sudaclick="blk_news_4"><li class="topli14"><a target="_blank" href="http://news.sina.com.cn/w/2018-06-04/doc-ihcmurvh1352129.shtml">俄前外长:俄从未处于孤独中 俄中不分老大老二</a></li>

<li><a target="_blank" href="http://finance.sina.com.cn/zt_d/fbbshui/">税务机关调查影视阴阳合同事件</a> <a target="_blank" href="http://finance.sina.com.cn/china/gncj/2018-06-04/doc-ihcmurvh1475686.shtml">律师:有可能涉嫌洗钱</a></li>

<li><a target="_blank" href="http://finance.sina.com.cn/chanjing/gsnews/2018-06-04/doc-ihcmurvh1441551.shtml">内部人士谈娃哈哈颓势:宗庆后亲力亲为 公司缺乏人才</a></li>
<li data-client="throw"  charslen="19">
<a href="http://video.sina.com.cn/news/spj/topvideoes20180603/#258592518" target="_blank" class="videoNewsLeft">情侣住宾馆 男子睡梦中舌头被蜈蚣咬伤</a>
</li>

</ul></div>



              <a href="javascript:void(0)" class="more_news selected" id="tab_yw_02" style="bottom:17px;">返回&gt;&gt;</a>
            </div>

            <script type="text/javascript" id="js_tab_1">
            jsLoader(ARTICLE_JSS.common,function(){
                var subshow = new SubShowClass('none','onclick');
                subshow.addLabel('tab_yw_02','blk_yw_01');
                subshow.addLabel('tab_yw_01','blk_yw_02');
            });
            </script>
<!-- wapnewstop browser end 勿删 -->
<!-- 要闻 end -->
            <!-- wapnewstop browser end 勿删 -->
            <script type="text/javascript" id="js_tab_1">
            jsLoader(ARTICLE_JSS.common,function(){
                var subshow = new SubShowClass('none','onclick');
                subshow.addLabel('tab_yw_02','blk_yw_01');
                subshow.addLabel('tab_yw_01','blk_yw_02');
            });
            </script>
          <!-- 要闻 end -->

          <!-- middle end -->
          </div>



		<div class="p_right">
			<style type="text/css">
    .zhengwu-mod{
      width: 260px;
      clear: both;
    }
    .zhengwu-mod .item{
      padding-top: 10px;
    }
    .tlt-topTalk{
      display: inline-block;
      width: 106px;
      height: 23px;
      background: url('//n.sinaimg.cn/news/926f00e3/20180509/toptalk.png') no-repeat;
      margin:8px 0 0 5px;
    }
	.ct_p_05{height:170px; overflow:hidden;}
  </style>

<div class="blk_tit">
	<ol>
		<li class="selected" data-sudaclick="channel-yst"><a href="http://news.sina.com.cn/gaotan/" target="_blank">议事厅</a></li>
		<i class="tlt-topTalk"></i>
	</ol>
</div>
<!--lunbo-->
<div class="blk_main_02 mb_10" data-sudaclick="channel-yst">
	<div class="b_cont">
		<div id="yst_mod" class="ct_p_05 clearfix">
<div class="ct_pic"><a href="http://news.sina.com.cn/gaotan/2018-05-30/doc-ihcffhsv8507843.shtml" target="_blank"><img data-src="http://n.sinaimg.cn/news/transform/60/w520h340/20180601/AC1E-hcikcev9437827.jpg" width="260" height="170" /><span class="ct_txt">安康市长:人才大战,小城市也要活下去</span></a></div><div class="ct_pic"><a href="http://news.sina.com.cn/gaotan/2018-05-10/doc-ihaichqz2313032.shtml" target="_blank"><img data-src="http://n.sinaimg.cn/news/transform/60/w520h340/20180511/OszR-hamfahw0379727.jpg" width="260" height="170" /><span class="ct_txt">汶川书记的十年:早上对镜子说&quot;你行&quot;</span></a></div><div class="ct_pic"><a href="http://news.sina.com.cn/gaotan/2018-04-22/doc-ifznefkh7438639.shtml" target="_blank"><img data-src="http://n.sinaimg.cn/news/transform/60/w520h340/20180509/qdAD-fzrwiaz5145567.jpg" width="260" height="170" /><span class="ct_txt">四川宣汉县委书记选干部 现场出题作文</span></a></div><div class="ct_pic"><a href="http://news.sina.com.cn/gaotan/2018-04-02/doc-ifyswxnq1246250.shtml" target="_blank"><img data-src="http://n.sinaimg.cn/news/transform/60/w520h340/20180509/M8Vq-haichqy9728913.jpg" width="260" height="170" /><span class="ct_txt">广西融水县长：县长不敢融资是不合格</span></a></div><div class="ct_pic"><a href="http://news.sina.com.cn/gaotan/2018-03-18/doc-ifyshfur4016253.shtml" target="_blank"><img data-src="http://n.sinaimg.cn/news/transform/60/w520h340/20180509/A8SI-haichqy9736444.jpg" width="260" height="170" /><span class="ct_txt">贵阳市长:布2万天眼，劫案降至每日半起</span></a></div>		</div>
		<a href="javascript:void(0)" class="scrArrAbsLeft" id="btn_ystLeft"></a>
		<a href="javascript:void(0)" class="scrArrAbsRight" id="btn_ystRight"></a>
	</div>

	<div class="b_cons">
		<span class="scrDotList" id="ystPoint_mod">
			<span></span>
		</span>
	</div>
</div>
<script>
	jsLoader(ARTICLE_JSS.common, function () {
		var focusScroll = new ScrollPic();
		focusScroll.scrollContId = "yst_mod"; //内容容器ID

		focusScroll.dotListId = "ystPoint_mod";//点列表ID
		focusScroll.dotClassName = "";//点className
		focusScroll.dotOnClassName = "on";//当前点className
		focusScroll.listType = "";//列表类型(number:数字，其它为空)
		focusScroll.listEvent = "onmouseover"; //切换事件

		focusScroll.frameWidth = 260;//显示框宽度
		focusScroll.pageWidth = 260; //翻页宽度
		focusScroll.upright = false; //垂直滚动
		focusScroll.speed = 10; //移动速度(单位毫秒，越小越快)
		focusScroll.space = 40; //每次移动像素(单位px，越大越快)
		focusScroll.autoPlay = false; //自动播放
		focusScroll.autoPlayTime = 5; //自动播放间隔时间(秒)
		focusScroll.circularly = true;
		focusScroll.initialize(); //初始化
		document.getElementById('btn_ystLeft').onmousedown = function () {
			focusScroll.pre();
			return false;
		}
		document.getElementById('btn_ystRight').onmousedown = function () {
			focusScroll.next();
			return false;
		}
	});

</script>
<!--end lunbo-->
			
<div class="blk_tit mb_10">
	<ol>
		<li class="selected" data-sudaclick="blk_newsgeek"><a href="http://gov.sina.com.cn/" target="_blank">新浪政务</a></li>
	</ol>
</div>
<!--zhengwu-->
<div class="View" style="border: none; padding-bottom: 0;">
	<div class="zhengwu-mod" data-sudaclick="blk_newsgeek">
<div class="item">
			<div class="tl"><a href="http://news.sina.com.cn/gov/2018-06-04/doc-ihcmurvh2862067.shtml" target="_blank" class="zhk_tl">政务公号"抢滩"短视频平台 方式更直观</a></div>
			<div class="outline">
				<div class="thumb"><a href="http://news.sina.com.cn/gov/2018-06-04/doc-ihcmurvh2862067.shtml" target="_blank"><img src="http://n.sinaimg.cn/news/transform/245/w110h135/20180604/7gDW-hcmurvh2890295.jpg"></a></div>
<div class="txt">政务公号“抢滩”短视频平台，政法系统公号占比较大。<a href="http://news.sina.com.cn/gov/2018-06-04/doc-ihcmurvh2862067.shtml" target="_blank">[详细]</a></div>
	</div>
	</div><div class="item">
			<div class="tl"><a href="http://news.sina.com.cn/gov/2018-06-04/doc-ihcmurvh2868145.shtml" target="_blank" class="zhk_tl">"00后"登场 看今年高考有这些新特征</a></div>
			<div class="outline">
				<div class="thumb"><a href="http://news.sina.com.cn/gov/2018-06-04/doc-ihcmurvh2868145.shtml" target="_blank"><img src="http://n.sinaimg.cn/news/transform/245/w110h135/20180604/CniD-hcmurvh2914386.jpg"></a></div>
<div class="txt">今年高考看点不少，一批“接地气”的本科专业落地招生，还y有高考加分项目继续减少和规范。<a href="http://news.sina.com.cn/gov/2018-06-04/doc-ihcmurvh2868145.shtml" target="_blank">[详细]</a></div>
	</div>
	</div>	</div>
</div>
<ul class="list_12 link_c666">
<li><a href="http://news.sina.com.cn/gov/2018-06-04/doc-ihcmurvh2834314.shtml" target="_blank">中国人假日越来越多 "共时化"休假现象突出</a></li><li><a href="http://news.sina.com.cn/gov/2018-06-04/doc-ihcmurvh2829937.shtml" target="_blank">40多城市出台招揽人才政策 招才需量力而行</a></li></ul>
 
			<style>
			.zhengwu-mod .item .outline .thumb img{
     			 width:110px; height:135px;
    		}
			
			</style>
			<div id="blk_btnad_1">
				<!--_SINA_ADS_BEGIN_-->
				<!-- 260x210轮播矩形广告 开始 -->
				<div id="ad_47259">
					<script async charset="utf-8" src="//d5.sina.com.cn/litong/zhitou/sinaads/release/sinaads.js"></script><ins class="sinaads" data-ad-pdps="PDPS000000047259"></ins><script>(sinaads = window.sinaads || []).push({});</script>
				</div>
				<!--_SINA_ADS_END_-->
				<!--t id="news_web_index_v2015_adpic_1"-->

			</div><!--end ad -->
		</div><!--end left -->
		
	</div><!--end hq -->

<script type="text/javascript">
		function ScrollDiv(root, $){
			var scrollItems = $('div.item', root);
			var total = scrollItems.length;
			var currentIndex = 0;
			var prevBtn = $('a[role="prev"]', root);
			var nextBtn = $('a[role="next"]', root);
			var duration = 50;
			prevBtn.on('click', function (evt) {
				if (currentIndex > 0) {
					nextBtn.removeClass('nxt_dis').addClass('nxt');
					$(scrollItems[currentIndex]).hide();
					$(scrollItems[--currentIndex]).show();
					if (currentIndex === 0) {
						prevBtn.removeClass('pre').addClass('pre_dis');
					}
				}
			});
			nextBtn.on('click', function (evt) {
				if (currentIndex < total - 1) {
					prevBtn.removeClass('pre_dis').addClass('pre');
					$(scrollItems[currentIndex]).hide();
					$(scrollItems[++currentIndex]).show();
					if (currentIndex === (total-1)){
						nextBtn.removeClass('nxt').addClass('nxt_dis');
					}
				}
			});
		}
</script>

<!-- 首屏 firstpage -->

<!-- 返回顶部 begin -->
	<style type="text/css">
	.side-btns-wrap{width:50px;left: 50%; margin-left:505px;position: fixed;bottom: 40px; _position:absolute;_top:expression(documentElement.scrollTop + documentElement.clientHeight-120);z-index:100;visibility: hidden;overflow: hidden;}
	.side-btns-top{width:50px;}
	.side-btns-top a{display: block; line-height:500px; cursor:pointer;}
	.side-btns-top-btn { height: 50px; width: 50px;background:url(http://i0.sinaimg.cn/dy/deco/2012/1227/news_zxh_content_btn_bg.png) no-repeat 0 -110px;  filter:Alpha(Opacity=35); opacity:.35; overflow:hidden;}
	.side-btns-top-btn:hover {filter:Alpha(Opacity=50); opacity:.5;}
	.side-btns-top-close{width: 50px;height: 18px;margin-top:1px;background: url(http://i3.sinaimg.cn/dy/deco/2013/0913/close2.png) no-repeat;}
	.side-btns-wrap-resize{display: none !important;}
	</style>

	<script type="text/javascript">
	// 返回顶部js
	(function(aClz,maxSize,co) {
		var doc = document, side = (function() {var body = doc.body, firstChild = body.firstChild, wrap = doc.createElement('div'); wrap.className = 'side-btns-wrap'; wrap.innerHTML = '<div class="side-btns-top"><a class="side-btns-top-btn" href="javascript:;" title="返回顶部" suda-uatrack="key=channel_index_up_to_top&value=news" hidefocus>返回顶部</a><a class="side-btns-top-close" href="javascript:;" title="关闭" suda-uatrack="key=channel_index_up_to_top&value=news_close" hidefocus>关闭</a></div>'; firstChild ? firstChild.parentNode.insertBefore(wrap, firstChild) : body.appendChild(wrap); return wrap; })(), clz = side.className, nClz = clz + ' ' + aClz, cookieName = co.name || 'close_newsidxtop', domain = co.domain || 'news.sina.com.cn', path = co.path|| '/', lnks = side.getElementsByTagName('a'), btn = lnks[0], close = lnks[1], addEvent = function(o, s, fn) {if (o.attachEvent) {o.attachEvent('on' + s, fn); } else {o.addEventListener(s, fn, false); } return o; }, toggle = function() {var top = doc.documentElement.scrollTop || doc.body.scrollTop, visible = (top > 0 ? 'visible' : 'hidden'); side.style.visibility = visible; }, sideToggle = function(dis) {side.style.display = dis; }, resize = function() {var body = doc.documentElement || doc.body; if (!body) {return; } var width = body.offsetWidth; if (width < maxSize) {side.className = nClz; } else {side.className = clz; } }, toTop = function() {doc.documentElement.scrollTop = 0; doc.body.scrollTop = 0; }; var cookie = (function() {var co = {}; co.getCookie = function(name) {name = name.replace(/([\.\[\]\$])/g, '\\\$1'); var rep = new RegExp(name + '=([^;]*)?;', 'i'); var co = document.cookie + ';'; var res = co.match(rep); if (res) {return unescape(res[1]) || ""; } else {return ""; } }; co.setCookie = function(name, value, expire, path, domain, secure) {var cstr = []; cstr.push(name + '=' + escape(value)); if (expire) {var dd = new Date(); var expires = dd.getTime() + expire * 3600000; dd.setTime(expires); cstr.push('expires=' + dd.toGMTString()); } if (path) {cstr.push('path=' + path); } if (domain) {cstr.push('domain=' + domain); } if (secure) {cstr.push(secure); } document.cookie = cstr.join(';'); }; co.deleteCookie = function(name) {document.cookie = name + '=;' + 'expires=Fri, 31 Dec 1999 23:59:59 GMT;'; }; return co; })(); var display = cookie.getCookie(cookieName); if(display!=''){sideToggle('none'); return; } sideToggle('block'); resize(); addEvent(window, 'resize', resize); addEvent(close,'click',function(e){sideToggle('none'); cookie.setCookie(cookieName,'1',15*24,path,domain); if(window.event){window.event.returnValue = false; }else{e.preventDefault(); } }); addEvent(window, 'scroll', toggle); addEvent(btn, 'click', toTop); })('side-btns-wrap-resize',1110,{
		name:'close_newsidxtop',				//cookie名
		domain:'news.sina.com.cn'	//domain 根据频道不同
	});
	</script>

<!-- 返回顶部 end -->


<!--增加现场视频 PEIHE1-->
<div class="part_01 clearfix" data-sudaclick="blk_livevideo">
	<div class="Live_slie_tl" id="current-video-head" data-sudaclick="video_top_bar">
		<div class="Slide_control" data-sudaclick="video_top_arrow">
			<a href="javascript:;" id="current-video-prev" class="pre"></a>
			<span class="slide_nm" style="display:none"><span class="current-num">1</span><i>/</i><span class="total-num">8</span></i></span>
			<a href="javascript:;" id="current-video-next" class="nxt"></a>
		</div>
		<a href="http://video.sina.com.cn/news/" target="_blank">现场视频</a>
	</div>

  <div class="Live_slide" data-sudaclick="video_middle_arrow" >
   	<ul class="lst" id="current-video"  data-sudaclick="video_middle" style="width:1011px;overflow:hidden">

<li><div class="thumb"><a href="http://video.sina.com.cn/news/spj/topvideoes20180603/#258575670" target="_blank"><img src="http://n.sinaimg.cn/news/transform/509/w326h183/20180603/eK1b-hcmurvf7678683.png"><i class="slide_icon"></i></a></div><div class="item_tl"><a href="http://video.sina.com.cn/news/spj/topvideoes20180603/#258575670" target="_blank" class="slide_tl">82岁老院士“南海深潜记”</a></div></li>
<li><div class="thumb"><a href="http://video.sina.com.cn/news/spj/topvideoes20180604/#258614961" target="_blank"><img src="http://n.sinaimg.cn/video/transform/509/w326h183/20180604/IDDv-hcmurvh2990600.jpg"><i class="slide_icon"></i></a></div><div class="item_tl"><a href="http://video.sina.com.cn/news/spj/topvideoes20180604/#258614961" target="_blank" class="slide_tl">心有余悸！泰男子发现引擎盖下藏巨蟒</a></div></li>
<li><div class="thumb"><a href="http://video.sina.com.cn/news/spj/topvideoes20180604/#258537270" target="_blank"><img src="http://n.sinaimg.cn/video/transform/509/w326h183/20180604/znIM-hcmurvh2998501.jpg"><i class="slide_icon"></i></a></div><div class="item_tl"><a href="http://video.sina.com.cn/news/spj/topvideoes20180604/#258537270" target="_blank" class="slide_tl">森林幼儿园：孩子们在大自然中成长</a></div></li>
<li><div class="thumb"><a href="http://video.sina.com.cn/news/spj/topvideoes20180604/#258615457" target="_blank"><img src="http://n.sinaimg.cn/video/transform/509/w326h183/20180604/Q5R_-hcmurvh3003397.jpg"><i class="slide_icon"></i></a></div><div class="item_tl"><a href="http://video.sina.com.cn/news/spj/topvideoes20180604/#258615457" target="_blank" class="slide_tl">衡水二中给考生发钱：寓意“十全十美”</a></div></li>
<li><div class="thumb"><a href="http://video.sina.com.cn/news/spj/topvideoes20180603/#258587391" target="_blank"><img src="http://n.sinaimg.cn/news/transform/509/w326h183/20180603/cEuP-hcmurvf7724970.png"><i class="slide_icon"></i></a></div><div class="item_tl"><a href="http://video.sina.com.cn/news/spj/topvideoes20180603/#258587391" target="_blank" class="slide_tl">同一部电影 不同的人看到不一样的版本</a></div></li>
<li><div class="thumb"><a href="http://video.sina.com.cn/p/news/s/doc/2018-06-04/075468740728.html" target="_blank"><img src="http://n.sinaimg.cn/video/transform/509/w326h183/20180604/7mpQ-hcmurvh3014078.jpg"><i class="slide_icon"></i></a></div><div class="item_tl"><a href="http://video.sina.com.cn/p/news/s/doc/2018-06-04/075468740728.html" target="_blank" class="slide_tl">学生改编《我的天空》为高考生加油</a></div></li>
<li><div class="thumb"><a href="http://video.sina.com.cn/news/spj/topvideoes20180604/#258615254" target="_blank"><img src="http://n.sinaimg.cn/news/transform/509/w326h183/20180604/TTYz-hcmurvh3034044.jpg"><i class="slide_icon"></i></a></div><div class="item_tl"><a href="http://video.sina.com.cn/news/spj/topvideoes20180604/#258615254" target="_blank" class="slide_tl">女子吃隔夜小龙虾 食物中毒险昏迷</a></div></li>
<li><div class="thumb"><a href="http://video.sina.com.cn/p/news/live/doc/2018-06-04/071868740054.html" target="_blank"><img src="http://n.sinaimg.cn/news/transform/509/w326h183/20180604/99g2-hcmurvh3040206.jpg"><i class="slide_icon"></i></a></div><div class="item_tl"><a href="http://video.sina.com.cn/p/news/live/doc/2018-06-04/071868740054.html" target="_blank" class="slide_tl">熊妈妈每天带熊宝宝闯泳池游泳</a></div></li>
<li><div class="thumb"><a href="http://video.sina.com.cn/news/spj/topvideoes20180603/#258508503" target="_blank"><img src="http://n.sinaimg.cn/news/transform/509/w326h183/20180603/NSLV-hcmurvf7736542.png"><i class="slide_icon"></i></a></div><div class="item_tl"><a href="http://video.sina.com.cn/news/spj/topvideoes20180603/#258508503" target="_blank" class="slide_tl">无人售粉机2分半钟出炉一碗螺蛳粉</a></div></li>

	</ul>
  <a href="javascript:void 0;" style="display:none" class="slide_pre"></a>
  <a href="javascript:void 0;" style="display:none" class="slide_nxt"></a>
  </div>
<script type="text/javascript">

					jsLoader(ARTICLE_JSS.jq).jsLoader(ARTICLE_JSS.common, function(){
						var $ = jQuery;
						var scrollContent = $('#current-video');
						var head = $('#current-video-head');
						var slideItem = $('li', scrollContent);
						var width = slideItem.width();
						var margin = parseInt(slideItem.css('margin-left')) + parseInt(slideItem.css('margin-right'))
						var slideWidth = slideItem.length * (width + margin);
						$('ul', scrollContent).width(slideWidth);
						$('span.slide_nm', head).show();
						
						var currentSlideNum = 1;
						var pageWidth = (width+margin) * 3
						var totalSlideNum = Math.ceil(slideWidth/pageWidth);
						var currentNum = $('span.current-num', head);
						var totalNum = $('span.total-num', head);
						totalNum.text(totalSlideNum);
						currentNum.text(currentSlideNum);
						var focusScroll = new ScrollPic();
						focusScroll.scrollContId  = "current-video"; //内容容器ID

//						focusScroll.dotListId   = "";//点列表ID
//						focusScroll.dotClassName  = "";//点className
//						focusScroll.dotOnClassName = "";//当前点className
//						focusScroll.listType  = "";//列表类型(number:数字，其它为空)
//						focusScroll.listEvent = ""; //切换事件
						focusScroll.frameWidth  = 1000;//显示框宽度
						focusScroll.pageWidth = pageWidth; //翻页宽度

						focusScroll.upright = !1; //垂直滚动
						focusScroll.speed   = 10; //移动速度(单位毫秒，越小越快)
						focusScroll.space   = 40; //每次移动像素(单位px，越大越快)
						focusScroll.autoPlay  = !0; //自动播放
						focusScroll.autoPlayTime = 5; //自动播放间隔时间(秒)
						focusScroll.circularly = !0;
						
						focusScroll.onpagechange = function(index, total){
						//console.info('index ', index, 'total', total);
								currentNum.text(Math.min(index+1, total));
						};
            focusScroll.initialize(); //初始化
						scrollContent.parent().hover(function(evt){
							preBtn.show();
							nxtBtn.show();
						}, function(evt){
							preBtn.hide();
							nxtBtn.hide();
						});
            var preBtn = $('div.Live_slide a.slide_pre').on('mousedown', function(){
                focusScroll.pre();
            });
            var nxtBtn = $('div.Live_slide a.slide_nxt').on('mousedown', function(){
                focusScroll.next();
            });
						$('#current-video-prev').on('mousedown', function(){
								focusScroll.pre();
						});
						$('#current-video-next').on('mousedown', function(){
								focusScroll.next();
						});
					});

				
</script>
</div>
<!--/增加现场视频 PEIHE1-->
	
	<!--三轮播1000*90通栏00(天)  17/08  wenjing  begin -->
	<ins class="sinaads" data-ad-pdps="PDPS000000059342"></ins>
	<script>(sinaads = window.sinaads || []).push({});</script>
	<!--三轮播1000*90通栏00(天)  end-->

    <div class="part_01 clearfix">
		<div class="p_left_2">
    	<div class="p_left">

			  <!-- left begin -->
           <div class="blk_tit blk_tit_n4">
                <ol>
                    <li class="selected" id="blk_08_lab01" data-sudaclick="mil_1t"><a href="http://mil.news.sina.com.cn/" target="_blank">军事</a></li>
                </ol>
            </div>

                <!-- wap_sina_news_mil begin 勿删 -->
                <div class="blk_08 blk_340" id="blk_08_cont01" data-sudaclick="mil_1">

                  <div class="b_cont clearfix" style="padding-bottom:12px;">
                    <div class="ct_pt_02">
<!-- gsps军事1类 p_id=1&t_id=913&f_id=23299 -->
<!--t id="news_web_get_gspsdata" pid="1" tid="913" did="9" fid="sp_f23299" cname="军事1类"-->
						<h4 class="link_c000"><a href="http://mil.news.sina.com.cn/" target="_blank">我歼20出海新画面:桶滚动作模拟驱离外机</a></h4>
<div class="ct_pic">
	<a href="http://mil.news.sina.com.cn/" target="_blank"><img  src="http://n.sinaimg.cn/mil/transform/500/w300h200/20180527/55lZ-hcaquev0375741.jpg" width="150" height="100" /></a>
</div>
<div class="ct_txt">在央视近日报道中，出现了我空军歼-20战机出海进行实战化训练的新画面，以及很有实战价值的桶滚等战斗特技飞行动作·····</div>
					 </div>
                  </div>
                  <ul class="list_12 link_c666">

<li><a href="http://mil.news.sina.com.cn/jssd/2018-06-04/doc-ihcmurvh6854690.shtml" target="_blank">美称我052D无法防御其音响反舰导弹 我无人机可解围</a></li><li><a href="http://mil.news.sina.com.cn/jssd/2018-06-04/doc-ihcmurvh6831271.shtml" target="_blank">我歼20新动态引爆全国 俄媒猜测已具备全天候作战能力</a></li><li><a href="http://mil.news.sina.com.cn/jssd/2018-06-04/doc-ihcmurvh6815145.shtml" target="_blank">美称可随时掌控我094核潜艇动态 被我一轻型军舰打脸</a></li><li><a href="http://mil.news.sina.com.cn/jssd/2018-06-04/doc-ihcmurvh6780490.shtml" target="_blank">中国未来必建六个航母群 目前双航母已稳压印度海军</a></li><li><a href="http://mil.news.sina.com.cn/jssd/2018-06-04/doc-ihcmurvh6764104.shtml" target="_blank">欧盟空客与美国波音因补贴内讧 我C919或可借机获利</a></li><li><a href="http://mil.news.sina.com.cn/jssd/2018-06-04/doc-ihcmurvh6737652.shtml" target="_blank">我军那什么保卫南海？歼11制空红旗9防守鹰击12突防</a></li><li><a href="http://mil.news.sina.com.cn/jssd/2018-06-04/doc-ihcmurvh6712680.shtml" target="_blank">以色列战机被叙击落 美指责俄越界私自提供这款武器</a></li>
				  </ul>

                </div>
                <!-- wap_sina_news_mil end 勿删 -->

                <script type="text/javascript">
				jsLoader(ARTICLE_JSS.common,function(){
					var subshow = new SubShowClass('none','onmouseover');
					subshow.addLabel('blk_08_lab01','blk_08_cont01');
					//subshow.addLabel('blk_08_lab02','blk_08_cont02');
					//subshow.addLabel('blk_08_lab03','blk_08_cont03');
					//subshow.addLabel('blk_08_lab04','blk_08_cont04');
				});
				</script>

              <!-- left end -->

  </div>
    	<div class="p_middle">
  <!-- middle begin -->

<!-- wapnewsfirsttype browser begin 勿删 -->
    <!-- 国内新闻 begin -->
    <!-- 抓站_一类 begin -->
<div class="Tit_04" id="blk_gnxwup_01">
<!-- 国内一类非标 begin -->
<div style="position:relative;"></div>
<!-- 国内一类非标 end -->

<div class="TMenu_04 dfz_news" id="gnbd_news_01">
  <ul>
  	<li class="selected" id="tab_gnylup_01"><a target="_blank" href="http://news.sina.com.cn/china/">国内新闻</a></li>
	  <li id="tab_gnylup_02" style="display:none;"><a target="_blank" href="http://roll.news.sina.com.cn/news/gnxw/gatxw/index.shtml">港澳台</a></li>
  </ul>
</div>
</div>

<style>
#tab_gnylup_02{display:none !important;}
</style>





<div id="blk_new_gnxw">
<!-- wap_sina_news_gn begin 勿删 -->

<div class="blk_09" id="blk_gnxw_01">
  <ul class="list_14_noBg" id="blk_gnxw_011" data-client="p_china" data-sudaclick="news_gn_1">
<li  class="dot topli14" ><a href="http://news.sina.com.cn/c/nd/2018-06-04/doc-ihcmurvh7795272.shtml" target="_blank">央视：滴滴顺风车再爆审核漏洞 整改成效几何？</a></li><li ><a href="http://news.sina.com.cn/o/2018-06-04/doc-ihcmurvh7674281.shtml" target="_blank">台军称F-16飞行员殉职 半年多已两架战机“出事”</a></li><li ><a href="http://news.sina.com.cn/c/nd/2018-06-04/doc-ihcmurvh7009391.shtml" target="_blank">台媒：“汉光军演”首日 大陆运-9电子侦察机绕台</a></li><li ><a href="http://news.sina.com.cn/c/nd/2018-06-04/doc-ihcmurvh6903408.shtml" target="_blank">大兴安岭过境林火火线约10公里 3600余人参与扑救</a></li><li ><a href="http://news.sina.com.cn/c/2018-06-04/doc-ihcmurvh6638613.shtml" target="_blank">厅官内定中标公司 按五星级改造当地接待条件</a></li><li ><a href="http://news.sina.com.cn/c/2018-06-04/doc-ihcmurvh6487991.shtml" target="_blank">郑钢淼任上海统战部部长 施小琳任江西宣传部部长</a></li><li ><a href="http://news.sina.com.cn/c/2018-06-04/doc-ihcmurvh6263928.shtml" target="_blank">从省长到省长书记“一肩挑” 他对这事批示上百次</a></li><li ><a href="http://news.sina.com.cn/c/nd/2018-06-04/doc-ihcmurvh6089232.shtml" target="_blank">广东省政协原常委 港澳台委员会原主任陈国兴被查</a></li><li ><a href="http://news.sina.com.cn/o/2018-06-04/doc-ihcmurvh6017786.shtml" target="_blank">国内燃油附加费复征 明天起你的机票要涨价了</a></li><li ><a href="http://news.sina.com.cn/c/nd/2018-06-04/doc-ihcmurvh5569628.shtml" target="_blank">朝韩朝美双方接触顺利进行 中方对此回应</a></li><li ><a href="http://news.sina.com.cn/c/2018-06-04/doc-ihcmurvh5095985.shtml" target="_blank">公职人员注意 这12条红线万万不能碰</a></li><li ><a href="http://news.sina.com.cn/c/2018-06-04/doc-ihcmurvh4390921.shtml" target="_blank">香港“辱国议员”冲击立会案量刑：梁游等获刑4周</a></li><li ><a href="http://news.sina.com.cn/c/2018-06-04/doc-ihcmurvh4321981.shtml" target="_blank">中国纪检监察报：共产党的干部 除了担当别无选择</a></li>  </ul>
 <a href="javascript:void(0)" class="more_news" id="tab_gnxw_01" style="display:none;">更多新闻&gt;</a>
</div>

<!-- wap_sina_news_gn end 勿删 -->

	<div class="blk_09" id="blk_gnxw_02" style="display:none">
	  <ul class="list_14_noBg" id="blk_gnxw_012" data-sudaclick="news_gn_1mr">
	  </ul>
	  <a href="javascript:void(0)" class="more_news" id="tab_gnxw_02">返回&gt;&gt;</a>
	</div>

</div>

<!-- t id="news_web_get_gspsdata" pid="1" tid="912" did="1" fid="sp_f28339" cname="国内一类" -->


    <!-- 国内新闻 end -->
    <!-- 抓站_一类 end -->
    <script type="text/javascript" id="js_tab_2">
    jsLoader(ARTICLE_JSS.common,function(){
        var subshow = new SubShowClass('none','onmouseover');
        subshow.addLabel('tab_gnylup_01','blk_new_gnxw');
        subshow.addLabel('tab_gnylup_02','blk_new_gtxw');

        var subshow02 = new SubShowClass('none','onclick');
        subshow02.addLabel('tab_gnxw_02','blk_gnxw_01');
        subshow02.addLabel('tab_gnxw_01','blk_gnxw_02');

    });
    </script>
</div>
<div class="p_left_2b">
          <!-- middle end -->
          </div>
		  <div class="p_left">

        	<div tab-type="tab-wrap">
            	<div class="blk_tit">
                    <ol>
						<li tab-type="tab-nav" class=" selected"><a href="http://history.sina.com.cn/" target="_blank">历史</a></li>
                        <li tab-type="tab-nav"><a href="http://book.sina.com.cn/" target="_blank">读书</a></li>
                    </ol>
                </div>
                <div class="blk_08 blk_0606_01">
                    <div class="blk_main">
                        <div class="blk_main_li" tab-type="tab-cont"  data-sudaclick="history_1">
<!--t id="news_web_get_gspsdata" pid="1" tid="912" did="1" fid="sp_f28338" cname="历史区块" -->
							<div class="b_cont clearfix">
	<div class="ct_p_160 clearfix">
		<div class="ct_box"><a href="http://slide.blog.sina.com.cn/slide_54_37780_55851.html#p=1
" target="_blank"><img width="160" height="90" alt="
狄仁杰：让人细思极恐的能力" src="
http://n.sinaimg.cn/history/e2da3f0c/20170814/drj1.jpg"><span class="ct_txt">
狄仁杰：让人细思极恐的能力</span></a></div>

<div class="ct_box"><a href="http://slide.blog.sina.com.cn/slide_54_37780_55702.html#p=1 
" target="_blank"><img width="160" height="90" alt="
《绣春刀Ⅱ》沈炼实有其人" src="
http://n.sinaimg.cn/history/e2da3f0c/20170804/a1.jpg"><span class="ct_txt">
《绣春刀Ⅱ》沈炼实有其人</span></a></div>	</div>
</div>
<ul class="list_12 link_c666" id="blk_book_011" style="padding-top:0;margin-top:-3px;">
	<li><a target="_blank" href="http://blog.sina.com.cn/lm/history/">虚构机关重重？盗墓最怕遇到什么</a> <a target="_blank" href="http://blog.sina.com.cn/s/blog_5fd385580102xn0i.html?tj=1">奈何闯王只愿做宋江</a></li>

<li><a target="_blank" href="http://blog.sina.com.cn/s/blog_4f8cf1540102xlbl.html?tj=1">五胡乱华对大汉民族的影响</a> <a href="http://blog.sina.com.cn/s/blog_4c622f220102x0ci.html?tj=1" target="_blank">历史上近乎完美的太子萧统</a></li>

<li><a target="_blank" href="http://blog.sina.com.cn/s/blog_7d75a1df0102y3rt.html?tj=1">魏晋第一才女：作一手好诗杀一路仇敌</a> <a target="_blank" href="http://blog.sina.com.cn/s/blog_414dbdbf0102xnlv.html?tj=1">高考前夕话历史</a></li>

<li><a target="_blank" href="http://blog.sina.com.cn/s/blog_5d2b45470102xew4.html?tj=1">李林甫死后杨国忠还告其谋反？</a> <a target="_blank" href="http://blog.sina.com.cn/s/blog_c53d95af0102xo0c.html?tj=1">北京明长城之美因为他</a></li>

<li><a href="http://blog.sina.com.cn/s/blog_180c7994b0102yedy.html?tj=1" target="_blank">父子两代备胎：赵允让赵宗实父子</a> <a target="_blank" href="http://blog.sina.com.cn/s/blog_a1929b370102xt7f.html?tj=1">顶罪的日本头号战犯</a></li>

<li><a target="_blank" href="http://blog.sina.com.cn/s/blog_562775eb0102y4dw.html?tj=1">政治天才贾谊玩儿不了政治</a> <a href="http://blog.sina.com.cn/s/blog_98a24dc30102zk0a.html?tj=1" target="_blank">李煜终被宋太宗赵炅鸩杀</a></li>

<li><a href="http://blog.sina.com.cn/s/blog_635c86d50102ygnk.html?tj=1" target="_blank">武松为何对宋江不再亲密</a> <a target="_blank" href="http://blog.sina.com.cn/s/blog_485dcc670102y1gz.html?tj=1">总是宦官成&quot;党锢事件&quot;的赢家</a></li></ul>

						</div>
                        <div class="blk_main_li" tab-type="tab-cont" style="display:none;"  data-sudaclick="book_1">
<!--t id="news_web_get_gspsdata" pid="1" tid="912" did="1" fid="sp_f28337" cname="读书区块"-->
							<div class="b_cont clearfix">
	<div class="ct_p_160 clearfix">
		<div class="ct_box"><a  href="http://vip.book.sina.com.cn/weibobook/sina_reader.php?bid=5372418" target="_blank"><img  width="160" height="90" src="http://n.sinaimg.cn/book/250/w150h100/20180523/yetg-hawmauc5778238.jpg" /><span class="ct_txt">医妃独步天下</span></a></div>
<div class="ct_box"><a  href="http://vip.book.sina.com.cn/weibobook/sina_reader.php?bid=5386738" target="_blank"><img  width="160" height="90" src="http://n.sinaimg.cn/book/250/w150h100/20180523/Oxc6-hawmauc5765766.jpg" /><span class="ct_txt">少年神医纵横都市</span></a></div>	</div>
</div>
<ul class="list_12 link_c666" id="blk_book_011" style="padding-top:0;margin-top:-3px;">
	<!--第1块-->
<li>
<a href="http://book.sina.com.cn/excerpt/" target="_blank">[新闻]</a>
<a href="http://book.sina.com.cn/news/whxw/2018-04-20/doc-ifznefkf7875849.shtml?pos=202061" target="_blank">北京市启动2018年“绿书签行动”活动</a></li>
<!--第2块-->
<li>[<a href="http://vip.book.sina.com.cn/weibobook?nwm=book_pc_0021" target="_blank">小说</a>] 
<a href="http://vip.book.sina.com.cn/weibobook/sina_reader.php?bid=5388183&nwm=book_pc_0022" target="_blank">嫡女贵凰：重生毒妃狠绝色</a> 
<a href="http://vip.book.sina.com.cn/weibobook/sina_reader.php?bid=5373727&nwm=book_pc_0023" target="_blank">那些年我爱过的女人</a></li><li>[<a href="http://vip.book.sina.com.cn/weibobook?nwm=book_pc_0024" target="_blank">小说</a>] 
<a href="http://vip.book.sina.com.cn/weibobook/sina_reader.php?bid=5397711&nwm=book_pc_0025" target="_blank">阴婚不散：傲娇鬼夫请你正经点</a> <a href="http://vip.book.sina.com.cn/weibobook/sina_reader.php?bid=5395803&nwm=book_pc_0026" target="_blank">修仙高手混花都</a></li><li>[<a href="http://vip.book.sina.com.cn/weibobook?nwm=book_pc_0027" target="_blank">小说</a>| 
<a href="http://vip.book.sina.com.cn/weibobook/sina_reader.php?bid=5371683&nwm=book_pc_0028" target="_blank">我就在这里，等着风也等你</a> <a href="http://vip.book.sina.com.cn/weibobook/sina_reader.php?bid=5394561&nwm=book_pc_0029" target="_blank">以吻封缄，终生为祭</a></li>
<!--第3块-->
<li><a href="http://vip.book.sina.com.cn/weibobook?nwm=book_pc_0030" target="_blank">[精品]</a>
<a href="http://vip.book.sina.com.cn/weibobook/sina_reader.php?bid=5387480&nwm=book_pc_0031" target="_blank">湘西赶尸鬼事之祝由世家</a> <a target="_blank" href="http://vip.book.sina.com.cn/weibobook/sina_reader.php?bid=5400416&nwm=book_pc_0032">重生之回到唐朝当王爷</a></li>
<li><a href="http://vip.book.sina.com.cn/weibobook" target="_blank">[连载]</a>
<a href="http://vip.book.sina.com.cn/weibobook/sina_reader.php?bid=5391897" target="_blank">早安，亿万金主夫君</a> 
<a href="http://vip.book.sina.com.cn/weibobook/sina_reader.php?bid=5402004" target="_blank">关于爱的事：盛装只为错过</a></li>
<li><a href="http://vip.book.sina.com.cn/weibobook" target="_blank">[完本]</a>
<a href="http://vip.book.sina.com.cn/weibobook/sina_reader.php?bid=5392121" target="_blank">王者崛起之路：人生得意无尽欢</a> 
<a href="http://vip.book.sina.com.cn/weibobook/sina_reader.php?bid=5383604" target="_blank">我以修罗成武神 </a></li></ul>
						</div>
                    </div>
                </div>
            </div>
		
		</div>
		<div class="p_middle">
          <!-- middle begin -->
            <!-- 国际新闻 begin -->
            <!-- 抓站_一类 begin -->
        <div class="Tit_04" id="blk_gjxwup_01">
          <div class="t_name"><a href="http://news.sina.com.cn/world/" target="_blank">国际新闻</a></div>
        </div>




<!-- wapsinaWORLD browser begin 勿删 -->
<!-- wap_sina_news_gj begin 勿删 -->
        <div class="blk_09" id="blk_gjxw_01">
          <ul class="list_14_noBg" id="blk_gjxw_011" data-client="p_world" data-sudaclick="news_gj_1">
<li class="dot topli14"><a href="http://news.sina.com.cn/w/2018-06-04/doc-ihcmurvh2229590.shtml" target="_blank">特朗普完成搞乱西方的任务 西方肯定要发生内讧</a></li><li><a href="http://news.sina.com.cn/w/2018-06-03/doc-ihcmurvh0095375.shtml" target="_blank">以色列士兵射杀21岁巴勒斯坦女护士 联合国谴责</a></li><li><a href="http://news.sina.com.cn/w/2018-06-04/doc-ihcmurvh2874645.shtml" target="_blank">韩媒：文在寅将加入特金会 共同宣告朝鲜战争结束</a></li><li  class="dot" ><a href="http://news.sina.com.cn/w/sy/2018-06-04/doc-ihcmurvh7531024.shtml" target="_blank">特朗普执政500天秀政绩 称同期成就胜过所有前任</a></li><li ><a href="http://news.sina.com.cn/w/sy/2018-06-04/doc-ihcmurvh7199405.shtml" target="_blank">普京出招反击 针对美国及其盟国签署反制裁法</a></li><li ><a href="http://news.sina.com.cn/w/sy/2018-06-04/doc-ihcmurvh6686666.shtml" target="_blank">莫迪在这一场合大谈中印合作 美国或要失望了</a></li><li ><a href="http://news.sina.com.cn/w/sy/2018-06-04/doc-ihcmurvh6451044.shtml" target="_blank">默克尔麻烦来了 德联邦移民与难民署被曝多起丑闻</a></li><li ><a href="http://news.sina.com.cn/w/sy/2018-06-04/doc-ihcmurvh6316608.shtml" target="_blank">普京与特朗普还有机会会晤吗？普京今天给出答案</a></li><li ><a href="http://news.sina.com.cn/w/sy/2018-06-04/doc-ihcmurvh6267760.shtml" target="_blank">日森友学园案进展:财务大臣减薪1年 20人将受处分</a></li><li ><a href="http://news.sina.com.cn/w/2018-06-04/doc-ihcmurvh5807275.shtml" target="_blank">加拿大总理回应特朗普征税：侮辱两国多年的友谊</a></li><li ><a href="http://news.sina.com.cn/w/sy/2018-06-04/doc-ihcmurvh5704908.shtml" target="_blank">菲律宾外长：中菲南海共同勘探最快明年展开</a></li>          </ul>
			<a href="javascript:void(0)" class="more_news" id="tab_gjxw_01" style="display:none;">更多新闻&gt;</a>
        </div>
<!-- wap_sina_news_gj end 勿删 -->

        <div class="blk_09" id="blk_gjxw_02" style="display:none">
          <ul class="list_14_noBg" id="blk_gjxw_012" data-sudaclick="news_gj_1mr">
          </ul>
          <a href="javascript:void(0)" class="more_news" id="tab_gjxw_02">返回&gt;&gt;</a>
        </div>
<!-- wapsinaWORLD browser end 勿删 -->

			
<!-- t id="news_web_get_gspsdata" pid="1" tid="912" did="1" fid="sp_f28340" cname="国际一类" -->
			
            <!-- 抓站_一类 end -->
            <!-- 国际新闻 end -->
            <script type="text/javascript" id="js_tab_3">
            jsLoader(ARTICLE_JSS.common,function(){
                var subshow = new SubShowClass('none','onclick');
                subshow.addLabel('tab_gjxw_02','blk_gjxw_01');
                subshow.addLabel('tab_gjxw_01','blk_gjxw_02');
            });
            </script>
          <!-- middle end -->
          </div>
</div>
<!--XBLK_STARTX-->
<div class="p_right">

	<div class="blk_07 blk_r_info">
		<div class="blk_tit mb_1">
			<ol>
				<li id="blk_07_lab01" class="selected ">国际观察</li>

				<li id="blk_07_lab02" style="display:none;"><a href="http://news.sina.com.cn/gjzg/" target="_blank">国际派</a></li>
				<li id="blk_07_lab03" class=""  style="display:none;"><a href="http://news.sina.com.cn/w/z/uselection2016/" target="_blank">美国大选</a></li>

			</ol>
		</div>
		
<!--天下周刊-->
	<div id="blk_07_cont01" class="blk_main_01" data-sudaclick="blk_zhoukan">
		<div class="View View_zhoukan" style="margin-top:0px !important;">
			<div class="Slide_control" style="display:none;">
				<a href="javascript:;" role="prev" class="pre_dis"></a>
				<a href="javascript:;" role="next" class="nxt"></a>
			</div>
			<div class="item_wrap">

				
				<div class="item">
					<div class="tl"><a href="http://news.sina.com.cn/c/2018-05-17/doc-iharvfhu3818555.shtml" target="_blank" class="zhk_tl">美国错误信号将中东推向深渊</a></div>
					<div class="outline">
						<div class="thumb"><a href="http://news.sina.com.cn/c/2018-05-17/doc-iharvfhu3818555.shtml" target="_blank"><img src="http://n.sinaimg.cn/news/transform/245/w110h135/20180517/DlzS-harvfhu6597497.jpg"></a></div>
						<div class="txt">特朗普政府向盟国开出“空头支票”，使之奉行强硬政策，酿成了中东地区的悲剧。<a href="http://news.sina.com.cn/c/2018-05-17/doc-iharvfhu3818555.shtml" target="_blank">[详细]</a></div>
					</div>
				</div>


			</div>
		</div>

	<script type="text/javascript">
		jsLoader(ARTICLE_JSS.jq, function () {
			var $ = jQuery;
			var root = $('div.View_zhoukan');
			ScrollDiv(root, $);
		});
	</script>

	</div>
<!--/天下周刊-->
		
		
		
<!--国际派-->
	<div id="blk_07_cont02" class="blk_main_01" data-sudaclick="blk_gjp">
		<div class="View View_gjp" style="margin-top:0px !important;">
			<div class="Slide_control">
				<a href="javascript:;" role="prev" class="pre_dis"></a>
				<a href="javascript:;" role="next" class="nxt"></a>
			</div>
			<div class="item_wrap">

				<div class="item">
					<div class="tl"><a href="http://news.sina.com.cn/zt_d/usconvention2016" target="_blank" class="zhk_tl">民主党大会严正以待迎奥巴马</a></div>
					<div class="outline">
						<div class="thumb"><a href="http://news.sina.com.cn/zt_d/usconvention2016" target="_blank"><img src="http://n.sinaimg.cn/news/20160728/7nRR-fxuifip3811871.jpg" width="110" height="135"></a></div>
						<div class="txt">民主党大会迎来了美国总统奥巴马，他的演讲能为希拉里助力吗？<a href="http://news.sina.com.cn/zt_d/usconvention2016" target="_blank">[详细]</a></div>
					</div>
				</div>
				<div class="item">
					<div class="tl"><a href="http://news.sina.com.cn/zt_d/usconvention2016" target="_blank" class="zhk_tl">特朗普高调出征迎战希拉里</a></div>
					<div class="outline">
						<div class="thumb"><a href="http://news.sina.com.cn/zt_d/usconvention2016" target="_blank"><img src="http://n.sinaimg.cn/news/transform/20160726/PcFE-fxuhukv7537967.jpg" width="110" height="135"></a></div>
						<div class="txt">半年前他还被美国媒体视为“笑话”，但如今，特朗普已扎扎实实地站到总统大选最前台，决战开始了<a href="http://news.sina.com.cn/zt_d/usconvention2016" target="_blank">[详细]</a></div>
					</div>
				</div>

			</div>
		</div>

	<script type="text/javascript">
		jsLoader(ARTICLE_JSS.jq, function () {
			var $ = jQuery;
			var root = $('div.View_gjp');
			ScrollDiv(root, $);
		});
	</script>

	</div>
<!--/国际派-->




<!--美国大选-->
	<div id="blk_07_cont03" class="blk_main_01" data-sudaclick="blk_mgdx">
		<div class="View View_zhoukan" style="margin-top:0px !important;">
			<div class="Slide_control" style="display:none;">
				<a href="javascript:;" role="prev" class="pre_dis"></a>
				<a href="javascript:;" role="next" class="nxt"></a>
			</div>
			<div class="item_wrap">
				
				<div class="item">
					<div class="tl"><a href="http://news.sina.com.cn/w/zg/2016-07-09/doc-ifxtwihp9896306.shtml" target="_blank" class="zhk_tl">美前军官:特朗普来给美国灭虫</a></div>
					<div class="outline">
						<div class="thumb"><a href="http://news.sina.com.cn/w/zg/2016-07-09/doc-ifxtwihp9896306.shtml" target="_blank"><img src="http://n.sinaimg.cn/news/transform/20160721/wPT0-fxuhukv7120025.png"></a></div>
						<div class="txt">“你请一个灭虫专家，不一定要在乎他的个性是怎样，你只要确保他能够除虫…特朗普就是这个人。”<a href="http://news.sina.com.cn/w/zg/2016-07-09/doc-ifxtwihp9896306.shtml" target="_blank">[详细]</a></div>
					</div>
				</div>


			</div>
		</div>

	</div>
<!--/美国大选-->

		
            <script type="text/javascript" id="js_tab_07">
            jsLoader(ARTICLE_JSS.common,function(){
                var subshow = new SubShowClass('none','onmouseover');
                subshow.addLabel('blk_07_lab01','blk_07_cont01');
                subshow.addLabel('blk_07_lab02','blk_07_cont02');
                subshow.addLabel('blk_07_lab03','blk_07_cont03');
                subshow.select(0);
            });
            </script>


	</div>


		<div class="blk_tit mb_1">
			<ol>
				<li class="selected "><a href="http://photo.sina.com.cn/" target="_blank">每日不可错过的十张图</a></li>
			</ol>
		</div>

	<div class="blk_main_02" data-sudaclick="blk_10pic">
		<div class="b_cont">
			<div id="scrPic_tenpic" class="ct_p_05 clearfix">

	<div class="ct_pic"><a href="http://slide.news.sina.com.cn/y/slide_1_88490_279008.html#p=1" target="_blank"><img data-src="http://n.sinaimg.cn/photo/transform/430/w260h170/20180604/mDqi-hcmurvh3211856.jpg" width="260" height="170" /><span class="ct_txt">新浪爱拍美图类周选43期欣赏</span></a></div>
	<div class="ct_pic"><a href="http://slide.news.sina.com.cn/y/slide_1_88490_278467.html#p=1" target="_blank"><img data-src="http://n.sinaimg.cn/photo/transform/430/w260h170/20180604/3708-hcmurvh3209369.jpg" width="260" height="170" /><span class="ct_txt">新浪爱拍记录类周选43期欣赏</span></a></div>

			</div>
			<a href="javascript:void(0)" class="scrArrAbsLeft" id="scrArrLeft_tenpic"></a>
			<a href="javascript:void(0)" class="scrArrAbsRight" id="scrArrRight_tenpic"></a>
		</div>

		<div class="b_cons">
			<span class="scrDotList" id="scrDotList_tenpic">
				<span></span>
			</span>
		</div>
	</div>


<div style="margin-top:40px;">
                        <ul class="link_c666 ul_c666" style="padding-bottom:15px;">
<li><script async charset="utf-8" src="//d5.sina.com.cn/litong/zhitou/sinaads/release/sinaads.js"></script><ins class="sinaads" data-ad-pdps="PDPS000000057077"></ins><script>(sinaads = window.sinaads || []).push({});</script></li>
                        </ul>

                <div id="blk_btnad_2">
<ins class="sinaads" data-ad-pdps="PDPS000000059732"></ins>
<script>(sinaads = window.sinaads || []).push({});</script>
                </div>
</div>

</div>


<script>
	jsLoader(ARTICLE_JSS.common, function () {
		var focusScroll = new ScrollPic();
		focusScroll.scrollContId = "scrPic_tenpic"; //内容容器ID

		focusScroll.dotListId = "scrDotList_tenpic";//点列表ID
		focusScroll.dotClassName = "";//点className
		focusScroll.dotOnClassName = "on";//当前点className
		focusScroll.listType = "";//列表类型(number:数字，其它为空)
		focusScroll.listEvent = "onmouseover"; //切换事件

		focusScroll.frameWidth = 260;//显示框宽度
		focusScroll.pageWidth = 260; //翻页宽度
		focusScroll.upright = false; //垂直滚动
		focusScroll.speed = 10; //移动速度(单位毫秒，越小越快)
		focusScroll.space = 40; //每次移动像素(单位px，越大越快)
		focusScroll.autoPlay = false; //自动播放
		focusScroll.autoPlayTime = 5; //自动播放间隔时间(秒)
		focusScroll.circularly = true;
		focusScroll.initialize(); //初始化
		document.getElementById('scrArrLeft_tenpic').onmousedown = function () {
			focusScroll.pre();
			return false;
		}
		document.getElementById('scrArrRight_tenpic').onmousedown = function () {
			focusScroll.next();
			return false;
		}
	});

</script>
<!--XBLK_ENDX-->
</div>


<script type="text/javascript">
(function() {
	function addEvent(obj, eventType, func) {
		if(obj.attachEvent) {
			obj.attachEvent("on" + eventType, func);
		} else {
			obj.addEventListener(eventType, func, false);
		}
	};

	function attachURL2Window(id,url) {
		var links;
		try {
			links = document.getElementById(id).getElementsByTagName("a");
		}catch(e) {
			links = [];
		}
		for (var i = 0, len = links.length; i < len; i++) {
			addEvent(links[i], "mousedown", function(e) {
				var writeCookie = function(O, o, l, I, p) {
				var i = "",
				c = "",
				path = "";
				if (l != null) {
					if(l == "NaN"){
						i = ";";
					}else{
						i = new Date((new Date).getTime() + l * 3600000);
						i = "; expires=" + i.toGMTString();
					}
				};
				if (I != null) {
					c = ";domain=" + I
				};
				if(p != null){
					path = ";path=" + p;
				};
				document.cookie = O + "=" + escape(o) + i + c + path;
				};
				writeCookie("directAd_news","true",1,".sina.com.cn","/");
				//点击监测
				var _clickStat = new Image();
				_clickStat.src = url + "&_=" + new Date().getTime() + "&url=";
			});
		}
	};
attachURL2Window("blk_gnxw_011","http://sina.allyes.com/main/adfclick?db=sina&bid=510151,575636,580909&cid=0,0,0&sid=583287&advid=18748&camid=89911&show=ignore");
})()
</script>




<!-- AD tl01 begin -->
<!--XAD_STARTX-->
<!--_SINA_ADS_BEGIN_-->
<div><!-- 1000x90轮播通栏01广告 开始 -->
<div id="ad_47208">
<script async charset="utf-8" src="//d2.sina.com.cn/litong/zhitou/sinaads/release/sinaads.js"></script><ins class="sinaads" data-ad-pdps="PDPS000000058970"></ins><script>(sinaads = window.sinaads || []).push({});</script>
</div>
<!-- 1000x90轮播通栏01广告 开始 --></div>
<!--_SINA_ADS_END_-->
<!--XAD_ENDX-->
<!-- AD tl01 end -->


    <div class="part_01 clearfix">
    	<div class="p_left">
            <div class="blk_new_02" id="blk_phb_01" tab-type="tab-wrap">
                <ol class="blk_nav_1">
                    <li tab-type="tab-nav" class="selected left"><a href="http://news.sina.com.cn/hotnews/" target="_blank">点击排行</a></li>
                    <li tab-type="tab-nav" style="width:110px;left:114px;"><a href="http://news.sina.com.cn/hotnews/" target="_blank">观看排行</a></li>
                    <li tab-type="tab-nav" class="right"><a href="http://news.sina.com.cn/hotnews/" target="_blank">分享排行</a></li>
                </ol>

                <div class="blk_content">
                	<div class="blk_content_1" tab-type="tab-cont">
                    	<div class="blk_content_box" tab-type="tab-wrap" >
                        	<div class="blk_content_tit">
                            	<ol>
                                    <li tab-type="tab-nav" class="selected">今天</li>
                                    <li tab-type="tab-nav">昨天</li>
                                    <li tab-type="tab-nav">一周</li>
                                </ol>
                                <div class="tit_more"><a href="http://news.sina.com.cn/hotnews/" target="_blank">更多</a></div>
                            </div>
                            <div class="blk_content_list h31" tab-type="tab-cont">
                                <ul id="all_list_01"  data-sudaclick="hotnews_all_1">

                                </ul>
                            </div>
                            <div class="blk_content_list h31" tab-type="tab-cont" style="display:none;">
                                <ul id="all_list_02"  data-sudaclick="hotnews_all_2">

                                </ul>
                            </div>
                            <div class="blk_content_list h31" tab-type="tab-cont" style="display:none;">
                                <ul id="all_list_03"  data-sudaclick="hotnews_all_3">

                                </ul>
                            </div>
                        </div>
                     </div>

                    <div tab-type="tab-cont" class="blk_content_3" style="display:none">
                        <div tab-type="tab-wrap" class="blk_content_box">
                            <div class="blk_content_tit">
                                <ol>
                                    <li class="selected" tab-type="tab-nav">今天</li>
                                    <li tab-type="tab-nav">昨天</li>
                                    <li tab-type="tab-nav">一周</li>
                                </ol>
                                <div class="tit_more"><a target="_blank" href="http://news.sina.com.cn/hotnews/">更多</a></div>
                            </div>
                            <div tab-type="tab-cont" class="blk_content_list h31">
                                <ul data-sudaclick="hotnewsvideo_1" id="newsvideo_list_01">
								</ul>
                            </div>
                            <div style="display:none;" tab-type="tab-cont" class="blk_content_list h31">
                                <ul data-sudaclick="hotnewsvideo_2" id="newsvideo_list_02">
								</ul>
                            </div>
                            <div style="display:none;" tab-type="tab-cont" class="blk_content_list h31">
                                <ul data-sudaclick="hotnewsvideo_3" id="newsvideo_list_03">
								</ul>
                            </div>
                        </div>
                    </div>

                    <div class="blk_content_2" tab-type="tab-cont" style="display:none;">
                        <div class="blk_content_list h31">
                            <ul id="all_list_04" data-sudaclick="hotnews_allshr">

                            </ul>
                        </div>
                    </div>

                </div>
            </div>

        </div>

        <div class="p_middle">
  <!-- middle begin -->
<div class="Tit_04" id="blk_cjkjqcfcup_01">
  <div class="t_name"><a href="http://finance.sina.com.cn/" target="_blank">财经</a><span class="dot">·</span><a href="http://tech.sina.com.cn/" target="_blank">科技</a><span class="dot">·</span><a href="http://auto.sina.com.cn/" target="_blank">汽车</a><span class="dot">·</span><a href="http://www.leju.com/#source=pc_sina_xwdh1&source_ext=pc_sina" target="_blank">房产</a><span class="dot">·</span><a href="http://dichan.sina.com.cn/" target="_blank">地产</a><span class="dot">·</span><a href="http://edu.sina.com.cn/" target="_blank">教育</a></div>
</div>

    <!-- wapsinaAUTO browser begin 勿删 -->



<div class="blk_09" id="blk_cjkjqcfc_01">
  <ul class="list_14_noBg" id="blk_cjkjqcfc_011" data-client="p_finance" data-sudaclick="fin_1">

    <!-- wap_sina_news_finance begin 勿删 -->
<li class="topli14"><a target="_blank" href="http://finance.sina.com.cn/roll/2018-06-04/doc-ihcmurvh1470652.shtml">格力、美的体育营销长期互怼 世界杯比赛“吹冷风”</a></li>

<li><a target="_blank" href="http://finance.sina.com.cn/roll/2018-06-04/doc-ihcmurvh1566402.shtml">三全食品首募项目“烂尾”十年  又逢新零售进展不顺</a></li>



<li><a target="_blank" href="http://finance.sina.com.cn/china/2018-06-04/doc-ihcmurvh5076342.shtml">盘点曾经偷税漏税的明星们 多数以补缴税款方式告终</a></li>






<li><a target="_blank" href="http://finance.sina.com.cn/stock/s/2018-06-04/doc-ihcmurvh5126074.shtml">金一文化违规减持仅&quot;罚酒三杯&quot;未来减持或&quot;仍不手软&quot;</a></li>


<li><a target="_blank" href="http://finance.sina.com.cn/stock/focus/2018-06-04/doc-ihcmurvh5640752.shtml">宋城演艺忽悠&quot;洋韭菜&quot;:未来几年利润翻三番 被疑炒作</a></li>    <!-- wap_sina_news_finance end 勿删 -->

    <!-- wap_sina_news_tech begin 勿删 -->
<li class="dot"><a target="_blank" href="http://tech.sina.com.cn/zt_d/tvst/">头腾大战升级 头条:腾讯封禁头条系产品 还进行污名化</a></li>


<li><a target="_blank" href="http://tech.sina.com.cn/e/2018-06-04/doc-ihcmurvh4627100.shtml">TCL集团内部重组 逐步将家电等业务分拆至TCL多媒体</a></li>



<li><span class="fe661"></span><a target="_blank" href="http://tousu.sina.com.cn/">黑猫投诉|</a><a target="_blank" href="http://tousu.sina.com.cn/complaint/view/17347222315/">用户在转转上买手机货物不符合 平台未解决</a></li>
<li><span class="fe661"></span><a target="_blank" href="http://tech.sina.com.cn/d/s/2018-06-04/doc-ihcmurvh2507253.shtml">暗物质究竟为何物？最终会消失吗？</a> <a target="_blank" href="http://gif.sina.com.cn/">小孩花式向上挑眉</a></li>    <!-- wap_sina_news_tech end 勿删 -->

<li class="dot"><a target="_blank" href="http://auto.sina.com.cn/news/hy/2018-05-18/detail-iharvfhv1021884.shtml">大众卡客车CFO辞职</a> <a target="_blank" href="http://auto.sina.com.cn/news/hy/2018-05-17/detail-iharvfhu6747216.shtml">特斯拉事故致死检察机关介入</a></li><li><a href="http://bj.leju.com/" target="_blank">
租房入学催生学位占位费
</a> <a href="http://bj.leju.com/news/2018-05-29/11206407067892390867291.shtml
" target="_blank">恒大品牌馆解密北京房企</a></li><!-- 最后一行19个字以内 --><li class="dot"><a target="_blank" href="http://edu.sina.com.cn/">“00后”登场2018年高考新特征</a> <a target="_blank" href="http://zhiyuan.edu.sina.com.cn/query/yxxq/">往年高考分数线</a></li><!-- publish_helper name='汽车一类' p_id='1' t_id='925' d_id='1' 
t id="news_web_get_gspsdata" pid="1" tid="925" did="1" fid="sp_f23645" cname="汽车一类"
t id="news_web_get_gspsdata" pid="1" tid="908" did="26" fid="sp_f24084" cname="房产一类"
t id="news_web_get_gspsdata" pid="1" tid="926" did="1" fid="sp_f23673" cname="教育一类"
-->

  </ul>
  <a href="javascript:void(0)" class="more_news" id="tab_cjkjqcfc_01">更多新闻></a>
</div>

			
<!-- gsps财经更多 -->
<!--t id="news_web_get_gspsdata" pid="1" tid="908" did="27" fid="sp_f23233" cname="财经更多"-->
<div class="blk_09" id="blk_cjkjqcfc_02" style="display:none;"> 
  <a href="javascript:void(0)" class="more_news selected" id="tab_cjkjqcfc_02">返回&gt;&gt;</a>
</div>
<!-- sp_f23233 end -->

    <!-- wapsinaAUTO browser end 勿删 -->
    <script type="text/javascript" id="js_tab_4">
     jsLoader(ARTICLE_JSS.common,function(){
        var subshow = new SubShowClass('none','onclick');
        subshow.addLabel('tab_cjkjqcfc_02','blk_cjkjqcfc_01');
        subshow.addLabel('tab_cjkjqcfc_01','blk_cjkjqcfc_02');

    });
    </script>
  <!-- middle end -->
  </div>

<!--XBLK_STARTX-->
        <div class="p_right">
  		<!-- right begin -->
        <div class="blk_12" tab-type="tab-wrap">
        	<div class="blk_tit  mb_1">
                <ol>
                    <li id="blk_12_lab01"><a href="http://health.sina.com.cn/" target="_blank">健康</a></li>
                    <li id="blk_12_lab02"><a href="http://style.sina.com.cn/" target="_blank">时尚</a></li>
                    <li id="blk_12_lab03"><a href="http://collection.sina.com.cn/" target="_blank">收藏</a></li>
                </ol>
            </div>

            <div class="blk_main">
<!-- gsps健康时尚收藏区块 p_id=1&t_id=912&f_id=28341 -->
<!--t id="news_web_get_gspsdata" pid="1" tid="912" did="1" fid="sp_f28341" cname="健康时尚收藏区块"-->
				 <div id="blk_12_cont01" class="blk_main_01" data-sudaclick="health_1">

	<!-- publish_helper name='health_1_健康一类_图文' p_id='1' t_id='916' d_id='$did' -->
	<div class="b_cont">
		<div class="ct_p_05 clearfix" id="scrPic_jksp_01">
			<div class="ct_pic"><a href="http://slide.health.sina.com.cn/d/slide_31_28379_194374.html#p=1" target="_blank"> <img src="http://n.sinaimg.cn/default/transform/430/w260h170/20180417/BacF-fzihnep0168493.jpg" width="260" height="170" alt="戒酒前后对比照" /><span class="ct_txt">戒酒前后对比照</span></a></div> <div class="ct_pic"><a href="http://med.sina.com/article_detail_103_1_36892.html" target="_blank"> <img src="http://www.sinaimg.cn/dy/2017/1122/U10617P1DT20171122164715.jpg" width="260" height="170" alt="单身养狗死亡风险降低33%" /><span class="ct_txt">单身养狗死亡风险降低33%</span></a></div> <div class="ct_pic"><a href="http://slide.health.sina.com.cn/hc/slide_31_28380_195609.html#p=1" target="_blank"> <img src="http://n.sinaimg.cn/health/20170823/QjD5-fykcppy0720894.jpg" width="260" height="170" alt="走进美国纽约大脑银行" /><span class="ct_txt">走进美国纽约大脑银行</span></a></div> <div class="ct_pic"><a href="http://slide.health.sina.com.cn/hc/slide_31_28380_192425.html#p=1" target="_blank"> <img src="http://n.sinaimg.cn/default/transform/430/w260h170/20180417/kLKe-fzihnep0177810.jpg" width="260" height="170" alt="罕见连头女婴" /><span class="ct_txt">罕见连头女婴</span></a></div> 		</div>
		<a href="javascript:void(0)" class="scrArrAbsLeft" id="scrArrLeft_jksp_01"></a>
		<a href="javascript:void(0)" class="scrArrAbsRight" id="scrArrRight_jksp_01"></a>
	</div>

	<div class="b_cons">
		<span class="scrDotList" id="scrDotList_jksp_01">
			<span></span>
		</span>
	</div>

	<ul class="list_12 link_c666">
		<li><a target="_blank" href="http://med.sina.com/article_detail_103_2_39855.html" >精子可以改装成宫颈癌杀手？</a></li><li><a target="_blank" href="http://med.sina.com/article_detail_103_1_39840.html" >“细菌+蔬菜” 抑制超75%癌细胞</a></li><li><a target="_blank" href="http://med.sina.com/article_detail_103_1_39969.html" >一孕傻三年？科学家首次证明:确实存在</a></li><li><a target="_blank" href="http://med.sina.com/article_detail_103_1_39841.html" >夜班族注意！长期夜班增加女性患癌风险</a></li>	</ul>

	<script type="text/javascript">
		jsLoader(ARTICLE_JSS.common,function(){
			var focusScroll = new ScrollPic();
			focusScroll.scrollContId  = "scrPic_jksp_01"; //内容容器ID

			focusScroll.dotListId   = "scrDotList_jksp_01";//点列表ID
			focusScroll.dotClassName  = "";//点className
			focusScroll.dotOnClassName = "on";//当前点className
			focusScroll.listType  = "";//列表类型(number:数字，其它为空)
			focusScroll.listEvent = "onmouseover"; //切换事件

			focusScroll.frameWidth  = 260;//显示框宽度
			focusScroll.pageWidth = 260; //翻页宽度
			focusScroll.upright = false; //垂直滚动
			focusScroll.speed   = 10; //移动速度(单位毫秒，越小越快)
			focusScroll.space   = 40; //每次移动像素(单位px，越大越快)
			focusScroll.autoPlay  = false; //自动播放
			focusScroll.autoPlayTime = 5; //自动播放间隔时间(秒)
			focusScroll.circularly = true;
			focusScroll.initialize(); //初始化
			document.getElementById('scrArrLeft_jksp_01').onmousedown = function(){
				focusScroll.pre();
				return false;
			}
			document.getElementById('scrArrRight_jksp_01').onmousedown = function(){
				focusScroll.next();
				return false;
			}
		});
	</script>
</div>
				 <div id="blk_12_cont02" class="blk_main_02"  data-sudaclick="fashion_1">

	<!-- publish_helper name='style_1_尚品一类_图文' p_id='1' t_id='917' d_id='$did' -->

	<div class="b_cont">
		<div class="ct_p_05 clearfix" id="scrPic_jksp_02">
			<div class="ct_pic"><a href="http://fashion.sina.com.cn/s/ce/2018-06-04/0747/doc-ihcikcew2241284.shtml" target="_blank"> <img src="http://n.sinaimg.cn/fashion/transform/430/w260h170/20180604/2_sW-hcmurvh5481206.jpg" width="260" height="170" alt="时尚圈的另类“包包种草机”" /><span class="ct_txt">时尚圈的另类“包包种草机”</span></a></div> <div class="ct_pic"><a href="http://fashion.sina.com.cn/style/man/2018-06-01/1526/doc-ihcikcev7123042.shtml" target="_blank"> <img src="http://n.sinaimg.cn/fashion/transform/430/w260h170/20180604/3_85-hcmurvh3022842.jpg" width="260" height="170" alt="姜文为啥招女人喜欢" /><span class="ct_txt">姜文为啥招女人喜欢</span></a></div> <div class="ct_pic"><a href="http://fashion.sina.com.cn/d/2018-06-04/0749/doc-ihcikcew1921473.shtml" target="_blank"> <img src="http://n.sinaimg.cn/fashion/transform/430/w260h170/20180604/oT1N-hcmurvh2659105.jpg" width="260" height="170" alt="夏天到了 你有资格炫“腹”吗？" /><span class="ct_txt">夏天到了 你有资格炫“腹”吗？</span></a></div> <div class="ct_pic"><a href="http://fashion.sina.com.cn/we/2018-06-01/1537/doc-ihcikcev7503442.shtml" target="_blank"> <img src="http://n.sinaimg.cn/eladies/transform/430/w260h170/20180604/Oc6_-hcmurvh3182557.jpg" width="260" height="170" alt="夏天就要穿美美的裙子" /><span class="ct_txt">夏天就要穿美美的裙子</span></a></div> 		</div>
		<a href="javascript:void(0)" class="scrArrAbsLeft" id="scrArrLeft_jksp_02"></a>
		<a href="javascript:void(0)" class="scrArrAbsRight" id="scrArrRight_jksp_02"></a>
	</div>

	<div class="b_cons">
		<span class="scrDotList" id="scrDotList_jksp_02">
			<span></span>
		</span>
	</div>

	<ul class="list_12 link_c666">
		<li><a target="_blank" href="http://fashion.sina.com.cn/s/ce/2018-06-04/0748/doc-ihcikcew1439800.shtml" >周冬雨高圆圆都爱同色系 居然还显瘦</a></li><li><a target="_blank" href="http://fashion.sina.com.cn/style/man/2018-06-04/0753/doc-ihcaquev6203695.shtml" >剔个牙也能让我成为朋友圈的“暴发户”</a></li><li><a target="_blank" href="http://fashion.sina.com.cn/l/ts/rc/2018-06-04/0751/doc-ihcikcew2405952.shtml" >神话“凉凉”冬虫夏草被踢出保健品圈子</a></li><li><a target="_blank" href="http://fashion.sina.com.cn/s/fo/2018-06-01/1516/doc-ihcikcev5014859.shtml" >你家爱豆让多少人踏上剁手之路</a></li>	</ul>

	<script type="text/javascript">
		jsLoader(ARTICLE_JSS.common,function(){
			var focusScroll = new ScrollPic();
			focusScroll.scrollContId  = "scrPic_jksp_02"; //内容容器ID

			focusScroll.dotListId   = "scrDotList_jksp_02";//点列表ID
			focusScroll.dotClassName  = "";//点className
			focusScroll.dotOnClassName = "on";//当前点className
			focusScroll.listType  = "";//列表类型(number:数字，其它为空)
			focusScroll.listEvent = "onmouseover"; //切换事件

			focusScroll.frameWidth  = 260;//显示框宽度
			focusScroll.pageWidth = 260; //翻页宽度
			focusScroll.upright = false; //垂直滚动
			focusScroll.speed   = 10; //移动速度(单位毫秒，越小越快)
			focusScroll.space   = 40; //每次移动像素(单位px，越大越快)
			focusScroll.autoPlay  = false; //自动播放
			focusScroll.autoPlayTime = 5; //自动播放间隔时间(秒)
			focusScroll.circularly = true;
			focusScroll.initialize(); //初始化
			document.getElementById('scrArrLeft_jksp_02').onmousedown = function(){
				focusScroll.pre();
				return false;
			}
			document.getElementById('scrArrRight_jksp_02').onmousedown = function(){
				focusScroll.next();
				return false;
			}
		});
	</script>
</div>
				 <div id="blk_12_cont01" class="blk_main_01" data-sudaclick="health_1">

	<!-- publish_helper name='collection_1_收藏一类_图文' p_id='1' t_id='918' d_id='$did' -->
	<div class="b_cont">
		<div class="ct_p_05 clearfix" id="scrPic_jksp_03">
			<div class="ct_pic"><a href="http://collection.sina.com.cn/yhds/2018-04-16/doc-ifzcyxmv3385834.shtml" target="_blank"> <img src="http://www.sinaimg.cn/dy/2018/0416/U5566P1DT20180416162853.jpg" width="260" height="170" alt="神经网络一捣乱 油画看不出真假" /><span class="ct_txt">神经网络一捣乱 油画看不出真假</span></a></div> <div class="ct_pic"><a href="http://collection.sina.com.cn/hwdt/2018-04-16/doc-ifzcyxmv2045432.shtml" target="_blank"> <img src="http://www.sinaimg.cn/dy/2018/0416/U5566P1DT20180416100746.jpg" width="260" height="170" alt="因叙利亚多年战乱 收藏老爷车尽数被毁" /><span class="ct_txt">因叙利亚多年战乱 收藏老爷车尽数被毁</span></a></div> <div class="ct_pic"><a href="http://collection.sina.com.cn/yjjj/2018-04-14/doc-ifzcyxmu2878746.shtml" target="_blank"> <img src="http://n.sinaimg.cn/default/transform/430/w260h170/20180417/yWyq-fzihnep0343456.jpg" width="260" height="170" alt="艺术拍卖整体上扬 罕见珍品提升市场" /><span class="ct_txt">艺术拍卖整体上扬 罕见珍品提升市场</span></a></div> <div class="ct_pic"><a href="http://collection.sina.com.cn/yjjj/2018-04-13/doc-ifzcyxmu0273689.shtml" target="_blank"> <img src="http://www.sinaimg.cn/dy/2018/0413/U5566P1DT20180413165635.jpg" width="260" height="170" alt="文物局：在美受损兵马俑已运回国" /><span class="ct_txt">文物局：在美受损兵马俑已运回国</span></a></div> 		</div>
		<a href="javascript:void(0)" class="scrArrAbsLeft" id="scrArrLeft_jksp_03"></a>
		<a href="javascript:void(0)" class="scrArrAbsRight" id="scrArrRight_jksp_03"></a>
	</div>

	<div class="b_cons">
		<span class="scrDotList" id="scrDotList_jksp_03">
			<span></span>
		</span>
	</div>

	<ul class="list_12 link_c666">
		<li><a target="_blank" href="http://collection.sina.com.cn/cpsc/2018-04-16/doc-ifzcyxmv3837822.shtml" >四大名著邮票：市场表现冰火两重天</a></li><li><a target="_blank" href="http://collection.sina.com.cn/yjjj/2018-04-16/doc-ifzcyxmv3781076.shtml" >三人联手推出网络诈骗新花样办书画展</a></li><li><a target="_blank" href="http://collection.sina.com.cn/cqyw/2018-04-16/doc-ifzcyxmv2441307.shtml" >壕买5600万翡翠？“雪姨”王琳怒斥造谣者</a></li>	</ul>

	<script type="text/javascript">
		jsLoader(ARTICLE_JSS.common,function(){
			var focusScroll = new ScrollPic();
			focusScroll.scrollContId  = "scrPic_jksp_03"; //内容容器ID

			focusScroll.dotListId   = "scrDotList_jksp_03";//点列表ID
			focusScroll.dotClassName  = "";//点className
			focusScroll.dotOnClassName = "on";//当前点className
			focusScroll.listType  = "";//列表类型(number:数字，其它为空)
			focusScroll.listEvent = "onmouseover"; //切换事件

			focusScroll.frameWidth  = 260;//显示框宽度
			focusScroll.pageWidth = 260; //翻页宽度
			focusScroll.upright = false; //垂直滚动
			focusScroll.speed   = 10; //移动速度(单位毫秒，越小越快)
			focusScroll.space   = 40; //每次移动像素(单位px，越大越快)
			focusScroll.autoPlay  = false; //自动播放
			focusScroll.autoPlayTime = 5; //自动播放间隔时间(秒)
			focusScroll.circularly = true;
			focusScroll.initialize(); //初始化
			document.getElementById('scrArrLeft_jksp_03').onmousedown = function(){
				focusScroll.pre();
				return false;
			}
			document.getElementById('scrArrRight_jksp_03').onmousedown = function(){
				focusScroll.next();
				return false;
			}

		});
	</script>
</div>
			</div>

            <script type="text/javascript" id="js_tab_5">
            jsLoader(ARTICLE_JSS.common,function(){
                var subshow = new SubShowClass('none','onmouseover');
                subshow.addLabel('blk_12_lab01','blk_12_cont01');
                subshow.addLabel('blk_12_lab02','blk_12_cont02');
                subshow.addLabel('blk_12_lab03','blk_12_cont03');
				subshow.select(1);
            });
            </script>

        </div>

  </div>
<!--XBLK_ENDX-->

    </div>

<!--XAD_STARTX-->

<!--XAD_ENDX-->

    <div class="part_01 clearfix">
        <div class="p_left">

          <!-- left begin -->
        <div class="blk_tit mb_10">
            <ol>
                <li class="selected "><a href="http://ent.sina.com.cn/" target="_blank">娱乐热点</a>·<a href="http://eladies.sina.com.cn/" target="_blank">时尚热点</a></li>
            </ol>
            <div class="tit_more"><a href="http://ent.sina.com.cn/" target="_blank">更多</a></div>
        </div>

            <div class="blk_13" id="blk_ylrd_01"  data-sudaclick="enthot_elahot">

        <div class="ct_p_160 clearfix">
<div class="ct_box"><a  href="http://slide.ent.sina.com.cn/star/slide_4_704_280474.html" target="_blank"><img  width="160" height="90" src="http://n.sinaimg.cn/ent/transform/250/w160h90/20180604/_6H6-hcmurvh2778716.jpg" /><span class="ct_txt">关晓彤穿短裙踢足球</span></a></div>

<div class="ct_box"><a  href="http://slide.ent.sina.com.cn/star/w/slide_4_704_280466.html" target="_blank"><img  width="160" height="90" src="http://n.sinaimg.cn/ent/transform/250/w160h90/20180604/1dB7-hcmurvh2784427.jpg" /><span class="ct_txt">袁弘张歆艺搞怪合照秀恩爱</span></a></div>        </div>
        <ul class="list_12 link_c666">
<li><a target="_blank" href="http://slide.ent.sina.com.cn/star/slide_4_704_280502.html">辣妈胡杏儿连体裤清新</a> <a target="_blank" href="http://slide.ent.sina.com.cn/y/k/slide_4_704_280499.html">宣美夏日写真秀长腿</a> <a target="_blank" href="http://slide.ent.sina.com.cn/star/slide_4_704_280471.html">沈月娇小可爱</a></li>

<li><a target="_blank" href="http://slide.ent.sina.com.cn/z/v/slide_4_704_280312.html">baby直发清纯可人</a>  <a target="_blank" href="http://slide.ent.sina.com.cn/z/v/slide_4_704_280309.html">网友法国偶遇赵薇舒淇</a> <a target="_blank" href="http://slide.ent.sina.com.cn/star/slide_4_704_280324.html">超模杜鹃长裙优雅</a></li>        </ul>

              <div class="line_01"></div>

<!-- publish_helper name='eladies_1_时尚热点_图文' p_id='1' t_id='923' d_id='1' -->
        <div class="ct_p_160 clearfix" id="blk_ylrd_012">
<!--t id="news_web_get_gspsdata" pid="1" tid="923" did="1" fid="sp_f23594" cname="时尚热点1"-->
			<div class="ct_box"><a  href="http://fashion.sina.com.cn/s/in/2018-06-01/1638/doc-ihcikcew2062503.shtml" target="_blank"><img  width="160" height="90" src="http://n.sinaimg.cn/fashion/transform/250/w160h90/20180604/WfLA-hcmurvh5690309.jpg" /><span class="ct_txt">Bella撞衫苹果保鲜膜</span></a></div><div class="ct_box"><a  href="http://slide.fashion.sina.com.cn/s/slide_24_84625_116799.html" target="_blank"><img  width="160" height="90" src="http://n.sinaimg.cn/fashion/250/w160h90/20180530/tPUq-hcffhsv5058206.jpg" /><span class="ct_txt">王凯封面大片自带神秘气息</span></a></div>        </div>

        <ul class="list_12 link_c666">
<!--t id="news_web_get_gspsdata" pid="1" tid="923" did="1" fid="sp_f23591" cname="时尚热点2"-->
			<li><a href="http://fashion.sina.com.cn/s/tr/2018-06-04/0748/doc-ihcikcew1255688.shtml" target="_blank">时髦保值的长青单品</a> <a href="http://fashion.sina.com.cn/b/mk/2018-06-04/0750/doc-ihcikcew1511454.shtml" target="_blank">王菊黑壮照样SLAY</a></li><li><a href="http://fashion.sina.com.cn/style/man/2018-06-04/0755/doc-ihcffhsu9510825.shtml" target="_blank">所有爆款都在山寨他</a> <a href="http://video.sina.com.cn/p/fashion/fas/doc/2018-06-01/174468680052.html" target="_blank">刘承羽最想演的角色是？</a></li>        </ul>

			</div>
          <!-- left end -->

          </div>
          <div class="p_middle">
          <!-- middle begin -->
        <div class="Tit_04" id="blk_lctycpup_01">
          <div class="t_name"><a href="http://ent.sina.com.cn/" target="_blank">娱乐</a><span class="dot">·</span><a href="http://sports.sina.com.cn" target="_blank">体育</a><span class="dot">·</span><a href="http://lottery.sina.com.cn/" target="_blank">彩票</a><span class="dot">·</span><a href="http://game.sina.com.cn/" target="_blank">游戏</a></div>
        </div>

            <!-- wapsinaENTSPORTS browser begin 勿删 -->


        <div class="blk_09" id="blk_lctycp_01">
          <ul class="list_14_noBg" id="blk_lctycp_011" data-client="p_ent"  data-sudaclick="ent_1">
            <!-- wap_sina_news_ent begin 勿删 -->
<li><a target="_blank" href="http://ent.sina.com.cn/m/c/2018-06-03/doc-ihcmurvh0824866.shtml">范冰冰工作室独家回应“阴阳合同”</a> <a target="_blank" href="http://ent.sina.com.cn/m/c/2018-06-03/doc-ihcmurvh1252336.shtml">崔永元向其道歉</a></li>

<li><a target="_blank" href="http://ent.sina.com.cn/s/m/2018-06-04/doc-ihcmurvh1539314.shtml">林允自曝花钱请摄影师拍机场照</a> <a target="_blank" href="http://ent.sina.com.cn/tv/zy/2018-06-04/doc-ihcmurvh1430863.shtml">颖儿发博力挺杨超越</a></li>

<li><a target="_blank" href="http://ent.sina.com.cn/s/m/2018-06-03/doc-ihcmurvh1163164.shtml">张一山宋妍霏被扒疑恋爱</a> <a target="_blank" href="http://ent.sina.com.cn/y/ygangtai/2018-06-04/doc-ihcmurvh1363169.shtml">李荣浩零点为女友杨丞琳庆生</a></li><li><a target="_blank" href="http://ent.sina.com.cn/y/ygangtai/2018-06-04/doc-ihcmurvh1381611.shtml">被黑粉攻击王嘉尔泪崩</a> <a target="_blank" href="http://ent.sina.com.cn/s/m/2018-06-03/doc-ihcmurvh1193273.shtml">迪丽热巴直播被粉丝说胖反应萌</a></li>

<li><a target="_blank" href="http://ent.sina.com.cn/photo/">图</a>:<a target="_blank" href="http://slide.ent.sina.com.cn/star/w/slide_4_704_280467.html">杨恭如身材曼妙</a>  <a target="_blank" href="http://slide.ent.sina.com.cn/star/w/slide_4_704_280464.html">张檬红唇显妖艳</a> <a target="_blank" href="http://slide.ent.sina.com.cn/star/w/slide_4_704_280468.html">高圆圆女神范十足</a></li>            <!-- wap_sina_news_ent end 勿删 -->


            <!-- wap_sina_news_sports begin 勿删 -->
<li class="dot"><a target="_blank" href="http://sports.sina.com.cn/nba/">NBA总决赛-库里飙进9三分勇士2-0骑士</a> <a target="_blank" href="http://sports.sina.com.cn/basketball/nba/2018-06-04/doc-ihcmurvh3285539.shtml">又破历史纪录</a></li>


<li><a target="_blank" href="http://sports.sina.com.cn/tennis/wta/2018-06-04/doc-ihcmurvh7776112.shtml">突发!小威宣布因伤退出法网</a> <a target="_blank" href="http://sports.sina.com.cn/tennis/atp/2018-06-04/doc-ihcmurvh7868207.shtml">纳达尔获生涯900胜进八强</a></li>

<li><a target="_blank" href="http://sports.sina.com.cn/g/2018worldcupeq/">热身-内马尔复出破门巴西2-0</a> <a target="_blank" href="http://sports.sina.com.cn/g/laliga/2018-06-04/doc-ihcmurvh1926950.shtml">曼城核心助攻西班牙1-1</a></li>




<li><a target="_blank" href="http://2018.sina.com.cn/ger/2018-06-04/doc-ihcmurvh6343673.shtml">德国队世界杯23人名单:萨内落选</a> <a target="_blank" href="http://sports.sina.com.cn/china/j/2018-06-04/doc-ihcmurvh5823974.shtml">比利时名单:中超2将</a></li>

<li><a target="_blank" href="http://sports.sina.com.cn/china/national/2018-06-04/doc-ihcmurvh7806541.shtml">热身-张玉宁破门U23国足4-2胜</a> <a target="_blank" href="http://sports.sina.com.cn/china/j/2018-06-04/doc-ihcmurvh4646597.shtml">关晓彤自曝是国安球迷</a></li><li><a target="_blank" href="http://lottery.sina.com.cn/">任性!老板3400万买彩中2千万</a> <a target="_blank" href="http://sports.sina.com.cn/l/2018-06-04/doc-ihcmurvh2252096.shtml">老伯29元中体彩3435万</a></li>            <!-- wap_sina_news_sports end 勿删 -->

<!--t id="news_web_get_gspsdata" pid="1" tid="930" did="9" fid="sp_f23791" cname="游戏1类内容"-->
			  <li class="dot"><a target="_blank" href="http://games.sina.com.cn/">宝可梦Let'sGO是全新系列</a> <a href="http://games.sina.com.cn/o/n/2018-06-04/hcmurvh3312337.shtml"target="_blank">进化将在9月3日关闭服务器</a></li>
<li><a href="http://games.sina.com.cn/o/n/2018-06-04/hcmurvh3291516.shtml" target="_blank">索尼正在开发《血源》和《地平线》新作 或在E3公布</a></li>

          </ul>
          <a href="javascript:void(0)" class="more_news" id="tab_lctycp_01">更多新闻&gt;</a>
        </div>


<!-- gsps娱乐·体育·彩票·游戏更多 p_id=1&t_id=908&f_id=23233 -->
<!-- id="news_web_get_gspsdata" pid="1" tid="908" did="29" fid="sp_f23233" cname="娱乐·体育·彩票·游戏"-->
			  <div class="blk_09" id="blk_lctycp_02" style="display:none;">
				  <a href="javascript:void(0)" class="more_news selected" id="tab_lctycp_02">返回&gt;&gt;</a>
			  </div>
            <!-- wapsinaENTSPORTS browser end 勿删 -->
            <script type="text/javascript" id="js_tab_5">
            jsLoader(ARTICLE_JSS.common,function(){
                var subshow = new SubShowClass('none','onclick');
                subshow.addLabel('tab_lctycp_02','blk_lctycp_01');
                subshow.addLabel('tab_lctycp_01','blk_lctycp_02');
            });
            </script>
          <!-- middle end -->
          </div>

<!--XBLK_STARTX-->
          <div class="p_right">
            <!-- right begin -->
            <div class="blk_12 h_360">
                <div class="blk_tit  mb_1">
                    <ol>
                        <li class=" selected" id="tab_gjdl_01" style="display:none;"><a href="http://sky.news.sina.com.cn/" target="_blank">航空</a></li>
                        <li id="tab_gjdl_02"><a href="http://gif.sina.com.cn/" target="_blank">GIF趣图</a></li>
                    </ol>
                </div>
				<div class="blk_main">


                <div id="blk_gjdl_02" class="blk_main_02" data-sudaclick="geo_1">

            <div class="b_cont">
              <div class="ct_p_05 clearfix" id="scrPic_gjdl_02">
<div class="ct_pic"><a  href="http://gif.sina.com.cn/" target="_blank"><img  data-src="http://f.sinaimg.cn/tech/573/w373h200/20180604/poFb-hcmurvh3089474.gif" width="260" height="170" /><span class="ct_txt">小孩知道自己的眉毛可以向上抬后</span></a></div>
<div class="ct_pic"><a  href="http://gif.sina.com.cn/" target="_blank"><img  data-src="http://n.sinaimg.cn/tech/625/w377h248/20180531/90ZN-hcikcev5302507.gif" width="260" height="170" /><span class="ct_txt">熊孩子挖蚌反被夹住爪子，哈哈好心疼！</span></a></div>
<div class="ct_pic"><a  href="http://gif.sina.com.cn/" target="_blank"><img  data-src="http://f.sinaimg.cn/tech/550/w350h200/20180530/Ahux-hcffhsv4136161.gif" width="260" height="170" /><span class="ct_txt">一家老少,其乐融融……</span></a></div>
<div class="ct_pic"><a  href="http://gif.sina.com.cn/" target="_blank"><img  data-src="http://n.sinaimg.cn/tech/750/w480h270/20180529/7L1W-hcffhsu8268899.gif" width="260" height="170" /><span class="ct_txt">瞧把它给吓的，竟都举手投降了</span></a></div>
              </div>
                <a href="javascript:void(0)" class="scrArrAbsLeft" id="scrArrLeft_gjdl_02"></a>
                <a href="javascript:void(0)" class="scrArrAbsRight" id="scrArrRight_gjdl_02"></a>
            </div>
            
            <div class="b_cons">
              <span class="scrDotList" id="scrDotList_gjdl_02">
                <span></span>
              </span>
            </div>
            
            <ul class="list_12 link_c666">
<li><a target="_blank" href="http://tech.sina.com.cn/d/s/2018-06-04/doc-ihcmurvh2592927.shtml">活跃冥王星：星球表面现固态甲烷形成的沙丘</a></li><li><a target="_blank" href="http://tech.sina.com.cn/d/2018-06-04/doc-ihcmurvh2464891.shtml">不令人想念！女宇航员揭秘空间站如厕系统</a></li>




<li><a target="_blank" href="http://tech.sina.com.cn/d/s/2018-06-04/doc-ihcmurvh2336074.shtml">SpaceX将推迟首次载人绕月球商业飞行计划</a></li>

<li><a target="_blank" href="http://tech.sina.com.cn/d/s/2018-06-04/doc-ihcmurvh2189725.shtml">“珞珈一号”试验卫星发射 用于夜光遥感</a></li>


<li><a target="_blank" href="http://slide.tech.sina.com.cn/d/slide_5_453_117032.html">神奇！南非水牛路见不平 顶飞狮子救下巨蜥</a></li>      </ul>

            <script type="text/javascript">
              jsLoader(ARTICLE_JSS.common,function(){
                  var focusScroll = new ScrollPic();
                  focusScroll.scrollContId  = "scrPic_gjdl_02"; //内容容器ID
            
                  focusScroll.dotListId   = "scrDotList_gjdl_02";//点列表ID
                  focusScroll.dotClassName  = "";//点className
                  focusScroll.dotOnClassName = "on";//当前点className
                  focusScroll.listType  = "";//列表类型(number:数字，其它为空)
                  focusScroll.listEvent = "onmouseover"; //切换事件
            
                  focusScroll.frameWidth  = 260;//显示框宽度
                  focusScroll.pageWidth = 260; //翻页宽度
                  focusScroll.upright = false; //垂直滚动
                  focusScroll.speed   = 10; //移动速度(单位毫秒，越小越快)
                  focusScroll.space   = 40; //每次移动像素(单位px，越大越快)
                  focusScroll.autoPlay  = false; //自动播放
                  focusScroll.autoPlayTime = 5; //自动播放间隔时间(秒)
                  focusScroll.circularly = true;
                  focusScroll.initialize(); //初始化
                  document.getElementById('scrArrLeft_gjdl_02').onmousedown = function(){
                    focusScroll.pre();
                    return false;
                  }
                  document.getElementById('scrArrRight_gjdl_02').onmousedown = function(){
                    focusScroll.next();
                    return false;
                  }
              });
            </script>
                </div>

					
				</div>
            </div>

  </div>

  <script type="text/javascript">
  	jsLoader(ARTICLE_JSS.common,function(){
		var subshow = new SubShowClass('none','onmouseover');
		//subshow.addLabel('tab_gjdl_01','blk_gjdl_01');
		subshow.addLabel('tab_gjdl_02','blk_gjdl_02');
		//subshow.random(1,1);
	});
  </script>

<!--XBLK_ENDX-->
    </div>

    <div class="part_01 clearfix">
    	<div class="p_left">


             <!--深度-->
			 <div class="blk_new_01 exclsv_hot">
				<div class="blk_tit">
					<ol>
						<li id="jiong_nav" class=" selected"><a href="http://news.sina.com.cn/zt_d/nextmedia" target="_blank">热点追踪</a></li>
					</ol>
<div class="tit_more"><a target="_blank" href="http://news.sina.com.cn/zt_d/nextmedia">更多</a></div>
				</div>                
                <div class="blk_main" data-sudaclick="blk_djrd">
					<div class="blk_jzy">
				        <ul class="exclsv_hot_ls">

<li>
	<h3 class="link_c333"><a href="http://news.sina.cn/zt_d/zgzy2018" target="_blank">收藏丨中国政要全阵容</a></h3>
		<div class="jzy_box clearfix">
			<div class="jzy_img"><a href="http://news.sina.cn/zt_d/zgzy2018" target="_blank"><img src="http://n.sinaimg.cn/news/transform/190/w110h80/20180320/sjqz-fyskeuc5449622.jpg"></a></div>
			<div class="jzy_txt"><p>新一届国家机构领导人已全部选出，这份名单值得收藏。 <a class="news_more" href="http://news.sina.cn/zt_d/zgzy2018" target="_blank">[详细]</a></p></div>
		</div>
</li>
<li>
	<h3 class="link_c333"><a href="http://news.sina.cn/zt_d/jianchawei2018" target="_blank">漫游国家监察委丨新浪新闻</a></h3>
		<div class="jzy_box clearfix">
			<div class="jzy_img"><a href="http://news.sina.cn/zt_d/jianchawei2018" target="_blank"><img src="http://n.sinaimg.cn/news/transform/190/w110h80/20180318/egif-fyshfur1284091.jpg"></a></div>
			<div class="jzy_txt"><p>以后在教科书看到的将不再是“一府两院”，而是“一府两院一委”。 <a class="news_more" href="http://news.sina.cn/zt_d/jianchawei2018" target="_blank">[详细]</a></p></div>
		</div>
</li>
<li>
	<h3 class="link_c333"><a href="http://news.sina.com.cn/z/zhihuijianwu2018" target="_blank">检察官的黑科技:无人机发现山林被掏空</a></h3>
		<div class="jzy_box clearfix">
			<div class="jzy_img"><a href="http://news.sina.com.cn/z/zhihuijianwu2018" target="_blank"><img src="http://n.sinaimg.cn/news/transform/190/w110h80/20180316/3ws4-fyshfuq0890678.png"></a></div>
			<div class="jzy_txt"><p>中国检察机关走过了“数字检务”“网络检务”“信息检务”阶段，现已升级进入“智慧检务”阶段。 <a class="news_more" href="http://news.sina.com.cn/z/zhihuijianwu2018" target="_blank">[详细]</a></p></div>
		</div>
</li>

						</ul>
					</div>
                </div>
            </div>
			<!--/深度-->




            <div>
<!--_SINA_ADS_BEGIN_-->
<!-- 340x120轮播要闻区左侧按钮广告 开始 -->
<div id="ad_05677"><script async charset="utf-8" src="//d3.sina.com.cn/litong/zhitou/sinaads/release/sinaads.js"></script><ins class="sinaads" data-ad-pdps="PDPS000000005677"></ins><script>(sinaads = window.sinaads || []).push({});</script></div>
<!-- 340x120轮播要闻区左侧按钮广告 结束 -->
<!--_SINA_ADS_END_-->
			</div>

			<div class="sp_h12"></div>

  		</div>

        <div class="p_middle">
  <!-- middle begin -->
<div class="Tit_04" id="blk_shup_01">
  <div class="t_name"><a href="http://news.sina.com.cn/society/" target="_blank">社会</a></div>
</div>

    <!-- wapsinaSTYLE browser begin 勿删 -->

<!-- gsps社会区块 p_id=1&t_id=912&f_id=28344 -->
			




<div class="blk_09" id="blk_sh_01">
    <!-- wap_sina_news_society begin 勿删 -->
  <ul class="list_14_noBg" id="blk_sh_011" data-client="p_society" data-sudaclick="news_sh_1">
<li class="dot topli14"><a href="http://news.sina.com.cn/society/" target="_blank">夫妻为躲债务协议假离婚 丈夫想复婚妻子却反悔</a></li><li><a href="http://news.sina.com.cn/s/wh/2018-06-04/doc-ihcmurvh6907594.shtml" target="_blank">10万中国小龙虾出征世界杯 俄罗斯吃货或“沦陷”</a></li><li><a href="http://news.sina.com.cn/c/2018-06-04/doc-ihcmurvh5419065.shtml" target="_blank">劫匪谈判时突然情绪激动伤害人质 狙击手开枪击毙</a></li><li><a href="http://news.sina.com.cn/s/2018-06-04/doc-ihcmurvh5045272.shtml" target="_blank">人贩子在湖北当街抢小孩子？事情比你想象复杂</a></li><li><a href="http://news.sina.com.cn/s/2018-06-04/doc-ihcmurvh4213153.shtml" target="_blank">中科大少年班：像天才的普通人</a></li><li><a href="http://news.sina.com.cn/s/2018-06-04/doc-ihcmurvh4101138.shtml" target="_blank">重庆高考女状元伦敦创业卖小面 价格超乎你想象</a></li><li><a href="http://news.sina.com.cn/o/2018-06-04/doc-ihcmurvh3837174.shtml" target="_blank">川航成都至海口航班起飞1小时返航 客服:公司原因</a></li><li><a href="http://news.sina.com.cn/s/2018-06-04/doc-ihcmurvh3321271.shtml" target="_blank">男子劫持人质不听劝阻伤害人质 被狙击手击毙</a></li><li><a href="http://news.sina.com.cn/s/2018-06-04/doc-ihcmurvh3193522.shtml" target="_blank">合同吓坏市场?华谊兄弟和范冰冰持股公司股价大跌</a></li><li><a href="http://news.sina.com.cn/s/2018-06-04/doc-ihcmurvh2853451.shtml" target="_blank">独子猝死生前欠巨款 老母亲7年坚持给人洗碗还债</a></li><li><a href="http://news.sina.com.cn/o/2018-06-04/doc-ihcmurvh2829266.shtml" target="_blank">A级通缉令嫌犯行凶致1死 案发前已背5条人命(图)</a></li><li><a href="http://news.sina.com.cn/o/2018-06-04/doc-ihcmurvh2700431.shtml" target="_blank">男子800元买报废轿车 用三轮车“驮”着飞奔(图)</a></li><li><a href="http://news.sina.com.cn/s/2018-06-04/doc-ihcmurvh2020447.shtml" target="_blank">女子8万买塑身内衣 6个月没穿出傲人身材要求退款</a></li><li><a href="http://news.sina.com.cn/s/2018-06-04/doc-ihcmurvh2212923.shtml" target="_blank">这名警察小姐姐火了：15秒视频点赞超过150万(图)</a></li>  </ul>
    <!-- wap_sina_news_society end 勿删 -->
  <!-- <a href="javascript:void(0)" class="more_news" id="tab_sh_01">更多新闻&gt;</a> -->
</div>

<div class="blk_09" id="blk_sh_02" style="display:none;">
  <ul class="list_14_noBg" id="blk_sh_012"  data-sudaclick="news_sh_1">
  </ul>
  <a href="javascript:void(0)" class="more_news" id="tab_sh_02">返回&gt;&gt;</a>
</div>

			
<!-- t id="news_web_get_gspsdata" pid="1" tid="912" did="1" fid="sp_f28344" cname="社会区块" -->

    <!-- wapsinaSTYLE browser end 勿删 -->
    <script type="text/javascript" id="js_tab_6">
     jsLoader(ARTICLE_JSS.common,function(){
          var subshow = new SubShowClass('none','onclick');
		 //subshow.addLabel('tab_sh_02','blk_sh_01');
		 //subshow.addLabel('tab_sh_01','blk_sh_02');
      });
    </script>

    <div class="blk_09">
<!-- gsps广告 -->
<!--t id="news_web_get_gspsdata" pid="1" tid="66" did="419" fid="sp_f1333" cname="广告" -->
		<!--新闻中心要闻区01文字位开始 淘宝测试-->
<ul class="list_14_noBg">
 <li class="dot">
   <ins class="sinaads" data-ad-pdps="PDPS000000002101" ></ins>
   <script>(sinaads = window.sinaads || []).push({});</script>
 </li>
</ul>

<ins class="sinaads" data-ad-pdps="PDPS000000000054" data-ad-width="360" data-ad-height="144" data-ad-type="embed"></ins>
<script>(sinaads = window.sinaads || []).push({});</script>
<!-- sp_f1333 end -->
	</div>

  <!-- wapnewsfirsttype browser end 勿删 -->
  <!-- middle end -->
  </div>

<!--XBLK_STARTX-->
        <div class="p_right">

            <div class="blk_tit mb_1">
                <ol>
                    <li class="selected " id="tab_gy_01"><a href="http://gongyi.sina.com.cn/" target="_blank">公益</a></li>
					<li class="" id="tab_gy_02"><a href="http://green.sina.com.cn/" target="_blank">环保</a></li>
                </ol>
            </div>

<!-- gsps公益·环保区块 p_id=1&t_id=912&f_id=28345 -->
<!--t id="news_web_get_gspsdata" pid="1" tid="912" did="1" fid="sp_f28345" cname="公益·环保区块"-->
<div id="blk_gy_01" class="blk_260 blk_08"  data-sudaclick="gongyi_1" style="overflow:hidden;">
	<div class="b_cont" style="padding:0;width:260px; ">
	<div class="ct_p_05 clearfix" id="scrPic_gjdl_01_gy" style="padding-top:4px;">
		<div class="ct_pic"><a href="http://weibo.com/p/1008087a827114204fb26dc5b8d32805dc7b76" target="_blank"><img src="http://www.sinaimg.cn/dy/temp/924/2014/0212/U7063P1T924D2F23610DT20161115092138.jpg" width="260" height="170" alt="#中华环境奖#环保领域最高奖项" /><span class="ct_txt">#中华环境奖#环保领域最高奖项</span></a></div><div class="ct_pic"><a href="http://weibo.com/p/100808d2eed5a727b3c139e1e5ce3621c2f8e0" target="_blank"><img src="http://www.sinaimg.cn/dy/temp/924/2014/0212/U2390P1T924D2F23611DT20161202163436.png" width="260" height="170" alt="#中国公益新媒体沙龙#" /><span class="ct_txt">#中国公益新媒体沙龙#</span></a></div><div class="ct_pic"><a href="http://gongyi.sina.com.cn/2017-05-27/doc-ifyfqvmh9244280.shtml" target="_blank"><img src="http://www.sinaimg.cn/dy/temp/924/2014/0212/U263P1T924D2F23613DT20170601095333.jpg" width="260" height="170" alt="第七届“SEE生态奖”" /><span class="ct_txt">第七届“SEE生态奖”</span></a></div>	</div>
	<a href="javascript:void(0)" class="scrArrAbsLeft" id="scrArrLeft_gjdl_01_gy"></a>
	<a href="javascript:void(0)" class="scrArrAbsRight" id="scrArrRight_gjdl_01_gy"></a>
</div>

<div class="b_cons" style="padding:0;">
	<span class="scrDotList" id="scrDotList_gjdl_01_gy">
		<span></span>
	</span>
</div>

<ul class="list_12 link_c666" style="padding-bottom:6px;margin-top:-8px;">
	<li><strong>[</strong><a href="http://gongyi.sina.com.cn/gyzx/hg.html" target="_blank">焦点</a><strong>]</strong> <a href="http://gongyi.sina.com.cn/2017-05-27/doc-ifyfqvmh9244280.shtml" target="_blank">第七届“SEE生态奖”再启动</a></li>
                <li><strong>[</strong><a href="http://gongyi.sina.com.cn/gyzx.html" target="_blank">资讯</a><strong>]</strong> <a href="http://gongyi.sina.com.cn/greenlife/2017-05-23/doc-ifyfkqiv6684495.shtml" target="_blank">“爱每一天”全球可持续发展新媒体展</a></li></ul>
</div>

<!-- by cheny 2013-01-23 start -->
<script type="text/javascript">
	jsLoader(ARTICLE_JSS.common,function(){
		var focusScroll = new ScrollPic();
		focusScroll.scrollContId  = "scrPic_gjdl_01_gy"; //内容容器ID

		focusScroll.dotListId   = "scrDotList_gjdl_01_gy";//点列表ID
		focusScroll.dotClassName  = "";//点className
		focusScroll.dotOnClassName = "on";//当前点className
		focusScroll.listType  = "";//列表类型(number:数字，其它为空)
		focusScroll.listEvent = "onmouseover"; //切换事件

		focusScroll.frameWidth  = 260;//显示框宽度
		focusScroll.pageWidth = 260; //翻页宽度
		focusScroll.upright = false; //垂直滚动
		focusScroll.speed   = 10; //移动速度(单位毫秒，越小越快)
		focusScroll.space   = 40; //每次移动像素(单位px，越大越快)
		focusScroll.autoPlay  = false; //自动播放
		focusScroll.autoPlayTime = 5; //自动播放间隔时间(秒)
		focusScroll.circularly = true;
		focusScroll.initialize(); //初始化
		document.getElementById('scrArrLeft_gjdl_01_gy').onmousedown = function(){
			focusScroll.pre();
			return false;
		}
		document.getElementById('scrArrRight_gjdl_01_gy').onmousedown = function(){
			focusScroll.next();
			return false;
		}
	});
</script>
<!-- by cheny 2013-01-23 end -->


<div id="blk_gy_02" class="blk_260 blk_08"  data-sudaclick="green_1" style="overflow:hidden;">
	<div class="b_cont" style="padding:0;width:260px; ">
	<div class="ct_p_05 clearfix" id="scrPic_gjdl_01_hb" style="padding-top:4px;">
		<div class="ct_pic"><a href="http://news.sina.com.cn/green/roll/2016-02-24/doc-ifxprucu3182698.shtml" target="_blank"><img src="http://www.sinaimg.cn/dy/2016/0224/U1987P1DT20160224153827.jpg" width="260" height="170" alt="黎巴嫩遭“垃圾围城”" /><span class="ct_txt">黎巴嫩遭“垃圾围城”</span></a></div>	</div>
	<a href="javascript:void(0)" class="scrArrAbsLeft" id="scrArrLeft_gjdl_01_hb"></a>
	<a href="javascript:void(0)" class="scrArrAbsRight" id="scrArrRight_gjdl_01_hb"></a>
</div>

<div class="b_cons" style="padding:0;">
	<span class="scrDotList" id="scrDotList_gjdl_01_hb">
		<span></span>
	</span>
</div>

<ul class="list_12 link_c666" style="padding-bottom:6px;margin-top:-8px;">
	<li><strong>[</strong><a href="http://green.sina.com.cn/" target="_blank">焦点</a><strong>]</strong> <a href="http://news.sina.com.cn/green/pl/2016-02-24/doc-ifxprucu3182865.shtml" target="_blank" class="linkRed">最严“禁燃令”折射治理新思路</a></li>

<li><strong>[</strong><a href="http://green.sina.com.cn/" target="_blank">关注</a><strong>]</strong> <a href="http://news.sina.com.cn/green/roll/2016-02-24/doc-ifxprucs6459018.shtml" target="_blank" class="linkRed">臭氧成珠三角大气污染“元凶”</a></li></ul>
</div>

<!-- by cheny 2013-01-23 start -->
<script type="text/javascript">
	jsLoader(ARTICLE_JSS.common,function(){
		var focusScroll = new ScrollPic();
		focusScroll.scrollContId  = "scrPic_gjdl_01_hb"; //内容容器ID

		focusScroll.dotListId   = "scrDotList_gjdl_01_hb";//点列表ID
		focusScroll.dotClassName  = "";//点className
		focusScroll.dotOnClassName = "on";//当前点className
		focusScroll.listType  = "";//列表类型(number:数字，其它为空)
		focusScroll.listEvent = "onmouseover"; //切换事件

		focusScroll.frameWidth  = 260;//显示框宽度
		focusScroll.pageWidth = 260; //翻页宽度
		focusScroll.upright = false; //垂直滚动
		focusScroll.speed   = 10; //移动速度(单位毫秒，越小越快)
		focusScroll.space   = 40; //每次移动像素(单位px，越大越快)
		focusScroll.autoPlay  = false; //自动播放
		focusScroll.autoPlayTime = 5; //自动播放间隔时间(秒)
		focusScroll.circularly = true;
		focusScroll.initialize(); //初始化
		document.getElementById('scrArrLeft_gjdl_01_hb').onmousedown = function(){
			focusScroll.pre();
			return false;
		}
		document.getElementById('scrArrRight_gjdl_01_hb').onmousedown = function(){
			focusScroll.next();
			return false;
		}
	});
</script>
<!-- by cheny 2013-01-23 end -->
            <script type="text/javascript" id="js_tab_1">
            jsLoader(ARTICLE_JSS.common,function(){
                var subshow = new SubShowClass('none','onmouseover');
                subshow.addLabel('tab_gy_01','blk_gy_01');
                subshow.addLabel('tab_gy_02','blk_gy_02');
            });
            </script>





			<!--天气预报-->
			<div class="blk_tit">
			  <ol>
				<li class="selected "><a href="http://weather.sina.com.cn/" target="_blank">天气预报</a></li>
			  </ol>
			  <div class="tit_more" style="width:90px;"><a target="_blank" href="http://weather.sina.com.cn/">查询各地天气</a></div>
			</div>
            <script type="text/javascript" src="//int.dpool.sina.com.cn/iplookup/iplookup.php?format=js"></script>
			<script type="text/javascript">

              function _jsonp(url, callbackName, callback) {
            if (!url) {
                return
            }
            if (url.indexOf('?') === -1) {
                url += '?callback='
            } else {
                url += '&callback='
            }
            url += callbackName;
            var script = document.createElement('script');
            window[callbackName] = function(data) {
                callback && callback(data)
            }
            script.src = url;
            document.getElementsByTagName('head')[0].appendChild(script)
        }

        var h = 0;
        var b = 3000;
        var c = "//open.weather.sina.com.cn/api/weather/sinaForecast?";

        if(remote_ip_info.city){remote_ip_info.city = remote_ip_info.city;}
        else{remote_ip_info.city = "北京";}

        var e = {
            city: remote_ip_info.city,
            cityEn: encodeURIComponent( remote_ip_info.city ) 
        };

        window.homeWeatherWarnFun = function(data) {
            if (data && data.result.data && data.result.data.length > 0) {
                var warnImg = '<img width="36" height="23" src="'+ data.result.data[0] +'" />';
                document.getElementById("wth_warn").innerHTML = warnImg;
            }
        };

        var a = function(r) {
            var q = false;
            if (r && r.result.data) {
                var rdata = r.result.data,
				wthTime = rdata.days.day[0].forecast_date;
                if (rdata.days && rdata.info) {
                    var showCity = e.city;
                    if(e.city.length >= 4){
                        showCity = e.city.substring(0,3) +"..."
                    }

                    var showTemperature = "";
                    var showImg = "";
                    var showType = "";
					var showType2 = "";
					var windType = "";

                    if( rdata.days.day[0].day_temperature && rdata.days.day[0].day_temperature !=="" && rdata.days.day[0].day_temperature !=="\0" ){
                        showTemperature = rdata.days.day[0].day_temperature;
                        showImg = "http://i3.sinaimg.cn/dy/weather/main/index14/007/icons_128_yl/"+rdata.days.day[0].day_weather_code+".png";
                        showType = rdata.days.day[0].day_weather_type;
						windType = rdata.days.day[0].day_wind_type +"  " +rdata.days.day[0].day_wind_power;
                    } else {
                        showTemperature = rdata.days.day[0].night_temperature;
                        showImg = "http://i3.sinaimg.cn/dy/weather/main/index14/007/icons_128_yl/"+rdata.days.day[0].night_weather_code+".png";
                        showType = rdata.days.day[0].night_weather_type;
						windType = rdata.days.day[0].night_wind_type +"  " +rdata.days.day[0].night_wind_power;
                    }

                    var finalImg = '<img width="70" height="68" src="'+ showImg +'" title="'+showType+'" />';

                    var isIE6= !!window.ActiveXObject&&!window.XMLHttpRequest;
                    if(isIE6)
                    {
                        var imgTitle = "title='" + showType +"'";
                        var strNewHTML = "<span " + imgTitle
                        + " style=\"" + "display:block;width:70px; height:68px; cursor:pointer; filter:progid:DXImageTransform.Microsoft.AlphaImageLoader"
                        + "(src=\'" + showImg + "\', sizingMethod='scale');\"></span>";
                        finalImg = strNewHTML;
                    }
					var wthAqi = rdata.air.aqi=='' || typeof(rdata.air.aqi) == "undefined" ? '' : rdata.air.aqi,
					wthInfo = rdata.air.description  == '' || typeof(rdata.air.description) == "undefined" ? '' : '(' + rdata.air.description + ')',
					wthair = wthAqi == '' ? windType : '空气质量：<span>'+wthAqi+'</span><span>'+wthInfo+'</span>';
					showType2 = showType.length > 8 ? showType.substring(0,7) +"..." : showType;
					var weahtml = '<div class="wtop clearfix"><span class="wth_city">%showCity%</span><span class="wth_time">%wthTime%</span></div>';
					weahtml += '<div class="b_p0"><span class="wth_img" style="cursor:pointer;">%finalImg%<span class="wth_des">%showType2%</span></span></div>';
					weahtml += '<div class="b_p1"><div class="wmid"><span class="wth_info">%showTemperature%℃</span><span id="wth_warn" style="display:none;"></span></div><p>%wthair%</p></div>';
				    weahtml = weahtml.replace(/%showType2%/g,showType2).replace(/%finalImg%/g,finalImg).replace(/%showCity%/g,showCity).replace(/%wthTime%/g,wthTime).replace(/%showTemperature%/g,showTemperature).replace(/%wthair%/g,wthair);
                    var wea = document.getElementById("wea");
					wea.innerHTML = weahtml;
					var clickO = document.getElementById("blk_jrtq_01");
		             clickO.onclick = function(){
		                window.open('http://weather.sina.com.cn/'+rdata.info.url_code)}
				} else {
                    q = true
                }
                _jsonp(["//open.weather.sina.com.cn/api/weather/warn_pic/?",['city='+e.cityEn].join("&")].join(""),"homeWeatherWarnFun__",function(data){
                    homeWeatherWarnFun(data);
                })
            } else {
                q = true
            }
        };

        window.homeWeatherRenderFun = function(p) {
            a(p)
        };
        _jsonp([c,['length=1','air=1','city='+e.cityEn].join("&")].join(""),"homeWeatherRenderFunNew__",function(data){
                homeWeatherRenderFun(data);
        }) 

</script>
			<div class="blk_16 clearfix tdy_weather" id="blk_jrtq_01" data-sudaclick="blk_weather">
			  <div class="b_cont" id="wea">
			  </div>
			</div>




			<div class="pageReview" id="blk_syhg_01" style="z-index:1">
  <h4>首页回顾</h4>
  <form name="pageReview" onsubmit="return false">
    <select name="channel" class="pr_ch">
      <option value="www">首页</option>
      <option value="news" selected="selected">新闻</option>
      <option value="sports">体育</option>
      <option value="tech">科技</option>
      <option value="finance">财经</option>
      <option value="ent">娱乐</option>
      <option value="auto">汽车</option>
    </select>
    <input type="text" readonly class="pr_date" name="date" value="载入中,请稍候..." />
    <select name="time" class="pr_time">
      <option value="am" selected="selected">9:00</option>
      <option value="pm">21:00</option>
    </select>
  </form>
  <div class="dateView" id="dataView"></div>
</div>

			<script type="text/javascript">
              jsLoader(ARTICLE_JSS.common,function(){
                  //回顾
                  var review = new DateView('dataView');
                  review.startDate = '2002-01-01';
                  review.init();
                  var addEvent = function(obj,eventType,func){if(obj.attachEvent){obj.attachEvent("on"+eventType,func)}else{obj.addEventListener(eventType,func,false)}};
                  var delEvent = function(obj,eventType,func){if(obj.detachEvent){obj.detachEvent("on"+eventType,func)}else{obj.removeEventListener(eventType,func,false)}};
                  var state = 'close';
                  var ch = document.pageReview.channel;
                  var time = document.pageReview.time;

                  document.pageReview.date.value = '点击选择日期';
                  document.pageReview.date.onclick = function(){
                    if(state == 'close'){
                      open();
                    }else{
                      close();
                    }
                  };
                  function chkShow(e){
                    e = e || event;
                    ele = e.target || e.srcElement;
                    do{
                      if(ele == document.pageReview || ele == review.__ele){return} //点击在回顾区域
                      ele = ele.parentNode;
                    }while(ele != document.body & ele != document.documentElement);
                    close();
                  };
                  function close(){
                    review.__ele.style.display = 'none';
                    delEvent(document.body,'mousedown',chkShow);
                    state = 'close';
                  };
                  function open(){
                    review.__ele.style.display = 'block';
                    addEvent(document.body,'mousedown',chkShow);
                    state = 'open';
                  }

                  review.onclick = function(year, month, day){
                    var url;
                    //url规则
                    switch(ch.value){
                      case 'www':
                        url = 'http://www.sina.com.cn/head/www{$year}{$month}{$day}{$time}.shtml';
                        break;
                      case 'news':
                        url = 'http://news.sina.com.cn/head/news{$year}{$month}{$day}{$time}.shtml';
                        break;
                      case 'sports':
                        url = 'http://sports.sina.com.cn/head/sports{$year}{$month}{$day}{$time}.shtml';
                        break;
                      case 'finance':
                        url = 'http://finance.sina.com.cn/head/finance{$year}{$month}{$day}{$time}.shtml';
                        break;
                      case 'tech':
                        url = 'http://tech.sina.com.cn/head/tech{$year}{$month}{$day}{$time}.shtml';
                        break;
                      case 'ent':

                        url = 'http://ent.sina.com.cn/head/ent{$year}{$month}{$day}{$time}.shtml';
                        break;
                      case 'auto':
                        url = 'http://auto.sina.com.cn/head/auto{$year}{$month}{$day}{$time}.shtml';
                        break;
                    };
                    if(!url){return}
                    if(String(month).length < 2){month = '0' + month}
                    if(String(day).length < 2){day = '0' + day}
                    url = url.replace(/\{\$year\}/g,year).replace(/\{\$month\}/g,month).replace(/\{\$day\}/g,day).replace(/\{\$time\}/g,time.value);
                    window.open(url);
                    close();
                  };

              });
            </script>

  		</div>
<!--XBLK_ENDX-->
    </div>

<!-- AD tl02 begin -->
<!--XAD_STARTX-->
<!--_SINA_ADS_BEGIN_-->
<div><!-- 1000x90轮播通栏02广告 开始 -->
<div id="ad_47211">
  <script async charset="utf-8" src="//d5.sina.com.cn/litong/zhitou/sinaads/release/sinaads.js"></script><ins class="sinaads" data-ad-pdps="PDPS000000058103"></ins><script>(sinaads = window.sinaads || []).push({});</script>
</div></div>
<!--_SINA_ADS_END_-->
<!--XAD_ENDX-->
<!-- AD tl02 end -->

    <div class="partTit_01" id="blk_gntltop_01" data-sudaclick="gn2_tb">
<!-- publish_helper name='news_34_国内二类_栏目条' p_id='1' t_id='908' d_id='34' -->
      <div class="pT_name"><a href="http://news.sina.com.cn/china/" target="_blank" class="titName ptn_26">国内新闻</a></div>
      <div class="pT_links">[<a href="http://news.sina.com.cn/area/" target="_blank">各地新闻</a> | <a href="http://roll.news.sina.com.cn/news/gnxw/zs-pl/index.shtml" target="_blank">综述</a>·<a href="http://news.sina.com.cn/opinion/" target="_blank">评论</a>]</div>
      <div class="pT_more"><a href="http://news.sina.com.cn/zt/col_china/" target="_blank">国内新闻专题</a> | <a href="http://slide.news.sina.com.cn/c/" target="_blank">新闻图片</a> &nbsp;&nbsp&nbsp;&nbsp;<a href="http://news.sina.com.cn/china/" target="_blank">更多&gt;</a></div>
    </div>

    <div class="part_02 pt_8 clearfix">
    	<div class="p_left">
            <div class="blk_new_03">
                <div class="blk_nav_2"><a class="blk_nav_tit" href="http://news.sina.com.cn/hotnews/#2" target="_blank">国内新闻每日排行</a> <div class="tit_more"><a href="http://news.sina.com.cn/hotnews/#2" target="_blank">更多</a></div></div>
                <div class="blk_content">
                    <div class="blk_content_1" tab-type="tab-cont">
                        <div class="blk_content_box" tab-type="tab-wrap" >
                            <div class="blk_content_tit">
                                <ol>
                                    <li tab-type="tab-nav" class="selected">今天</li>
                                    <li tab-type="tab-nav">昨天</li>
                                    <li tab-type="tab-nav">一周</li>
                                </ol>
                            </div>
                            <div class="blk_content_list" tab-type="tab-cont">
                                <ul id="gn_list_01" data-sudaclick="gn_hotnews1">

                                </ul>
                            </div>
                            <div class="blk_content_list" tab-type="tab-cont" style="display:none;">
                                <ul id="gn_list_02" data-sudaclick="gn_hotnews2">

                                </ul>
                            </div>
                            <div class="blk_content_list" tab-type="tab-cont" style="display:none;">
                                <ul id="gn_list_03" data-sudaclick="gn_hotnews3">

                                </ul>
                            </div>
                        </div>
                     </div>

                    <div class="blk_content_2" tab-type="tab-cont">

                    </div>
                </div>

                <div style="height:10px;"></div>
				
<div class="blk_nav_2" style="margin-bottom: 9px;"><a class="blk_nav_tit" href="http://e.sina.com.cn/" target="_blank">新浪扶翼</a></div>
<ins class="sinaads" data-ad-pdps="PDPS000000058288"></ins><script>(sinaads = window.sinaads || []).push({});</script>
				
				
<!--
                <div>
id="news_web_index_v2015_adpic_3"
				</div>
-->
				
<!-- 文字商讯 -->
<!--_SINA_ADS_BEGIN_-->

<!--_SINA_ADS_END_-->

<!-- 新浪智投 -->
<!--_SINA_ADS_BEGIN_-->
				
<!--_SINA_ADS_END_-->

<!--ipad版替换位01-->

            </div>
        </div>

        <div class="p_middle">
          <!-- middle begin -->

<!-- 国内通栏-列表 -->
		
		<!-- 内地新闻 -->
        <div class="blk_09" id="blk_ndxw_01" data-sudaclick="gn2_list_01">
 			<ul class="list_14">
				<li><a href="http://news.sina.com.cn/c/nd/2018-06-04/doc-ihcmurvh7806542.shtml" target="_blank" >国家药监局决定对201家药企逐一开展现场检查</a><span class="time"> 21:36</span></li>			<li><a href="http://news.sina.com.cn/c/gat/2018-06-04/doc-ihcmurvh7861208.shtml" target="_blank" >台“汉光演习”近10年4起意外 坠机又翻车9死11伤</a><span class="time"> 21:34</span></li>			<li><a href="http://news.sina.com.cn/o/2018-06-04/doc-ihcmurvh7739215.shtml" target="_blank" >全国31省份公布高考举报电话 有的24小时接听</a><span class="time"> 21:23</span></li>			<li><a href="http://news.sina.com.cn/c/gat/2018-06-04/doc-ihcmurvh7670956.shtml" target="_blank" >发动机轴承断裂?台F16不排除空中解体 已用20多年</a><span class="time"> 21:07</span></li>			<li><a href="http://news.sina.com.cn/c/zj/2018-06-04/doc-ihcmurvh7583126.shtml" target="_blank" >《保险实名登记管理办法(征求意见稿)》征求意见</a><span class="time"> 20:58</span></li>			<li><a href="http://news.sina.com.cn/o/2018-06-04/doc-ihcmurvh7365411.shtml" target="_blank" >湖北警方一个月侦破破坏长江生态案65起 抓逾百人</a><span class="time"> 20:19</span></li>			<li><a href="http://news.sina.com.cn/c/nd/2018-06-04/doc-ihcmurvh7146190.shtml" target="_blank" >保姆放火案当事消防员:5点04分有报警 11分到小区</a><span class="time"> 19:52</span></li>
	</ul><div class="line_01"></div>	<ul class="list_14">
				<li><a href="http://news.sina.com.cn/c/nd/2018-06-04/doc-ihcmurvh7135301.shtml" target="_blank" >王毅：当今世界存在三个方面的赤字问题</a><span class="time"> 19:51</span></li>			<li><a href="http://news.sina.com.cn/o/2018-06-04/doc-ihcmurvh7202166.shtml" target="_blank" >李贻伟任广东省惠州市委书记 陈奕威另有任用</a><span class="time"> 19:46</span></li>			<li><a href="http://news.sina.com.cn/c/nd/2018-06-04/doc-ihcmurvh7107332.shtml" target="_blank" >青海玉树州杂多县发生3.1级地震 震源深度8千米</a><span class="time"> 19:45</span></li>			<li><a href="http://news.sina.com.cn/c/gat/2018-06-04/doc-ihcmurvh7093392.shtml" target="_blank" >台军方证实：坠机F-16飞行员已死亡 暂停搜索</a><span class="time"> 19:40</span></li>			<li><a href="http://news.sina.com.cn/c/2018-06-04/doc-ihcmurvh7082679.shtml" target="_blank" >陕西司法厅：全面自查今年的商品房销售摇号公证</a><span class="time"> 19:38</span></li>			<li><a href="http://news.sina.com.cn/o/2018-06-04/doc-ihcmurvh7234052.shtml" target="_blank" >陈爱军任安徽安庆市委副书记(图/简历)</a><span class="time"> 19:36</span></li>			<li><a href="http://news.sina.com.cn/c/2018-06-04/doc-ihcmurvh7055520.shtml" target="_blank" >外交部:中国公民暂勿前往以色列与加沙边境及附近</a><span class="time"> 19:30</span></li>
	</ul><div class="line_01"></div>	<ul class="list_14">
				<li><a href="http://news.sina.com.cn/c/2018-06-04/doc-ihcmurvh7034637.shtml" target="_blank" >山东通报4起诬告陷害诽谤党员干部典型问题</a><span class="time"> 19:30</span></li>			<li><a href="http://news.sina.com.cn/o/2018-06-04/doc-ihcmurvh7017027.shtml" target="_blank" >乐视网：历史上存在与贾跃亭资产财务不独立情况</a><span class="time"> 19:28</span></li>			<li><a href="http://news.sina.com.cn/c/2018-06-04/doc-ihcmurvh7359929.shtml" target="_blank" >崔永元：我针对的是刘震云和冯小刚</a><span class="time"> 19:05</span></li>			<li><a href="http://news.sina.com.cn/c/nd/2018-06-04/doc-ihcmurvh6862976.shtml" target="_blank" >崔永元被实名认证试飞员死亡威胁？空军：已退役</a><span class="time"> 19:02</span></li>			<li><a href="http://news.sina.com.cn/c/nd/2018-06-04/doc-ihcmurvh6848669.shtml" target="_blank" >环球时报社评：汉光军演已经堕落成一种政治仪式</a><span class="time"> 18:59</span></li>			<li><a href="http://news.sina.com.cn/o/2018-06-04/doc-ihcmurvh6750188.shtml" target="_blank" >少林寺宣布将重拍《少林寺》 全新改编耗资超两亿</a><span class="time"> 18:46</span></li>			<li><a href="http://news.sina.com.cn/o/2018-06-04/doc-ihcmurvh6828736.shtml" target="_blank" >组小学队与国乒拼未来 日主帅：靠雕虫小技赢不了</a><span class="time"> 18:36</span></li>
	</ul><div class="line_01"></div>	<ul class="list_14">
				<li><a href="http://news.sina.com.cn/c/nd/2018-06-04/doc-ihcmurvh6654551.shtml" target="_blank" >四川侦破特大制贩毒案 摧毁跨省制贩毒通道</a><span class="time"> 18:29</span></li>			<li><a href="http://news.sina.com.cn/o/2018-06-04/doc-ihcmurvh6506251.shtml" target="_blank" >“保姆放火案”被害人林生斌:终于等到想要的结果</a><span class="time"> 18:05</span></li>			<li><a href="http://news.sina.com.cn/o/2018-06-04/doc-ihcmurvh6503290.shtml" target="_blank" >科技部党组发一号文:国家科技咨询委员会呼之欲出</a><span class="time"> 18:03</span></li>			<li><a href="http://news.sina.com.cn/c/gat/2018-06-04/doc-ihcmurvh6476660.shtml" target="_blank" >台军确认失联F-16已坠毁 飞行员目前生死不明</a><span class="time"> 17:59</span></li>		<li><ins class="sinaads" data-ad-pdps="PDPS000000057504"></ins>
        <script>(sinaads = window.sinaads || []).push({});</script></li>
	</ul>        </div>
        
        

          <!-- middle end -->
          </div>


<!--XBLK_STARTX-->
        <div class="p_right">
        	<!--图片模块-->
			<div class="new_pics" id="new_pics">
           		<div class="blk_nav_3">
                	<a target="_blank" href="http://photo.sina.com.cn/" class="blk_nav_tit">图片</a><div class="tit_more"><a target="_blank" href="http://photo.sina.com.cn/">更多</a></div>
                </div>
                <ul class="new_pic_lst">
                	<li data-sudaclick="blk_photo_wit">
                    	<h3 class="new_pic_tit"><a href="http://photo.sina.com.cn/wit/" target="_blank">看见</a></h3>

                        <div class="new_pic_box">
                        	<a href="http://slide.news.sina.com.cn/z/slide_1_64237_278581.html" target="_blank" class="zt_pic_w"><img src="http://n.sinaimg.cn/news/transform/434/w260h174/20180531/KDAW-hcikcev3315736.jpg" width="260" height="174"><span class="ct_txt">曾经的杀马特教父现在咋样了？</span></a>
                        </div>

                    </li>
                    <li data-sudaclick="blk_photo_mortal">
                    	<h3 class="new_pic_tit"><a href="http://photo.sina.com.cn/newyouth" target="_blank">新青年</a></h3>

                        <div class="new_pic_box">
                        	<a href="http://photo.sina.com.cn/newyouth/doc-ihcffhsv2772708.shtml" target="_blank" class="zt_pic_w"><img src="http://n.sinaimg.cn/photo/500/w300h200/20180529/bGPB-hcffhsv2761031.jpg" width="260" height="174"><span class="ct_txt">20岁技校女孩凭这门手艺成为世界冠军</span></a>
                        </div>

                    </li>
                    <li data-sudaclick="blk_photo_hist">
                    	<h3 class="new_pic_tit"><a href="http://photo.sina.com.cn/ygdbns" target="_blank">一个都不能少</a></h3>

                        <div class="new_pic_box">
                        	<a href="http://slide.news.sina.com.cn/slide_1_89251_278101.html" target="_blank" class="zt_pic_w"><img src="http://n.sinaimg.cn/news/1_img/upload/299fd2ed/783/w950h633/20180529/PaE9-hcffhsv0542137.png" width="260" height="174"><span class="ct_txt">一个都不能少：川妹子离开上海回大…</span></a>
                        </div>

                    </li>

                </ul>
           </div>
		   <!--/图片模块-->
        </div>
<!--XBLK_ENDX-->


    </div>

<!-- iplookup 检查地域 begin -->
<script type="text/javascript">
  Function.prototype.Bind=function(){var __m=this,object=arguments[0],args=new Array;for(var i=1;i<arguments.length;i++){args.push(arguments[i]);}return function(){return __m.apply(object,args);};};var isIE=false;var userAgent=navigator.userAgent.toLowerCase();if(userAgent.indexOf("msie")!=-1&&userAgent.indexOf("opera")==-1){isIE=true;}if(typeof IO=="undefined"){IO={};}IO.Script=function(){this.Init.apply(this,arguments);};IO.Script.prototype={_scriptCharset:"utf-8",_oScript:null,Init:function(opts){this._setOptions(opts);},_setOptions:function(opts){if(typeof opts!="undefined"){if(opts.script_charset){this._scriptCharset=opts.script_charset;}}},_clearScriptObj:function(){if(this._oScript){try{this._oScript.onload=null;if(this._oScript.onreadystatechange){this._oScript.onreadystatechange=null;}this._oScript.parentNode.removeChild(this._oScript);}catch(e){}}},_callbackWrapper:function(callback){if(this._oScript.onreadystatechange){if(this._oScript.readyState!="loaded"&&this._oScript.readyState!="complete"){return;}}if(typeof callback!="undefined"){callback();}this._clearScriptObj();},load:function(url,callback){this._oScript=document.createElement("SCRIPT");this._oScript.type="text/javascript";if(isIE){this._oScript.onreadystatechange=this._callbackWrapper.Bind(this,callback);}else{this._oScript.onload=this._callbackWrapper.Bind(this,callback);}this._oScript.charset=this._scriptCharset;this._oScript.src=url;document.getElementsByTagName("head")[0].appendChild(this._oScript);}};

  if (remote_ip_info.ret==1) {
    switch (remote_ip_info.province) {

      case '安徽' : (new IO.Script).load("http://ah.sina.com.cn/newscenter/ah.js");
        break;

      case '江苏' : (new IO.Script).load("http://jiangsu.sina.com.cn/newscenter/jiangsu.js");
        break;

      case '河北' : (new IO.Script).load("http://hebei.sina.com.cn/newscenter/hebei.js");
        break;

      case '辽宁' : (new IO.Script).load("http://ln.sina.com.cn/newscenter/ln.js");
        break;

      case '陕西' : (new IO.Script).load("http://sx.sina.com.cn/newscenter/sx.js");
        break;

      case '黑龙江' : (new IO.Script).load("http://hlj.sina.com.cn/newscenter/hlj.js");
        break;

      case '湖南' : (new IO.Script).load("http://hunan.sina.com.cn/newscenter/hunan.js");
        break;

      case '重庆' : (new IO.Script).load("http://cq.sina.com.cn/newscenter/cq.js");
        break;

      case '湖北' : (new IO.Script).load("http://hb.sina.com.cn/newscenter/hb.js");
        break;

      case '浙江' : (new IO.Script).load("http://zj.sina.com.cn/newscenter/zj.js");
        break;

      case '福建' : (new IO.Script).load("http://fj.sina.com.cn/newscenter/fj.js");
        break;

      case '河南' : (new IO.Script).load("http://henan.sina.com.cn/newscenter/henan.js");
        break;

      case '上海' : (new IO.Script).load("http://sh.sina.com.cn/newscenter/sh.js");
        break;

      case '广东' : (new IO.Script).load("http://gd.sina.com.cn/newscenter/gd.js");
        break;

      case '四川' : (new IO.Script).load("http://sc.sina.com.cn/newscenter/sc.js");
        break;

      case '天津' : (new IO.Script).load("http://tj.sina.com.cn/newscenter/tj.js");
        break;

      case '江西' : (new IO.Script).load("http://jx.sina.com.cn/newscenter/jx.js");
        break;

      case '吉林' : (new IO.Script).load("http://jl.sina.com.cn/newscenter/jl.js");
        break;

      case '山西' : (new IO.Script).load("http://shanxi.sina.com.cn/newscenter/shanxi.js");
        break;

      case '山东' : (new IO.Script).load("http://sd.sina.com.cn/newscenter/sd.js");
        break;

      case '广西' : (new IO.Script).load("http://gx.sina.com.cn/newscenter/gx.js");
        break;

      case '海南' : (new IO.Script).load("http://hainan.sina.com.cn/newscenter/hainan.js");
        break;

      default : break;
    }
  }
</script>
<!-- iplookup 检查地域 end -->

<!-- AD tl03 begin -->
<!--XAD_STARTX-->
<!--_SINA_ADS_BEGIN_-->
<div><!-- 1000x90轮播通栏03广告 开始 -->
<div id="ad_47212">
  <script async charset="utf-8" src="//d5.sina.com.cn/litong/zhitou/sinaads/release/sinaads.js"></script><ins class="sinaads" data-ad-pdps="PDPS000000047212"></ins><script>(sinaads = window.sinaads || []).push({});</script>
</div></div>
<!--_SINA_ADS_END_-->
<!--XAD_ENDX-->
<!-- AD tl03 end -->

    <div class="partTit_01" id="blk_gjtltop_01"   data-sudaclick="gj2_tb">
<!-- publish_helper name='news_36_国际二类_栏目条' p_id='1' t_id='908' d_id='36' -->
      <div class="pT_name"><a href="http://news.sina.com.cn/world/" target="_blank" class="titName ptn_27">国际新闻</a></div>
      <div class="pT_more"><a href="http://news.sina.com.cn/zt/col_world/" target="_blank">国际新闻专题</a> | <a href="http://slide.news.sina.com.cn/w/" target="_blank">新闻图片</a> &nbsp;&nbsp;&nbsp;&nbsp;<a href="http://news.sina.com.cn/world/" target="_blank">更多&gt;</a></div>
    </div>

    <div class="part_02 pt_8 clearfix">
    	<div class="p_left">
            <div class="blk_new_03">
                <div class="blk_nav_2"><a class="blk_nav_tit" href="http://news.sina.com.cn/hotnews/#3" target="_blank">国际新闻每日排行</a> <div class="tit_more"><a href="http://news.sina.com.cn/hotnews/#3" target="_blank">更多</a></div></div>
                <div class="blk_content">
                    <div class="blk_content_1" tab-type="tab-cont">
                        <div class="blk_content_box" tab-type="tab-wrap" >
                            <div class="blk_content_tit">
                                <ol>
                                    <li tab-type="tab-nav" class="selected">今天</li>
                                    <li tab-type="tab-nav">昨天</li>
                                    <li tab-type="tab-nav">一周</li>
                                </ol>
                            </div>
                            <div class="blk_content_list" tab-type="tab-cont">
                                <ul id="gj_list_01"   data-sudaclick="gj_hotnews1">

                                </ul>
                            </div>
                            <div class="blk_content_list" tab-type="tab-cont" style="display:none;">
                                <ul id="gj_list_02" data-sudaclick="gj_hotnews2">

                                </ul>
                            </div>
                            <div class="blk_content_list" tab-type="tab-cont" style="display:none;">
                                <ul id="gj_list_03" data-sudaclick="gj_hotnews3">

                                </ul>
                            </div>
                        </div>
                     </div>

                    <div class="blk_content_2" tab-type="tab-cont">

                    </div>
                </div>
            </div>
            <script type="text/javascript">
			jsLoader(ARTICLE_JSS.jq,function(){

		//全站每日点击排行
		getAjaxData('//top.news.sina.com.cn/ws/GetTopDataList.php?top_channel=news&top_type=day&top_cat=www_www_all_suda_suda&top_time=today&top_show_num=8&top_order=DESC&js_var=data','all_list_01')

		//全站昨日点击排行
		getAjaxData('//top.news.sina.com.cn/ws/GetTopDataList.php?top_channel=news&top_type=day&top_cat=www_www_all_suda_suda&top_time='+GetDateStr(-1)+'&top_show_num=8&top_order=DESC&js_var=data','all_list_02')

		//全站一周点击排行
		getAjaxData('//top.news.sina.com.cn/ws/GetTopDataList.php?top_channel=news&top_type=week&top_cat=www_www_all_suda_suda&top_time=today&top_show_num=8&top_order=DESC&js_var=data','all_list_03')

		//新闻视频每日点击排行
		getAjaxData('//top.news.sina.com.cn/ws/GetTopDataList.php?top_type=day&top_cat=video_news_all_by_vv&top_time=today&top_show_num=8&top_order=DESC&callback=showVideoTop&__app_key=1841630516&format=json','newsvideo_list_01')

		//新闻视频昨日点击排行
		getAjaxData('//top.news.sina.com.cn/ws/GetTopDataList.php?top_type=day&top_cat=video_news_all_by_vv&top_time='+GetDateStr(-1)+'&top_show_num=8&top_order=DESC&callback=showVideoTop&__app_key=1841630516&format=json','newsvideo_list_02')

		//新闻视频一周点击排行
		getAjaxData('//top.news.sina.com.cn/ws/GetTopDataList.php?top_type=week&top_cat=video_news_all_by_vv&top_time=today&top_show_num=8&top_order=DESC&callback=showVideoTop&__app_key=1841630516&format=json','newsvideo_list_03')

		//全站分享排行
		getAjaxData('//top.news.sina.com.cn/ws/GetTopDataList.php?top_type=all&top_cat=wbrmzfxw&top_time=today&top_show_num=9&top_order=DESC&js_var=wbrmzfxw_1_data&short_title=1','all_list_04',true)

		//国内每日点击排行
		getAjaxData('//top.news.sina.com.cn/ws/GetTopDataList.php?top_type=day&top_cat=news_china_suda&top_time=today&top_show_num=10&top_order=DESC&js_var=china_1_data&short_title=1','gn_list_01')

		//国内昨日点击排行
		getAjaxData('//top.news.sina.com.cn/ws/GetTopDataList.php?top_type=day&top_cat=news_china_suda&top_time='+GetDateStr(-1)+'&top_show_num=10&top_order=DESC&js_var=china_1_data&short_title=1','gn_list_02') 

		//国内一周点击排行
		getAjaxData('//top.news.sina.com.cn/ws/GetTopDataList.php?top_type=week&top_cat=news_china_suda&top_time=today&top_show_num=10&top_order=DESC&js_var=china_2_data&short_title=1','gn_list_03') 

		//国际每日点击排行
					getAjaxData('//top.news.sina.com.cn/ws/GetTopDataList.php?top_type=day&top_cat=news_world_suda&top_time=today&top_show_num=5&top_order=DESC&js_var=world_1_data&call_back=showContent&short_title=1','gj_list_01')

		//国际昨日点击排行
		getAjaxData('//top.news.sina.com.cn/ws/GetTopDataList.php?top_type=day&top_cat=news_world_suda&top_time='+GetDateStr(-1)+'&top_show_num=5&top_order=DESC&js_var=world_1_data&short_title=1','gj_list_02') 

		//国际一周点击排行
		getAjaxData('//top.news.sina.com.cn/ws/GetTopDataList.php?top_type=week&top_cat=news_world_suda&top_time=today&top_show_num=5&top_order=DESC&js_var=world_2_data&short_title=1','gj_list_03')

				function createrNewLi(data,id,btn){
					var html = '';
					 for (var i = 0;i<data.length; i++) {
						var title = data[i].title;
						if (data[i].short_title && data[i].short_title != "None"){
						  //title = data[i].short_title;
						  //使用短标题
						}

						if(btn){
							var oNewLi = '<li><a href="' + data[i].url + '" target="_blank"><strong>'+commafy(data[i].top_num)+'</strong><em>'+(i+1)+'</em><span>' + title.gbCut(44) + '</span></a></li>';
							if(i == data.length-1){
								oNewLi = '<li class="last"><a href="' + data[i].url + '" target="_blank"><strong>'+commafy(data[i].top_num)+'</strong><em>'+(i+1)+'</em><span>' + title.gbCut(44) + '</span></a></li>';	
							}
							html += oNewLi;
						}else{

							if(id == "newsvideo_list_01" || id == "newsvideo_list_02" || id == "newsvideo_list_03")
							{
									title = title.replace(/视频:|视频：|视频-/g, '');
									var oNewLi = '<li><a href="' + data[i].url + '" target="_blank"><em>'+(i+1)+'</em><span class="videoNewsLeft">' + title.gbCut(44) + '</span></a></li>';
									if(i == data.length-1){
										oNewLi = '<li class="last"><a href="' + data[i].url + '" target="_blank"><em>'+(i+1)+'</em><span class="videoNewsLeft">' + title.gbCut(44) + '</span></a></li>';	
									}
									html += oNewLi;
							}
							else
							{
								var oNewLi = '<li><a href="' + data[i].url + '" target="_blank"><em>'+(i+1)+'</em>' + title.gbCut(46) + '</a></li>';
								if(i == data.length-1){
									oNewLi = '<li class="last"><a href="' + data[i].url + '" target="_blank"><em>'+(i+1)+'</em>' + title.gbCut(46) + '</a></li>';	
								}
								html += oNewLi;
							}

						}
					  }
					  document.getElementById(id).innerHTML = html;
				}

				function getAjaxData(url,id,btn){
					jQuery.ajax({
					type	  : "get",
					url       : url,
					dataType  : 'jsonp',
					jsonp: "callback",
					cache : "true",
					jsonpCallback : "hncb_" + id,
						success   : function(msg) {

							createrNewLi(msg.data || msg.result.data,id,btn)

						}
					 });		
				}
				function GetDateStr(AddDayCount) {
				  var dd = new Date();
				  dd.setDate(dd.getDate()+AddDayCount);//获取AddDayCount天后的日期
				  //var y = dd.getYear()+1900;
				  var y = dd.getFullYear();
				  var m = dd.getMonth()+1;//获取当前月份的日期
				  if (m<10) m = '0' + m;
				  var d = dd.getDate();
				  if (d<10) d = '0' + d;
				  return ''+y+m+d;
				}
				function commafy(num){
				  num = num+"";
				  var re=/(-?\d+)(\d{3})/
				  while(re.test(num)){
					num=num.replace(re,"$1,$2")
				  }
				  return num;
				}

			})

		</script>
            <div class="blk_new_05">
            	<div class="blk_nav_2"><a class="blk_nav_tit" href="http://travel.sina.com.cn/" target="_blank">新浪旅游</a> <div class="tit_more"><a href="http://travel.sina.com.cn/" target="_blank">更多</a></div></div>
                <div class="blk_box blk_l_info">
                	<div class="blk_main"  data-sudaclick="travel_1" style="height:255px;overflow:hidden;">
<!-- gsps旅游区块 -->
<!--t id="news_web_get_gspsdata" pid="1" tid="932" did="1" fid="sp_f23846" cname="旅游区块"-->

<div class="clearfix" style="padding: 0 0 6px;position: relative; margin: 0 auto;">
        <div  style=" float: left;width: 340px;background-color: #f2f2f2;zoom: 1;overflow: hidden;">
            <h4 class="link_c000" style="    font-size: 14px;font-weight: bold;line-height: 38px;    background: #fff;"><a href="http://travel.sina.com.cn" target="_blank">文艺小城华欣的浪漫与柔情</a></h4>
            <div  style="float: left;width: 116px;"><a href="http://travel.sina.com.cn" target="_blank"><img src="http://n.sinaimg.cn/travel/500/w300h200/20180604/duqR-hcmurvh4652041.jpg" width="150" height="100"></a></div>
            <div  style="margin-left: 156px;padding-right: 2px;padding-left: 3px;_padding-left: 0;color: #666;line-height: 24px;padding-top: 5px;word-break: break-all;">除了清迈，小城华欣的文艺与清新，也在一簇簇鲜花和斑斓的色彩中，绽放着独有的浪漫与柔情······</div>
        </div>
</div>

<ul class="link_c666 ul_c666">
<!-- gsps旅游区块 -->
<!--t id="news_web_get_gspsdata" pid="1" tid="932" did="1" fid="sp_f23843" cname="旅游区块"-->
<li><a target="_blank" href="http://travel.sina.com.cn/itinerary/?domestic">国内|</a> <a target="_blank" href="http://travel.sina.com.cn/domestic/pages/2018-06-04/detail-ihcmurvh3130044.shtml">灵山福地永州阳明山</a> <a target="_blank" href="http://travel.sina.com.cn/domestic/pages/2018-06-04/detail-ihcmurvh3013450.shtml">绿水绕青山醉美湘江源</a></li><li><a target="_blank" href="http://travel.sina.com.cn/itinerary/?domestic">出境|</a> <a target="_blank" href="http://travel.sina.com.cn/outbound/pages/2018-06-04/detail-ihcmurvh3287665.shtml">一座古老而又年轻的小城</a> <a href="http://travel.sina.com.cn/outbound/pages/2018-05-23/detail-ihawmauc3247600.shtml" target="_blank">泰国小城的浪漫与柔情</a></li><li><a target="_blank" href="http://travel.sina.com.cn/news/">行业|</a> <a target="_blank" href="http://travel.sina.com.cn/domestic/news/2018-06-01/detail-ihcikcev9554851.shtml">加长版复兴号上京沪高铁</a>  <a target="_blank" href="http://travel.sina.com.cn/domestic/news/2018-06-04/detail-ihcmurvh3740586.shtml">云南整治旅游购物场所</a></li>
<li><a target="_blank" href="http://travel.sina.com.cn/video/">视频|</a> <a href="http://travel.sina.com.cn/video/hot/2018-05-30/detail-ihcikcew2950775.shtml" target="_blank">探寻旷世海难背后的故事</a> <a href="http://travel.sina.com.cn/video/hot/2018-06-03/detail-ihcmurvf9293176.shtml" target="_blank">十大高性价比目的地</a></li><li><a target="_blank" href="http://travel.sina.com.cn/hdphoto/">发现|</a>  <a target="_blank" href="http://slide.travel.sina.com.cn/slide_68_87701_392203.html">可可西里最美的人间禁地</a> <a href="http://slide.travel.sina.com.cn/slide_68_87701_392204.html" target="_blank">星光璀璨的观光隧道</a></li>
</ul>

					</div>
                </div>
            </div>
        </div>
		<div class="p_middle" >
  <!-- middle begin -->

<!-- gsps国际通栏列表 -->
		
		<!-- 国际新闻 -->
        <div class="blk_09" id="blk_ndxw_01" data-sudaclick="gj2_list_01">
 			<ul class="list_14">
				<li><a href="http://news.sina.com.cn/w/2018-06-04/doc-ihcmurvh7872349.shtml" target="_blank" >被控违法超5万次罚34亿 这家银行终于承认洗钱了</a><span class="time"> 21:47</span></li>			<li><a href="http://news.sina.com.cn/w/sy/2018-06-04/doc-ihcmurvh7826356.shtml" target="_blank" >美国强征钢铝关税惹众怒 G7部长会不欢而散</a><span class="time"> 21:35</span></li>			<li><a href="http://news.sina.com.cn/w/sy/2018-06-04/doc-ihcmurvh7726984.shtml" target="_blank" >FBI探员在酒吧忘我热舞 结果腰间枪走火打中他人</a><span class="time"> 21:24</span></li>			<li><a href="http://news.sina.com.cn/w/sy/2018-06-04/doc-ihcmurvh7592010.shtml" target="_blank" >以牙还牙？俄法院指控乌克兰记者犯间谍罪 判12年</a><span class="time"> 20:59</span></li>			<li><a href="http://news.sina.com.cn/w/sy/2018-06-04/doc-ihcmurvh7532352.shtml" target="_blank" >驻叙美军基地发生爆炸致1死 叙民主力量淡定训练</a><span class="time"> 20:45</span></li>			<li><a href="http://news.sina.com.cn/w/sy/2018-06-04/doc-ihcmurvh7657675.shtml" target="_blank" >4岁乔治王子热衷马术 威廉夫妇为帮儿子圆梦拼了</a><span class="time"> 20:34</span></li>			<li><a href="http://news.sina.com.cn/w/sy/2018-06-04/doc-ihcmurvh7421047.shtml" target="_blank" >文在寅在青瓦台会见菲律宾总统杜特尔特</a><span class="time"> 20:30</span></li>
	</ul><div class="line_01"></div>	<ul class="list_14">
				<li><a href="http://news.sina.com.cn/o/2018-06-04/doc-ihcmurvh7411612.shtml" target="_blank" >新媒：朝拟在新加坡租车 供金正恩在“特金会”用</a><span class="time"> 20:29</span></li>			<li><a href="http://news.sina.com.cn/w/sy/2018-06-04/doc-ihcmurvh7400512.shtml" target="_blank" >普京：美国的政治骚动给俄美会谈的筹备造成困扰</a><span class="time"> 20:28</span></li>			<li><a href="http://news.sina.com.cn/w/2018-06-04/doc-ihcmurvh7314598.shtml" target="_blank" >印尼非法金矿发生山体滑坡 造成5人死亡1人失踪</a><span class="time"> 20:05</span></li>			<li><a href="http://news.sina.com.cn/w/2018-06-04/doc-ihcmurvh7123522.shtml" target="_blank" >约旦首相汉尼-穆尔基辞职</a><span class="time"> 19:44</span></li>			<li><a href="http://news.sina.com.cn/o/2018-06-04/doc-ihcmurvh6930121.shtml" target="_blank" >保加利亚要处死一只奶牛：因它“无证”进入欧盟</a><span class="time"> 19:14</span></li>			<li><a href="http://news.sina.com.cn/o/2018-06-04/doc-ihcmurvh6749687.shtml" target="_blank" >韩国文体部：朝韩将共同编纂民族语言大辞典</a><span class="time"> 18:42</span></li>			<li><a href="http://news.sina.com.cn/o/2018-06-04/doc-ihcmurvh6665805.shtml" target="_blank" >新加坡“特金会”酒店将划为“特别活动区”</a><span class="time"> 18:28</span></li>
	</ul><div class="line_01"></div>	<ul class="list_14">
				<li><a href="http://news.sina.com.cn/w/2018-06-04/doc-ihcmurvh6591517.shtml" target="_blank" >阿富汗自杀式炸弹袭击7死9伤 暂无组织宣称负责</a><span class="time"> 18:16</span></li>			<li><a href="http://news.sina.com.cn/o/2018-06-04/doc-ihcmurvh6485316.shtml" target="_blank" >默克尔拒为意减免债务 称欧元区不应变成债务联盟</a><span class="time"> 18:02</span></li>			<li><a href="http://news.sina.com.cn/w/sy/2018-06-04/doc-ihcmurvh6509533.shtml" target="_blank" >俄将实施航空乘客黑名单制度 有人将被禁飞1年</a><span class="time"> 17:55</span></li>			<li><a href="http://news.sina.com.cn/o/2018-06-04/doc-ihcmurvh6399178.shtml" target="_blank" >台湾货船掉落83个集装箱 悉尼海滩能捡到尿布</a><span class="time"> 17:52</span></li>			<li><a href="http://news.sina.com.cn/w/sy/2018-06-04/doc-ihcmurvh6443549.shtml" target="_blank" >被乌克兰拘留的俄记者公寓遭洗劫 尚不明何人所为</a><span class="time"> 17:50</span></li>			<li><a href="http://news.sina.com.cn/w/sy/2018-06-04/doc-ihcmurvh6339286.shtml" target="_blank" >俄罗斯安全局逮捕11名恐怖分子招募者</a><span class="time"> 17:38</span></li>
	</ul>        </div>
        
        
			
			
  <!-- middle end -->
		</div>

<!--XBLK_STARTX-->
        <div class="p_right">
        	<div class="blk_new_04">

                <div class="blk_nav_3">
                	<a class="blk_nav_tit" href="http://slide.news.sina.com.cn/w/" target="_blank">国际热图</a><div class="tit_more"><a href="http://slide.news.sina.com.cn/w/" target="_blank">更多</a></div>
                </div>
                <div class="blk_box">
                	<div class="b_cont w_240">
                      <div class="ct_p_05 clearfix" id="scrPic_gjrt_01"  data-sudaclick="blk_gjrt">
		
		<div class="ct_pic w_240"><a href="http://slide.news.sina.com.cn/w/slide_1_2841_280667.html" target="_blank"><img data-src="http://k.sinaimg.cn/n/news/transform/200/w600h400/20180604/N33v-hcmurvh3387520.jpg/w240h156z1l0t0q100713.jpg" alt="美国边防警察射杀偷渡少女" /><span class="ct_txt">美国边防警察射杀偷渡少女</span></a></div>		<div class="ct_pic w_240"><a href="http://slide.news.sina.com.cn/w/slide_1_2841_280591.html" target="_blank"><img data-src="http://k.sinaimg.cn/n/news/transform/200/w600h400/20180604/m_NS-hcmurvh2563019.jpg/w240h156z1l0t0q100e0f.jpg" alt="世界知名连体婴姐妹双双去世 年仅21岁" /><span class="ct_txt">世界知名连体婴姐妹双双去世 年仅2..</span></a></div>		<div class="ct_pic w_240"><a href="http://slide.news.sina.com.cn/w/slide_1_2841_280571.html" target="_blank"><img data-src="http://k.sinaimg.cn/n/news/transform/200/w600h400/20180604/LrBm-hcmurvh2457017.jpg/w240h156z1l0t0q100380.jpg" alt="菲律宾总统杜特尔特抵韩访问" /><span class="ct_txt">菲律宾总统杜特尔特抵韩访问</span></a></div>		<div class="ct_pic w_240"><a href="http://slide.news.sina.com.cn/w/slide_1_2841_280555.html" target="_blank"><img data-src="http://k.sinaimg.cn/n/news/transform/200/w600h400/20180604/_fVa-hcmurvh2343300.jpg/w240h156z1l0t0q1002d5.jpg" alt="这是金正恩给特朗普写的亲笔信" /><span class="ct_txt">这是金正恩给特朗普写的亲笔信</span></a></div>        
        
					  </div>
                      <a href="javascript:void(0)" class="scrArrAbsLeft" id="scrArrLeft_gjrt_01"></a>
                      <a href="javascript:void(0)" class="scrArrAbsRight" id="scrArrRight_gjrt_01"></a>
                    </div>

                    <div class="b_cons">
                      <span class="scrDotList" id="scrDotList_gjrt_01">
                        <span></span>
                      </span>
                    </div>
					<script type="text/javascript">
                       jsLoader(ARTICLE_JSS.common,function(){
                          var focusScroll = new ScrollPic();
                          focusScroll.scrollContId  = "scrPic_gjrt_01"; //内容容器ID

                          focusScroll.dotListId   = "scrDotList_gjrt_01";//点列表ID
                          focusScroll.dotClassName  = "";//点className
                          focusScroll.dotOnClassName = "on";//当前点className
                          focusScroll.listType  = "";//列表类型(number:数字，其它为空)
                          focusScroll.listEvent = "onmouseover"; //切换事件

                          focusScroll.frameWidth  = 240;//显示框宽度
                          focusScroll.pageWidth = 240; //翻页宽度
                          focusScroll.upright = false; //垂直滚动
                          focusScroll.speed   = 10; //移动速度(单位毫秒，越小越快)
                          focusScroll.space   = 40; //每次移动像素(单位px，越大越快)
                          focusScroll.autoPlay  = false; //自动播放
                          focusScroll.autoPlayTime = 5; //自动播放间隔时间(秒)
                          focusScroll.circularly = true;
                          focusScroll.initialize(); //初始化
                          document.getElementById('scrArrLeft_gjrt_01').onmousedown = function(){
                            focusScroll.pre();
                            return false;
                          }
                          document.getElementById('scrArrRight_gjrt_01').onmousedown = function(){
                            focusScroll.next();
                            return false;
                          }
                      });
                    </script>
                </div>
                 <div class="blk_nav_3">
                	<a href="http://news.sina.com.cn/media/" class="blk_nav_tit" target="_blank">传媒</a><div class="tit_more"><a href="http://news.sina.com.cn/media/" target="_blank">更多</a></div>
                </div>
                <div class="blk_box blk_r_info">
                	<div class="blk_main" data-sudaclick="blk_cm">
<!-- gsps传媒区块 -->
<!--t id="news_web_get_gspsdata" pid="1" tid="908" did="19" fid="sp_f23232" cname="传媒区块"-->
<h3 class="link_c333"><a href="http://news.sina.com.cn/media/" target="_blank"><b>全球热捧北京电影节</b></a></h3>

<div class="pic_info clearfix">
	<div class="l_pic"><a href="http://news.sina.com.cn/m/roll/2016-04-22/doc-ifxrpvea1092102.shtml" target="_blank"><img data-src="http://www.sinaimg.cn/dy/2016/0422/U1987P1DT20160422111202.jpg
		" width="100" height="66" alt="首页配图" src="http://www.sinaimg.cn/dy/2016/0422/U1987P1DT20160422111202.jpg&#10;"></a></div>
	<div class="r_txt"><p>每年50%的递增幅度，让中国电影市场成了一块巨大吸铁石。<a class="news_more" href="http://news.sina.com.cn/m/roll/2016-04-22/doc-ifxrpvea1092102.shtml" target="_blank">[详细]</a></p></div>
</div>
					</div>
                </div>

            </div>

            <div style="margin-top:10px;">

<a href="http://news.sina.com.cn/pc/2016-03-17/326/3319.html" target="_blank"><img src="http://www.sinaimg.cn/dy/2016/0321/U11594P1DT20160321190229.png" /></a>

			</div>

        </div>
<!--XBLK_ENDX-->
    </div>

    <!-- part_02 end -->

	<div class="sp_h10"></div>

    <!-- part_03 begin -->

<!-- AD tl04 begin -->
<!--XAD_STARTX-->
<!--_SINA_ADS_BEGIN_-->
<div><!-- 1000x90轮播通栏04广告 开始 -->
<div id="ad_47213">
<ins class="sinaads" id="PDPS000000058104" data-ad-pdps="PDPS000000058104" style="border:1px solid #ccc;"></ins>
  <script>
  (sinaads = window.sinaads || []).push({
    params : {
    sinaads_success_handler : function(){
      var xwsy000ceshi = document.getElementById('PDPS000000058104');
      xwsy000ceshi.childNodes[0].style.width = 970 + 'px';
    }
  }
  });
  </script>
</div></div>
<!--_SINA_ADS_END_-->
<!--XAD_ENDX-->
<!-- AD tl04 end -->

	<div class="sp_h10"></div>


<!-- gsps军事通栏 p_id=1&t_id=912&f_id=28346 -->
<!--t id="news_web_get_gspsdata" pid="1" tid="912" did="1" fid="sp_f28346" cname="军事通栏"-->
<!-- 军事通栏开始 -->
<div class="partTit_02" id="blk_jstltop_01" data-sudaclick="mil2_tb">
	<div class="pT_name"><a href="http://mil.news.sina.com.cn/" target="_blank" class="titName ptn_28">军事新闻</a></div>
	<div class="pT_more"><a href="http://slide.mil.news.sina.com.cn/" target="_blank" class="link-fff">军图大全</a> | <a href="http://mil.news.sina.com.cn/jssd/" target="_blank" class="linkRed">深度观察</a> | <a href="http://mil.news.sina.com.cn/dgby/" target="_blank" class="link-fff">大国博弈</a> | <a href="http://mil.news.sina.com.cn/jshm/" target="_blank" class="link-fff">军史揭秘</a> | <a href="http://roll.mil.news.sina.com.cn/s_zghjxldyd_all/index.shtml" target="_blank" class="link-fff">东海局势</a> | <a href="http://mil.news.sina.com.cn/nz/nhjszxdt/" target="_blank" class="link-fff">南海局势</a>  &nbsp;&nbsp&nbsp;&nbsp;<a href="http://mil.news.sina.com.cn/" target="_blank" >更多&gt;</a></div>
</div>

<div class="part_03 clearfix">

	<div class="p_left">
		<div class="blk_01 blk_new_06" tab-type="tab-wrap" data-sudaclick="mil2_pic">
			
<div class="blk_tit mb_10">
	<ol>
		<li tab-type="tab-nav" class='selected'><a href="http://slide.mil.news.sina.com.cn/i_list_8_203.html" target="_blank">中国海军</a></li>	<li tab-type="tab-nav" class=''><a href="http://slide.mil.news.sina.com.cn/i_list_8_193.html" target="_blank">中国空军</a></li>	<li tab-type="tab-nav" class=''><a href="http://slide.mil.news.sina.com.cn/s_list_8_199.html" target="_blank">中国陆军</a></li>	<li tab-type="tab-nav" class=''><a href="http://slide.mil.news.sina.com.cn/s_list_8_204.html" target="_blank">国际军情</a></li>	</ol>
</div>
<ul class="blk_main">
		<li style="" tab-type="tab-cont">
		<a href="http://slide.mil.news.sina.com.cn/h/slide_8_203_63568.html" target="_blank" class="pic"><img src="http://n.sinaimg.cn/mil/transform/576/w338h238/20180515/Ynfv-hapkuvm0606039.jpg"/></a>
		<div class="text"><a href="http://slide.mil.news.sina.com.cn/h/slide_8_203_63568.html" target="_blank">更显威猛！俯瞰中国海军航母战舰</a></div>
	</li>	<li style="display:none;" tab-type="tab-cont">
		<a href="http://slide.mil.news.sina.com.cn/k/slide_8_193_55549.html" target="_blank" class="pic"><img src="http://www.sinaimg.cn/jc/pc/2017-07-21/28/U12794P27T28D4872F431DT20170801180723.jpg"/></a>
		<div class="text"><a href="http://slide.mil.news.sina.com.cn/k/slide_8_193_55549.html" target="_blank">亚洲最强歼20现身阅兵！正面照帅瞎你</a></div>
	</li>	<li style="display:none;" tab-type="tab-cont">
		<a href="http://slide.mil.news.sina.com.cn/l/slide_8_199_55856.html" target="_blank" class="pic"><img src="http://www.sinaimg.cn/jc/pc/2017-08-07/28/U12794P27T28D4873F427DT20170811223157.jpg"/></a>
		<div class="text"><a href="http://slide.mil.news.sina.com.cn/l/slide_8_199_55856.html" target="_blank">3D打印！解放军空中突击旅战力爆表</a></div>
	</li>	<li style="display:none;" tab-type="tab-cont">
		<a href="http://slide.mil.news.sina.com.cn/l/slide_8_235_55800.html" target="_blank" class="pic"><img src="http://www.sinaimg.cn/jc/pc/2017-08-07/28/U12794P27T28D4873F426DT20170809224705.jpg"/></a>
		<div class="text"><a href="http://slide.mil.news.sina.com.cn/l/slide_8_235_55800.html" target="_blank">印度陆军之花！研制三十年的阿琼坦克</a></div>
	</li></ul>
		</div>
	</div>
	<div class="p_middle">
		<!-- middle begin -->
		<div class="Tit_06">
			<div class="t_name"><a href="http://mil.news.sina.com.cn/" target="_blank">军事新闻</a></div>
		</div>

		<div class="blk_28" id="blk_jsxw_02" data-sudaclick="mil2_list">
			
	<ul class="list_14">
				<li><a href="http://mil.news.sina.com.cn/jssd/2018-06-04/doc-ihcmurvh6538393.shtml" target="_blank" >印度试射烈火5导弹 印网友吐槽：为时已晚朝鲜都有了</a><span class="time"> 18:11</span></li>			<li><a href="http://mil.news.sina.com.cn/china/2018-06-04/doc-ihcmurvh5983473.shtml" target="_blank" >台军演习坠毁F16战机残骸被找到 已摔成碎片(图)</a><span class="time"> 16:54</span></li>			<li><a href="http://mil.news.sina.com.cn/jssd/2018-06-04/doc-ihcmurvh5881615.shtml" target="_blank" >辽宁舰直18预警机战位曝光：指挥人员比美E2还多1人</a><span class="time"> 16:40</span></li>			<li><a href="http://mil.news.sina.com.cn/2018-06-04/doc-ihcmurvh4316039.shtml" target="_blank" >中国054A舰刷产量记录 或成全球产量最大远洋护卫舰</a><span class="time"> 13:00</span></li>			<li><a href="http://mil.news.sina.com.cn/jssd/2018-06-04/doc-ihcmurvh4006281.shtml" target="_blank" >中国霹雳21导弹研发11年仍未亮相 或只是试验项目</a><span class="time"> 12:10</span></li>
	</ul><div class="line_01"></div>	<ul class="list_14">
				<li><a href="http://mil.news.sina.com.cn/jssd/2018-06-04/doc-ihcmurvh3729040.shtml" target="_blank" >中国太行发动机改成舰载燃气轮机 表现优于进口产品</a><span class="time"> 11:32</span></li>			<li><a href="http://mil.news.sina.com.cn/china/2018-06-04/doc-ihcmurvh3655441.shtml" target="_blank" >美防长香会发言就南海问题指责中国 却罕见无人捧场</a><span class="time"> 11:23</span></li>			<li><a href="http://mil.news.sina.com.cn/china/2018-06-04/doc-ihcmurvh3588232.shtml" target="_blank" >印媒：印度烈火5足以打遍中国 正研烈火6射程将翻倍</a><span class="time"> 11:15</span></li>			<li><a href="http://mil.news.sina.com.cn/jssd/2018-06-04/doc-ihcmurvh3286199.shtml" target="_blank" >美军26万支步枪被曝有走火危险 拧保险旋钮就会射击</a><span class="time"> 10:38</span></li>			<li><a href="http://mil.news.sina.com.cn/jssd/2018-06-04/doc-ihcmurvh3218223.shtml" target="_blank" >中国今年前5个月造出6架运20 但产能却受该因素制约</a><span class="time"> 10:30</span></li>
	</ul>        
        
		</div>

		<!-- middle end -->
	</div>

	<!--XBLK_STARTX-->
	<div class="p_right">
		<div class="blk_new_07">
			<div class="blk_nav_3">
				<a class="blk_nav_tit" href="http://mil.news.sina.com.cn/jssd/" target="_blank">热点追踪</a><div class="tit_more"><a href="http://mil.news.sina.com.cn/jssd/" target="_blank">更多</a></div>
			</div>
			<div class="blk_box blk_r_info" data-sudaclick="mil2_jqcg">
				<h3 class="link_c333">
<a href="http://mil.news.sina.com.cn/jssd/" target="_blank">印度首曝核试验照片 起爆点代号白宫
</a>
</h3>

<p>近日，印度官方首次公开了20年前代号为SHAKTI的核试验的照片<a class="news_more" href="http://mil.news.sina.com.cn/jssd/" target="_blank">[详细]</a></p>
<ul class="link_c666 ul_c666">
<li><a href="http://mil.news.sina.com.cn/jssd/2018-05-15/doc-ihapkuvm0460675.shtml" target="_blank">深度：俄为何想邀请中国访问国际空间站</a></li>
<li><a href="http://mil.news.sina.com.cn/jssd/2017-01-03/doc-ifxzczfc6695576.shtml" target="_blank">深度：敏感时期东风41亮剑有何玄机</a></li>
<li><a href="http://mil.news.sina.com.cn/jssd/2017-01-03/doc-ifxzczfc6695238.shtml" target="_blank">深度：神盾舰数量超美日在亚太总和</a></li>
</ul>
			</div>

			<div class="blk_nav_3 mt_20">
				<a class="blk_nav_tit" href="http://slide.mil.news.sina.com.cn/" target="_blank">最热图片</a><div class="tit_more"><a href="http://slide.mil.news.sina.com.cn/" target="_blank">更多</a></div>
			</div>
			<div class="blk_box blk_r_info" data-sudaclick="mil2_mbrt">
				
<ul class="link_c666 ul_c666">
	<li><a target="_blank" href="http://slide.mil.news.sina.com.cn/h/slide_8_203_63575.html" >中国舰队纵横东印度洋猛烈开火</a></li><li><a target="_blank" href="http://slide.mil.news.sina.com.cn/l/slide_8_199_47707.html" >曝中国新轻型坦克已批量服役</a></li><li><a target="_blank" href="http://slide.mil.news.sina.com.cn/k/slide_8_193_47695.html" >最新解放军歼20量产机亮相</a></li><li><a target="_blank" href="http://slide.mil.news.sina.com.cn/l/slide_8_28669_47699.html" >中国M99重狙阿勒颇战场发威</a></li><li><a target="_blank" href="http://slide.mil.news.sina.com.cn/l/slide_8_249_47703.html" >伊拉克用中国02式高射机枪打</a></li></ul>

			</div>
		</div>
	</div>
	<!--XBLK_ENDX-->
</div>
<!-- 军事通栏结束 -->

    <div class="sp_h20"></div>


<!-- gsps健康通栏 p_id=1&t_id=912&f_id=28325 -->
<!--t id="news_web_get_gspsdata" pid="1" tid="912" did="1" fid="sp_f28325" cname="健康通栏" -->
<!-- part_health begin -->
<div class="partTit_02" id="blk_jktltop_01" data-sudaclick="heal2_tb">
	<!-- publish_helper name='health_2_健康通栏_栏目条' p_id='1' t_id='916' d_id='2' -->
	<div class="pT_name"><a href="http://health.sina.com.cn/" target="_blank" class="titName ptn_29">健康新闻</a></div>
	<div class="pT_more"><a href="http://med.sina.com" target="_blank">医药新闻</a> | <a href="http://med.sina.com/article_gategory_101.html" target="_blank">药店</a> | <a href="http://health.sina.com.cn/disease/" target="_blank">疾病</a> | <a href="http://health.sina.com.cn/healthcare/" target="_blank">保健</a> | <a href="http://health.sina.com.cn/zl/" target="_blank">专栏</a> | <a href="http://health.sina.com.cn/" target="_blank">更多&gt;</a></div>
</div>

<div class="part_03 clearfix">
	<div class="p_left clearfix">
		<!-- left begin -->
		<div class="blk_new_08">
			<ul>
				<li><a target="_blank" href="http://health.sina.com.cn/disease/ku/">查病</a></li>
				<li><a target="_blank" href="http://drug.health.sina.com.cn/default.html">问药</a></li>
				<li><a target="_blank" href="http://health.sina.com.cn/healthcare/">养生</a></li>
				<li><a target="_blank" href="http://health.sina.com.cn/yanglao/">养老</a></li>
			</ul>
		</div>
		<div class="blk_27" id="blk_jkxw_01">
			<div class="b_cont">
				<div class="ct_p_05 clearfix" id="scrPic_jkxw_01"  data-sudaclick="heal2_pic">
					<!-- 轮播图 -->
					<div class="ct_pic"><a href="http://slide.health.sina.com.cn/slide_31_86516_173472.html#p=1" target="_blank"><img src="http://n.sinaimg.cn/health/w260h150/20180131/F2Hs-fyrcsrw1386110.jpg" width="260" height="150" alt="" /><span class="ct_txt">感冒多发，认清药盒上这些字再吃药</span></a></div><div class="ct_pic"><a href="http://slide.health.sina.com.cn/hc/slide_31_28380_38333.html#p=1" target="_blank"><img src="http://n.sinaimg.cn/health/w260h150/20180131/YNaG-fyrcsrw1371745.jpg" width="260" height="150" alt="" /><span class="ct_txt">冬季如何保护胃健康</span></a></div><div class="ct_pic"><a href="http://slide.health.sina.com.cn/d/slide_31_28379_133970.html#p=1" target="_blank"><img src="http://n.sinaimg.cn/health/w260h150/20180131/prsJ-fyrcsrw1379338.jpg" width="260" height="150" alt="" /><span class="ct_txt">6个远离职业病小妙招</span></a></div><div class="ct_pic"><a href="http://slide.health.sina.com.cn/d/slide_31_28379_230260.html#p=1" target="_blank"><img src="http://n.sinaimg.cn/health/w260h150/20180122/jhgW-fyqwiqi1985397.jpg" width="260" height="150" alt="" /><span class="ct_txt">摄影师为患病儿童拍超级英雄照</span></a></div>				</div>
				<a href="javascript:void(0)" class="scrArrAbsLeft" id="scrArrLeft_jkxw_01"></a>
				<a href="javascript:void(0)" class="scrArrAbsRight" id="scrArrRight_jkxw_01"></a>
			</div>
			<div class="b_cons">
				<span class="scrDotList" id="scrDotList_jkxw_01">
					<span></span>
				</span>
			</div>
		</div>

		<script type="text/javascript">
			jsLoader(ARTICLE_JSS.common,function(){
				var focusScroll = new ScrollPic();
				focusScroll.scrollContId  = "scrPic_jkxw_01"; //内容容器ID

				focusScroll.dotListId   = "scrDotList_jkxw_01";//点列表ID
				focusScroll.dotClassName  = "";//点className
				focusScroll.dotOnClassName = "on";//当前点className
				focusScroll.listType  = "";//列表类型(number:数字，其它为空)
				focusScroll.listEvent = "onmouseover"; //切换事件

				focusScroll.frameWidth  = 260;//显示框宽度
				focusScroll.pageWidth = 260; //翻页宽度
				focusScroll.upright = false; //垂直滚动
				focusScroll.speed   = 10; //移动速度(单位毫秒，越小越快)
				focusScroll.space   = 40; //每次移动像素(单位px，越大越快)
				focusScroll.autoPlay  = false; //自动播放
				focusScroll.autoPlayTime = 5; //自动播放间隔时间(秒)
				focusScroll.circularly = true;
				focusScroll.initialize(); //初始化
				document.getElementById('scrArrLeft_jkxw_01').onmousedown = function(){
					focusScroll.pre();
					return false;
				}
				document.getElementById('scrArrRight_jkxw_01').onmousedown = function(){
					focusScroll.next();
					return false;
				}
			});
		</script>

		<!-- left end -->
	</div>
	<div class="p_middle">
		<!-- middle begin -->
		<div class="blk_28" id="blk_jkxw_02">
			<ul class="list_14">
				<!-- mid -->
				<li class="dot topli14"><a href="http://health.sina.com.cn/" target="_blank"></a><a target="_blank" href="http://health.sina.com.cn/">长白发是缺什么营养</a> <a target="_blank" href="http://med.sina.com/health/">调查发现不少女性后悔冷冻卵子</a></li><li><a target="_blank" href="http://med.sina.com/health/article_detail_101_2_182.html">夏天爱出汗是因为肾虚？</a> <a target="_blank" href="http://med.sina.com/health/article_detail_100_2_219.html">如何凭眼力就能挑出甜甜的樱桃</a></li>

<li><a target="_blank" href="http://med.sina.com/health/article_detail_100_2_184.html">教你自制正宗酸梅汤</a>  <a target="_blank" href="http://med.sina.com/health/article_detail_100_2_222.html">这种东西放进药酒可能变毒酒</a></li>

<li><a target="_blank" href="http://med.sina.com/health/article_detail_103_1_208.html">退烧针柴胡注射液儿童被禁用</a> <a target="_blank" href="http://health.sina.com.cn/hc/2018-06-01/doc-ihcikcev9352748.shtml">一分钟测测你的记忆力</a></li>

<li><a target="_blank" href="http://health.sina.com.cn/hc/2018-05-30/doc-ihcffhsv4529293.shtml">夏季吃姜好处多</a> <a href="http://med.sina.com/health/article_detail_100_1_220.html" target="_blank">常吃坚果或降低心率不齐风险</a></li>


<li><a target="_blank" href="http://health.sina.com.cn/hc/2018-05-28/doc-ihcaquev3121712.shtml">盐吃得太少也致病</a> <a target="_blank" href="http://med.sina.com/health/article_detail_100_1_223.html">女性体内湿气过重有什么危害</a></li>

<li><a target="_blank" href="http://med.sina.com/health/article_detail_103_1_221.html">7名农民工误食断肠草中毒致3人死亡</a> <a href="http://health.sina.com.cn/d/2018-06-04/doc-ihcffhsu5372652.shtml" target="_blank">猝死前六个信号</a></li>			</ul>
		</div>
		<!-- middle end -->
	</div>

	<!--XBLK_STARTX-->
	<div class="p_right">
		<!-- right begin -->
		<div class="blk_30" id="blk_jkxw_03"  data-sudaclick="heal2_rpic">
			<!--r inner start-->
			<div class="ct_pt_07 clearfix">
				<div class="ct_pic"><a href="http://health.sina.com.cn/d/2017-11-10/doc-ifynstfh3381540.shtml" target="_blank"><img src="http://www.sinaimg.cn/dy/2018/0117/U12054P1DT20180117155255.jpg" width="85" height="85" alt="" /><span class="ct_tit">大医精诚李小霞</span></a></div>
				<div class="ct_txt">
					<ul class="list_12 link_c666">
						<li><a href="http://video.sina.com.cn/view/252083443.html" target="_blank">视频：云石纹蒸蛋糕</a></li><li><a href="http://slide.health.sina.com.cn/slide_31_86516_187678.html#p=1" target="_blank">抓住早晨黄金十分钟</a></li><li><a href="http://slide.health.sina.com.cn/d/slide_31_28379_133975.html#p=1" target="_blank">该怎么拯救哮喘的你</a></li><li><a href="http://slide.health.sina.com.cn/d/slide_31_28379_133974.html#p=1" target="_blank">让宝宝和咳嗽说再见</a></li>					</ul>
				</div>
			</div>
			<div class="ct_pt_07 clearfix mt_10">
				<div class="ct_pic"><a href="http://video.sina.com.cn/view/252083442.html" target="_blank"><img src="http://www.sinaimg.cn/dy/2017/1122/U5307P1DT20171122093448.jpg" width="85" height="85" alt="" /><span class="ct_tit">孜然羊排</span></a></div>
				<div class="ct_txt">
					<ul class="list_12 link_c666">
						<li><a href="http://slide.health.sina.com.cn/slide_31_86516_187247.html#p=1" target="_blank">冬季多吃养肺食物</a></li><li><a href="http://slide.health.sina.com.cn/slide_31_86516_185996.html#p=1" target="_blank">筋长一寸寿长十年</a></li><li><a href="http://video.sina.com.cn/view/252083440.html" target="_blank">元气早餐清汤面</a></li><li><a href="http://health.sina.com.cn/hc/2018-01-31/doc-ifyrcsrw1022878.shtml" target="_blank">过年要这么吃坚果</a></li>					</ul>
				</div>
			</div>
			<!--r inner end -->
		</div>
		<!-- right end -->
	</div>
	<!--XBLK_ENDX-->
</div>

<!-- part_health end -->





<!-- part_sports begin -->
<div class="partTit_01" id="blk_tytltop_01" data-sudaclick="sports2_tb">
  <div class="pT_name"><a href="http://sports.sina.com.cn/" target="_blank" class="titName ptn_30">体育新闻</a></div>
  <div class="pT_more"><a target="_blank" href="http://sports.sina.com.cn/nba/">NBA</a> | <a target="_blank" href="http://sports.sina.com.cn/cba/">CBA</a> | <a target="_blank" href="http://sports.sina.com.cn/g/championsleague/">欧冠</a> | <a target="_blank" href="http://sports.sina.com.cn/g/premierleague/">英超</a> | <a target="_blank" href="http://sports.sina.com.cn/g/laliga/">西甲</a> | <a target="_blank" href="http://sports.sina.com.cn/g/seriea/">意甲</a> | <a target="_blank" href="http://sports.sina.com.cn/g/bundesliga/">德甲</a> | <a target="_blank" href="http://sports.sina.com.cn/csl/">中超</a> | <a target="_blank" href="http://sports.sina.com.cn/z/AFCCL2016/">亚冠</a> | <a target="_blank" href="http://sports.sina.com.cn/tennis/">网球</a> | <a target="_blank" href="http://golf.sina.com.cn/">高尔夫</a> | <a target="_blank" href="http://f1.sina.com.cn/">F1</a> | <a target="_blank" href="http://sports.sina.com.cn/hdphoto/">高清图</a> &nbsp;&nbsp&nbsp;&nbsp;<a target="_blank" href="http://sports.sina.com.cn/">更多&gt;</a></div></div>

<div class="part_02 clearfix">
  <div class="p_left">
  <!-- left begin -->

<div class="Tit_08 t_mr10" id="blk_tyspup_01">
  <div class="t_name"><a href="http://video.sina.com.cn/sports/" target="_blank">体育视频</a></div>
  <div class="t_more"><a href="http://video.sina.com.cn/sports/" target="_blank">更多</a></div>
</div>

<div class="blk_31" id="blk_tysp_01" data-sudaclick="sports2_tysp">
  <div class="ct_p_06 clearfix" id="blk_xlsp_01">
<!--t id="news_web_get_gspsdata" pid="1" tid="920" did="4" fid="sp_f23511" cname="体育通栏_体育视频"-->
	
<div class="ct_box"><a href="http://video.sina.com.cn/p/sports/k/v/doc/2018-05-12/095668282652.html" target="_blank"><img width="105" height="79" alt="萌神库里三分18中18备战西决"  src="http://n.sinaimg.cn/sports/transform/749/w375h374/20180512/AnVw-hamfahw8524358.jpg"><s class="play_icon"></s><span class="ct_txt">萌神库里三分18中18备战西决</span></a></div><div class="ct_box"><a href="http://video.sina.com.cn/p/sports/j/v/doc/2018-05-11/115768264310.html" target="_blank"><img width="105" height="79" alt="&lt;咔咔野聊球&gt;上港俱乐部"  src="http://n.sinaimg.cn/sports/transform/164/w570h394/20180511/-7Ig-hamfahw2032763.jpg"><s class="play_icon"></s><span class="ct_txt">&lt;咔咔野聊球&gt;上港俱乐部</span></a></div><div class="ct_box"><a href="http://video.sina.com.cn/p/sports/go/v/doc/2018-05-04/144068229943.html" target="_blank"><img width="105" height="79" alt="体坛咖吧：很可能借AI作弊"  src="http://n.sinaimg.cn/sports/transform/320/w640h480/20180504/QR72-fzyqqiq8427754.jpg"><s class="play_icon"></s><span class="ct_txt">体坛咖吧：很可能借AI作弊</span></a></div><div class="ct_box"><a href="http://video.sina.com.cn/p/sports/j/v/doc/2018-05-02/074468226894.html" target="_blank"><img width="105" height="79" alt="&lt;咔咔·野聊球&gt;限薪令来"  src="http://n.sinaimg.cn/sports/transform/320/w640h480/20180502/Btre-fzyqqip7289086.jpg"><s class="play_icon"></s><span class="ct_txt">&lt;咔咔·野聊球&gt;限薪令来</span></a></div><div class="ct_box"><a href="http://video.sina.com.cn/p/sports/j/v/doc/2018-04-23/185068208137.html" target="_blank"><img width="105" height="79" alt="&lt;咔咔·野聊球&gt;复盘京穗"  src="http://n.sinaimg.cn/sports/transform/320/w640h480/20180423/7Jvb-fzqvvrz9977960.jpg"><s class="play_icon"></s><span class="ct_txt">&lt;咔咔·野聊球&gt;复盘京穗</span></a></div><div class="ct_box"><a href="http://video.sina.com.cn/p/sports/j/v/doc/2018-04-18/094968192047.html" target="_blank"><img width="105" height="79" alt="《咔咔·野聊球》麻酱VS油碟"  src="http://n.sinaimg.cn/sports/transform/320/w640h480/20180418/aBsN-fytnfyp7375489.jpg"><s class="play_icon"></s><span class="ct_txt">《咔咔·野聊球》麻酱VS油碟</span></a></div>
  </div>

  <ul class="list_12 link_c666" id="blk_xlty_02">
<li><a href="http://video.sina.com.cn/p/sports/laliga/v/doc/2017-08-30/120366985337.html" target="_blank">视频-皇马官方回顾阿森西奥4记世界波 潜质不输劳尔</a></li>

<li><a href="http://video.sina.com.cn/p/sports/laliga/v/doc/2017-08-30/104266984853.html"target="_blank" >视频-冠绝欧洲！皇马连续70场破门狂轰193球</a></li>

<li><a href="http://video.sina.com.cn/p/sports/g/v/doc/2017-08-30/095266983991.html"target="_blank">视频-欧足联年度最佳进球 曼朱欧冠惊天倒钩当选</a></li>  </ul>
</div>

    <div class="sp_h10"></div>
    <!-- 彩票信息 -->
<div class="Tit_08 t_mr10" id="blk_tyxwcpxxup_01">
  <div class="t_name"><a href="http://lottery.sina.com.cn/" target="_blank">彩票频道</a></div>
  <div class="t_more"><a href="http://lottery.sina.com.cn/" target="_blank">更多</a></div>
</div>

<div class="blk_32" id="blk_tyxwcpxx_01">
  <ul class="link_c666" data-sudaclick="sports2_cp">
<li><strong>[<a href="http://lottery.sina.com.cn/" target="_blank">头　条</a>]</strong> <a href="http://lottery.sina.com.cn/" >任性!老板3400万买彩中2000万 集资5亿终获刑
</a></li>

<li><strong>[<a href="http://lottery.sina.com.cn" target="_blank">球　通</a>]</strong> <a href="http://lottery.sina.com.cn/qiutong/" >新浪球通-专家好料推荐平台震撼上线</a> <a  href="http://sports.sina.com.cn/l/2018-04-12/doc-ifyzeyqa8896950.shtml"  >
使用说明</a></li>

<li><strong>[<a href="http://lottery.sina.com.cn" target="_blank">开　奖</a>]</strong> 
<a href="http://sports.sina.com.cn/lotto/">
后区全偶数 大乐透头奖空开 奖池涨至57.6亿</a></li>

<li><strong>[<a href="http://lottery.sina.com.cn/" target="_blank">智　能</a>]</strong> 
  <a  href="http://lottery.sina.com.cn/ai/"  >小炮智能预测足彩+NBA</a> <a  href="http://lottery.sina.com.cn/ai/cz/?price=4998"  >
最高充返1188</a> <a  href="http://lottery.sina.com.cn/ai/app/download/" target="_blank"  >下载App</a></li>

<li><strong>[<a href="http://lottery.sina.com.cn" target="_blank">行　业</a>]</strong> <a href="http://caitong.sina.com.cn/" >新浪彩通解读国内外彩票行业内幕</a> <a href="http://lotto.sina.cn/" >新版WAP更炫</a></li>

<li><strong>[<a href="http://sports.sina.com.cn/l/kaijiang/" target="_blank" >最　新</a>]</strong> <a href="http://sports.sina.com.cn/l/kaijiang/" target="_blank" >全国最全最快</a>:<a href="http://sports.sina.com.cn/l/kaijiang/detail.shtml?game=101" target="_blank">双色球</a> <a href="http://sports.sina.com.cn/l/kaijiang/detail.shtml?game=102" target="_blank">福彩3D</a> <a href="http://sports.sina.com.cn/l/kaijiang/detail.shtml?game=201" target="_blank">大乐透</a> <a href="http://sports.sina.com.cn/l/kaijiang/sfc.html" target="_blank">足彩</a> <a href="http://sports.sina.com.cn/l/kaijiang/detail.shtml?game=202" target="_blank">排列3</a></li>  </ul>
</div>


  <div>
<!--_SINA_ADS_BEGIN_-->
<!-- 340x120轮播体育左侧按钮广告 开始 -->
<div id="ad_47264">
<script async charset="utf-8" src="//d3.sina.com.cn/litong/zhitou/sinaads/release/sinaads.js"></script><ins class="sinaads" data-ad-pdps="PDPS000000047264"></ins><script>(sinaads = window.sinaads || []).push({});</script>
</div>
<!-- 340x120轮播体育左侧按钮广告 结束 -->
<!--_SINA_ADS_END_-->
  </div>

  <!-- left end -->
  </div>
  <div class="p_middle" data-sudaclick="sports2_list">
	
  <!-- middle begin -->

<!-- 篮球&NBA -->
<div class="Tit_06" id="blk_tyxwlqup_01">
  <div class="t_name"><a href="http://sports.sina.com.cn/nba/" target="_blank">篮球<span class="dot">·</span>NBA</a></div>
</div>
<div class="blk_33" id="blk_tyxwlq_01">
  <ul class="list_14">
<li><a href="http://sports.sina.com.cn/basketball/nba/2018-06-04/doc-ihcmurvh3377952.shtml" target="_blank">33+8+7！人类神仙三分精华 FMVP这次稳了吧</a></li><li><a href="http://sports.sina.com.cn/basketball/nba/2018-06-04/doc-ihcmurvh3344583.shtml" target="_blank">总决赛G2最大争议1球！詹姆斯被绊倒骑士却吃T</a></li><li><a href="http://sports.sina.com.cn/basketball/nba/2018-06-04/doc-ihcmurvh3291451.shtml" target="_blank">库里飙进9三分詹皇29分 勇士大胜骑士决赛2-0</a></li><li><a href="http://sports.sina.com.cn/basketball/nba/2018-06-04/doc-ihcmurvh3285539.shtml" target="_blank">库日天单场9三分！ 总决赛历史纪录被他踩脚下</a></li><li><a href="http://sports.sina.com.cn/basketball/nba/2018-05-31/doc-ihcffhsw0157813.shtml" target="_blank">勇士FMVP确定缺席总决赛G1！他缺阵胜率仅一半</a></li>
  </ul>
</div>
<!-- 国际足坛 -->
<div class="Tit_06" id="blk_tyxwgjztup_01">
  <div class="t_name"><a href="http://sports.sina.com.cn/global/" target="_blank">国际足坛</a></div>
</div>
<div class="blk_33" id="blk_tyxwgjzt_01">
  <ul class="list_14">
<li><a href="http://2018.sina.com.cn/arg/2018-06-04/doc-ihcmurvh3488005.shtml" target="_blank">梅西跟以色列踢友谊赛惹怒巴勒斯坦：烧光你球衣</a></li><li><a href="http://sports.sina.com.cn/g/pl/2018-06-04/doc-ihcmurvh2502922.shtml" target="_blank">穆帅:世界杯不是最高水平赛事 但影响力最大</a></li><li><a href="http://sports.sina.com.cn/g/pl/2018-06-04/doc-ihcmurvh2324562.shtml" target="_blank">穆里尼奥:C罗是葡萄牙领袖 世界杯能击败任何人</a></li><li><a href="http://sports.sina.com.cn/g/laliga/2018-06-04/doc-ihcmurvh1926950.shtml" target="_blank">热身-曼城核心助攻右翼替身进球 西班牙1-1瑞士</a></li><li><a href="http://sports.sina.com.cn/g/laliga/2018-06-04/doc-ihcmurvh1277782.shtml" target="_blank">热身赛-内马尔复出破僵局 巴西2-0胜克罗地亚</a></li>
  </ul>
</div>
<!-- 国内足坛 -->
<div class="Tit_06" id="blk_tyxwgnztup_01">
  <div class="t_name"><a href="http://sports.sina.com.cn/china/" target="_blank">国内足坛</a></div>
</div>
<div class="blk_33" id="blk_tyxwgnzt_01">
  <ul class="list_14">
<li><a href="http://sports.sina.com.cn/china/national/2018-06-04/doc-ihcmurvh4471690.shtml" target="_blank">王燊超为戴配饰上场道歉：意识错误 今后严于律己</a></li><li><a href="http://sports.sina.com.cn/china/j/2018-06-04/doc-ihcmurvh3636687.shtml" target="_blank">飞讯-恒大1200万年薪再追纳因 前中超金靴或回归</a></li><li><a href="http://sports.sina.com.cn/china/national/2018-06-04/doc-ihcmurvh2707104.shtml" target="_blank">郑智国足百场身后的命运多舛 恒大教练们如何夸他</a></li><li><a href="http://sports.sina.com.cn/china/national/2018-06-04/doc-ihcmurvh2482185.shtml" target="_blank">武磊：争取打进下一届世界杯 能力始终在泰国之上</a></li><li><a href="http://sports.sina.com.cn/china/zjclassic/2018-06-03/doc-ihcmurvh1130154.shtml" target="_blank">名宿谈中超争冠:恒大不改1点没戏 国安鲁能看好谁</a></li>
  </ul>
</div>
<!-- 综合体育 -->
<div class="Tit_06" id="blk_tyxwzhtyup_01">
  <div class="t_name"><a href="http://sports.sina.com.cn/others/" target="_blank">综合体育</a></div>
</div>
<div class="blk_33" id="blk_tyxwzhty_01">
  <ul class="list_14">
<li><a href="http://sports.sina.com.cn/others/pingpang/2018-06-04/doc-ihcmurvh1523512.shtml" target="_blank">张本智和：赢张继科后信心倍增 日本赛要击倒马龙</a></li><li><a href="http://sports.sina.com.cn/others/volleyball/2018-06-04/doc-ihcmurvh1752982.shtml" target="_blank">江川30分中国男排3-2法国 获男排联赛罗兹站第四</a></li><li><a href="http://sports.sina.com.cn/others/pingpang/2018-06-03/doc-ihcmurvh0994103.shtml" target="_blank">中乒赛马龙4-1胜樊振东称王 国乒包揽5项冠军</a></li>
  </ul>
</div>

  <!-- middle end -->
  

  </div>

<!--XBLK_STARTX-->
  <div class="p_right">
  <!-- right begin -->
    <!-- 他们在微博 -->

<div class="Tit_07" id="blk_tmzwbup_01">
  <div class="t_name"><a href="http://weibo.com/sportschannel" target="_blank">他们在微博</a></div>
</div>

<div class="blk_34" id="blk_tmzwb_01">
  <div class="b_cont" id="scrPic_tmzwb_01" data-sudaclick="sports2_weibo">


    <div class="b_box">
      <a class="twpic" target="_blank" href="http://weibo.com/warriors"><img width="50" height="50" alt="金州勇士的新浪微博" data-src="http://tvax1.sinaimg.cn/crop.41.36.322.322.50/e286b404ly8fqab0lcigxj20b40b40w0.jpg"></a>
      <div class="b_txt">
        <p><a target="_blank" href="http://weibo.com/warriors">金州勇士：</a><span class="link_c666"><a target="_blank" href="https://weibo.com/3800478724/GjMAkuGil">#NBA总决赛##金州勇士##库里# 邀您共享库里的三分球盛宴！http:/</a></span></p>
      </div>
    </div>    <div class="b_box">
      <a class="twpic" target="_blank" href="http://weibo.com/clevelandcavaliers"><img width="50" height="50" alt="克利夫兰骑士的新浪微博" data-src="http://tvax4.sinaimg.cn/crop.248.0.1583.1583.50/e286b988ly8fqarz39ni6j21kw17zqh4.jpg"></a>
      <div class="b_txt">
        <p><a target="_blank" href="http://weibo.com/clevelandcavaliers">克利夫兰骑士：</a><span class="link_c666"><a target="_blank" href="https://weibo.com/3800480136/GjMwIuWaE">回到主场，卷土重来，重整骑鼓！如果你依然相信骑士，请为我们点</a></span></p>
      </div>
    </div>    <div class="b_box">
      <a class="twpic" target="_blank" href="http://weibo.com/u/1320135280"><img width="50" height="50" alt="袁姗姗的新浪微博" data-src="http://tva3.sinaimg.cn/crop.0.0.1136.1136.50/4eafaa70jw8em0cj6p2nnj20vk0vk427.jpg"></a>
      <div class="b_txt">
        <p><a target="_blank" href="http://weibo.com/u/1320135280">袁姗姗：</a><span class="link_c666"><a target="_blank" href="https://weibo.com/1320135280/GjNyZ018m">非常感谢@NBA 欣赏了一场如此精彩的球赛 #NBA总决赛# 期待今年总</a></span></p>
      </div>
    </div>    <div class="b_box">
      <a class="twpic" target="_blank" href="http://weibo.com/sportschannel"><img width="50" height="50" alt="新浪体育的新浪微博" data-src="http://tva1.sinaimg.cn/crop.0.0.631.631.50/61add42ajw8f938lhtukrj20hj0hj76i.jpg"></a>
      <div class="b_txt">
        <p><a target="_blank" href="http://weibo.com/sportschannel">新浪体育：</a><span class="link_c666"><a target="_blank" href="https://weibo.com/1638781994/GjMg97F8Q">【库里纪录之夜！勇士主场再胜】#NBA总决赛# 第二场，勇士122-10</a></span></p>
      </div>
    </div>    <div class="b_box">
      <a class="twpic" target="_blank" href="http://weibo.com/u/1961800640"><img width="50" height="50" alt="王燊超_Alex的新浪微博" data-src="http://tva4.sinaimg.cn/crop.0.0.996.996.50/74eeb3c0jw8f7k55pubvnj20ro0ro773.jpg"></a>
      <div class="b_txt">
        <p><a target="_blank" href="http://weibo.com/u/1961800640">王燊超_Alex：</a><span class="link_c666"><a target="_blank" href="https://weibo.com/1961800640/GjNi9hZdW">随国家队从泰国集训回来了。在同缅甸的比赛中，我因为佩戴饰品，</a></span></p>
      </div>
    </div>    <div class="b_box">
      <a class="twpic" target="_blank" href="http://weibo.com/ITTFWorld"><img width="50" height="50" alt="ITTFWorld的新浪微博" data-src="http://tva4.sinaimg.cn/crop.0.0.936.936.50/d1845d57jw1e7bvxqg1t1j20q00q0q5c.jpg"></a>
      <div class="b_txt">
        <p><a target="_blank" href="http://weibo.com/ITTFWorld">ITTFWorld：</a><span class="link_c666"><a target="_blank" href="https://weibo.com/3515112791/GjHA40Y2w">#国际乒联巡回赛# #2018中国公开赛# 男单冠军自拍来啦！再次祝贺</a></span></p>
      </div>
    </div>

  </div>
</div>

<script type="text/javascript">
   jsLoader(ARTICLE_JSS.common,function(){
      var focusScroll = new ScrollPic();
      focusScroll.scrollContId  = "scrPic_tmzwb_01"; //内容容器ID

      focusScroll.frameWidth  = 243;//显示框宽度
      focusScroll.pageWidth = 243; //翻页宽度
      focusScroll.upright   = true; //垂直滚动
      focusScroll.speed   = 10; //移动速度(单位毫秒，越小越快)
      focusScroll.space   = 40; //每次移动像素(单位px，越大越快)
      focusScroll.autoPlay  = true; //自动播放
      focusScroll.autoPlayTime = 5; //自动播放间隔时间(秒)
      focusScroll.circularly  = true;
      focusScroll.initialize(); //初始化
    
  });
</script>



<!-- 体育专栏 -->
<!-- 体育专栏 -->
<!-- publish_helper name='sports_12_体育通栏_体育专栏' p_id='1' t_id='920' d_id='12' -->

<!--t id="news_web_get_gspsdata" pid="1" tid="920" did="12" fid="sp_f23511" cname="体育通栏_体育专栏"-->
	  <div class="Tit_07" id="blk_tyzlup_01">
  <div class="t_name"><a href="http://sports.sina.com.cn/zl/" target="_blank">体育专栏</a></div>
  <div class="t_more"><a href="http://sports.sina.com.cn/zl/" target="_blank">更多</a></div>
</div>

<div class="blk_26" id="blk_tyzl_01">
  <ul class="list_12 link_c666" data-sudaclick="sports2_zl">
	  <li><a title="为何要对里皮和国足吹毛求疵？" target="_blank" href="http://sports.sina.com.cn/zl/football/2018-06-04/zldoc-ihcmurvh2834006.shtml">为何要对里皮和国足吹毛求疵？</a></li><li><a title="安切洛蒂提前为将来执教中超铺路" target="_blank" href="http://sports.sina.com.cn/zl/football/2018-06-04/zldoc-ihcmurvh2777258.shtml">安切洛蒂提前为将来执教中超铺路</a></li><li><a title="状态火热的凯恩是整个英格兰的希望" target="_blank" href="http://sports.sina.com.cn/zl/football/2018-06-04/zldoc-ihcmurvh2748798.shtml">状态火热的凯恩是整个英格兰的希望</a></li><li><a title="武磊为什么能在国家队进球了？" target="_blank" href="http://sports.sina.com.cn/zl/football/2018-06-04/zldoc-ihcmurvh2698122.shtml">武磊为什么能在国家队进球了？</a></li><li><a title="刚成为神话的齐达内，为什么要走呢？" target="_blank" href="http://sports.sina.com.cn/zl/football/2018-06-04/zldoc-ihcmurvh2653205.shtml">刚成为神话的齐达内，为什么要走呢？</a></li>  </ul>
</div>


    <!-- 体育博客 -->

<div class="Tit_07" id="blk_mthzup_01">
  <div class="t_name"><a href="http://blog.sina.com.cn/lm/sports/" target="_blank">体育博客</a></div>
  <div class="t_more"><a href="http://blog.sina.com.cn/lm/sports/" target="_blank">更多</a></div>
</div>


<div class="blk_42" id="blk_spsc_03" data-sudaclick="sports2_blog" style="padding-top:16px;padding-bottom: 10px;">
<!-- publish_helper name='sports_9_体育通栏_体育博客' p_id='1' t_id='920' d_id='9' -->
<div class="ct_p_02 clearfix">

<div class="ct_box"><a href="http://blog.sina.com.cn/s/blog_536585320102xm6t.html" target="_blank"><img width="110" height="80"  src="http://n.sinaimg.cn/sports/transform/190/w110h80/20180528/O2er-hcaquev3948597.jpg"><span class="ct_txt">C罗表现不如3老</span></a></div>

<div class="ct_box"><a href="http://blog.sina.com.cn/s/blog_51ef9d460102yg66.html" target="_blank"><img width="110" height="80"  src="http://n.sinaimg.cn/sports/transform/190/w110h80/20180528/u1SX-hcaquev3954860.jpg"><span class="ct_txt">专访杨晨：谈青训</span></a></div>
</div>
  <ul class="list_12 link_c666">

<!--t id="news_web_get_gspsdata" pid="1" tid="920" did="9" fid="sp_f23508" cname="体育通栏_体育博客"-->
	  <li><a target="_blank" href="http://blog.sina.com.cn/s/blog_5a01615c0102xeob.html">裁判再成主角 红眼詹已无力对抗全世界</a></li><li><a target="_blank" href="http://blog.sina.com.cn/s/blog_536585320102xmnr.html">法国队替补的实力都比意大利强</a></li><li><a target="_blank" href="http://blog.sina.com.cn/s/blog_51ef9d460102ygu7.html">国足胜泰国 要相信里皮的执教能力</a></li>

  </ul>
</div>


  <!-- right end -->
  </div>
<!--XBLK_ENDX-->
</div>
<!-- part_sports end -->





<!-- AD tl05 begin -->
<!--XAD_STARTX-->
<!--_SINA_ADS_BEGIN_-->
<div><!-- 1000x90轮播通栏05广告 开始 -->
<div id="ad_47229">
  <script async charset="utf-8" src="//d5.sina.com.cn/litong/zhitou/sinaads/release/sinaads.js"></script><ins class="sinaads" data-ad-pdps="PDPS000000058105"></ins><script>(sinaads = window.sinaads || []).push({});</script>
</div></div>
<!--_SINA_ADS_END_-->
<!--XAD_ENDX-->
<!-- AD tl05 end -->





<!-- part_finance begin -->

<div class="partTit_01" id="blk_cjtltop_01"  data-sudaclick="fin2_tb">
  <div class="pT_name"><a href="http://finance.sina.com.cn/" target="_blank" class="titName ptn_31">财经新闻</a></div>
  <div class="pT_more"><a href="http://finance.sina.com.cn/china/" target="_blank">国内</a> | <a href="http://finance.sina.com.cn/guoji/" target="_blank">国际</a> | <a href="http://finance.sina.com.cn/chanjing/" target="_blank">产业</a> | <a href="http://finance.sina.com.cn/money/" target="_blank">理财</a> | <a href="http://finance.sina.com.cn/stock/" target="_blank">证券</a> | <a href="http://finance.sina.com.cn/fund/" target="_blank">基金</a> | <a href="http://finance.sina.com.cn/futuremarket/" target="_blank">期货</a> | <a href="http://finance.sina.com.cn/nmetal/" target="_blank">黄金</a> | <a href="http://finance.sina.com.cn/forex/" target="_blank">外汇</a> | <a href="http://finance.sina.com.cn/consume/" target="_blank">消费</a> &nbsp;&nbsp&nbsp;&nbsp;<a href="http://finance.sina.com.cn/" target="_blank">更多&gt;</a></div></div>


<div class="part_02 clearfix">
  <div class="p_left">
  <!-- left begin -->
<div class="Tit_08"  id="blk_czshup_01">
  <div class="t_name"><a href="http://slide.finance.sina.com.cn/hy/" target="_blank">财智生活</a></div>
  <div class="t_more"><a href="http://slide.finance.sina.com.cn/hy/" target="_blank">更多</a></div>
</div>

<div class="blk_76" id="blk_czsh_01"  data-sudaclick="fin2_czsh">

<a  href="http://finance.sina.com.cn/2018facetoface/" target="_blank"><img  src="http://n.sinaimg.cn/finance/490/w340h150/20180516/2mIf-fzrwiaz5469895.png" width="340" height="150" alt="潘石屹：房地产市场化对城市发展功不可没" /></a>
</div>

    <!-- 全球市场 begin -->

<div class="blk_fnc_01" data-sudaclick="blk_fnc_01">
  <div style="display:none;" id="tabss_script_loader"></div>
  <div class="blk_fnc_01_tit" id="blk_cjqqsc_01">
    <h4><a href="http://finance.sina.com.cn/money/globalindex/" target="_blank">全球市场</a></h4>
    <div class="blk_fnc_01_menu">
      <div class="default" id="tab_x_0" onmouseover="checkView(this);">股市</div>
      <div class="default" id="tab_x_1" onmouseover="checkView(this);">汇市</div>
      <div class="default" id="tab_x_2" onmouseover="checkView(this);" style="width:67px;">黄金原油</div>
      <div class="default" id="tab_x_3" onmouseover="checkView(this);">期指</div>
      <div class="default" id="tab_x_4" onmouseover="checkView(this);">期市</div>
    </div>
  </div>
  <div class="blk_fnc_01_cont clearfix">
    <div class="blk_fnc_01_list" id="blk_cjqqsc_02">
      <div class="default" id="tab_y_0" onmouseover="checkView(this);">
        <div class="border"></div>
        <div class="name">中国</div>
      </div>
      <div class="default" id="tab_y_1" onmouseover="checkView(this);">
        <div class="border"></div>
        <div class="name">亚太</div>
      </div>
      <div class="default" id="tab_y_2" onmouseover="checkView(this);">
        <div class="border"></div>
        <div class="name">北美</div>
      </div>
      <div class="default" id="tab_y_3" onmouseover="checkView(this);">
        <div class="border"></div>
        <div class="name">欧洲</div>
      </div>
    </div>
    <div class="blk_fnc_01_main" id="blk_cjqqsc_03">

<div id="tab_0" class="default" config="上证综指,sh000001,http://image.sinajs.cn/newchart/small/nsh000001.gif,http://finance.sina.com.cn/realstock/company/sh000001/nc.shtml,stock|深证成指,sz399001,http://image.sinajs.cn/newchart/small/nsz399001.gif,http://finance.sina.com.cn/realstock/company/sz399001/nc.shtml,stock"></div>

      <div id="tab_1" class="default" config="恒生指数,b_HSI,http://image.sinajs.cn/newchart/hk_stock/min_small/HSI.gif,http://finance.sina.com.cn/stock/hkstock/quote.html?code=HSI,int|日经指数,b_NKY,,,int"></div>

      <div id="tab_2" class="default" config="道琼斯,b_INDU,,http://finance.sina.com.cn/stock/usstock/US100_DJI.shtml,int|纳斯达克,b_CCMP,,http://finance.sina.com.cn/stock/usstock/US100_IXIC.shtml,int|标准普尔指数,b_SPX,,http://finance.sina.com.cn/stock/usstock/US100_INX.shtml,int|多伦多证交所指数,b_SPTSX,,,int"></div>

      <div id="tab_3" class="default" config="富时100指数,b_UKX,,,int|德国DAX指数,b_DAX,,,int|法国CAC40指数,b_CAC,,,int|富时意大利MIB指数,b_FTSEMIB,,,int"></div>

      <div id="tab_4" class="default" config="人民币,USDCNY,http://image.sinajs.cn/newchart/v5/forex/min30_m/USDCNY.gif,http://finance.sina.com.cn/money/forex/hq/USDCNY.shtml,forex|港币,HKD,http://image.sinajs.cn/newchart/v5/forex/min5_m/HKDCNY.gif,http://finance.sina.com.cn/money/forex/hq/HKDCNY.shtml,forex"></div>

      <div id="tab_5" class="default" config="日元,USDJPY,http://image.sinajs.cn/newchart/v5/forex/min5_m/USDJPY.gif,http://finance.sina.com.cn/money/forex/hq/USDJPY.shtml,forex|澳元,AUDUSD,http://image.sinajs.cn/newchart/v5/forex/min5_m/AUDUSD.gif,http://finance.sina.com.cn/money/forex/hq/AUDUSD.shtml,forex"></div>

      <div id="tab_6" class="default" config="美指,DINIW,http://image.sinajs.cn/newchart/v5/forex/min5_m/DINIW.gif,http://finance.sina.com.cn/money/forex/hq/DINIW.shtml,forex|加元,USDCAD,http://image.sinajs.cn/newchart/v5/forex/min5_m/USDCAD.gif,http://finance.sina.com.cn/money/forex/hq/USDCAD.shtml,forex"></div>

      <div id="tab_7" class="default" config="欧元,EURUSD,http://image.sinajs.cn/newchart/v5/forex/min5_m/EURUSD.gif,http://finance.sina.com.cn/money/forex/hq/EURUSD.shtml,forex|英镑,GBPUSD,http://image.sinajs.cn/newchart/v5/forex/min5_m/GBPUSD.gif,http://finance.sina.com.cn/money/forex/hq/GBPUSD.shtml,forex"></div>

      <div id="tab_8" class="default" config="黄金,hf_GC,http://image.sinajs.cn/newchart/v5/futures/global/mins/GC.gif,http://finance.sina.com.cn/futures/quotes/GC.shtml?GC,hk_futures|原油,hf_CL,http://image.sinajs.cn/newchart/v5/futures/global/mins/CL.gif,http://finance.sina.com.cn/futures/quotes/CL.shtml?CL,hk_futures"></div>

      <div id="tab_9" class="default" config="期指1707,CFF_IF1711,http://image.sinajs.cn/newchart/cffex/real/mins/IF1711.gif,http://finance.sina.com.cn/money/cffex/quotes/IF1707/nc.shtml,cffex|期指1709,CFF_IF1712,http://image.sinajs.cn/newchart/cffex/real/mins/IF1712.gif,http://finance.sina.com.cn/money/cffex/quotes/IF1709/nc.shtml,cffex"></div>

      <div id="tab_10" class="default" config="大豆连续,A0,http://image.sinajs.cn/newchart/v5/futures/mins/A0.gif,http://finance.sina.com.cn/futures/quotes/A0.shtml,futures|铜连续,CU0,http://image.sinajs.cn/newchart/v5/futures/mins/CU0.gif,http://finance.sina.com.cn/futures/quotes/CU0.shtml,futures"></div>

      <div id="tab_11" class="default" config="镍,hf_TRB,http://image.sinajs.cn/newchart/v5/futures/mins/NI0.gif,http://finance.sina.com.cn/futures/quotes/TRB.shtml,hk_futures|恒生指数期货,hf_HSI,http://image.sinajs.cn/newchart/v5/futures/global/mins/HSI.gif,http://finance.sina.com.cn/money/future/quote_hf.html?HSI,hk_futures"></div>

      <div id="tab_12" class="default" config="美黄豆,hf_S,http://image.sinajs.cn/newchart/v5/futures/global/mins/S.gif,http://finance.sina.com.cn/futures/quotes/S.shtml,hk_futures|美玉米,hf_C,http://image.sinajs.cn/newchart/v5/futures/global/mins/C.gif,http://finance.sina.com.cn/futures/quotes/C.shtml,hk_futures"></div>

      <div id="tab_13" class="default" config="伦铜,hf_CAD,http://image.sinajs.cn/newchart/v5/futures/global/mins/CAD.gif,http://finance.sina.com.cn/futures/quotes/CAD.shtml,hk_futures|伦铝,hf_AHD,http://image.sinajs.cn/newchart/v5/futures/global/mins/AHD.gif,http://finance.sina.com.cn/futures/quotes/AHD.shtml,hk_futures"></div>

      <div id="tab_14" class="default" config="伦敦金,hf_XAU,http://image.sinajs.cn/newchart/v5/futures/global/mins/XAU.gif,http://finance.sina.com.cn/futures/quotes/XAU.shtml,hk_futures|伦敦银,hf_XAG,http://image.sinajs.cn/newchart/v5/futures/global/mins/XAG.gif,http://finance.sina.com.cn/futures/quotes/XAG.shtml,hk_futures"></div>

      <div id="tab_15" class="default" config="黄金延期,SGE_AUTD,http://image.sinajs.cn/newchart/spot/gold/mins/AUTD.gif,http://finance.sina.com.cn/money/gold/AUTD/quote.shtml,SGE|白银延期,SGE_AGTD,http://image.sinajs.cn/newchart/spot/gold/mins/AGTD.gif,http://finance.sina.com.cn/money/gold/AGTD/quote.shtml,SGE"></div>
    </div>
  </div>
</div>
<script type="text/javascript">
  var checkViewTable = {
    "x": "-1", "y": "-1",
    "00": "0", "01": "1", "02": "2", "03": "3",
    "10": "4", "11": "5", "12": "6", "13": "7",
    "20": "15", "21": "-1", "22": "8", "23": "14",
    "30": "9", "31": "-1", "32": "-1", "33": "-1",
    "40": "10", "41": "11", "42": "12", "43": "13"
  };

  function $_id(id) {
    return document.getElementById(id);
  }

  function checkView(elem) {
    var arr = elem.id.split("_");
    var dirc = arr[1];
    var tag = arr[2];
    if (elem.className != "default") {return;}
    if (checkViewTable[checkViewTable["x"] + checkViewTable["y"]] != "-1") {
      $_id("tab_" + checkViewTable[checkViewTable["x"] + checkViewTable["y"]]).className = "default";
    }
    var theother = {"x": "y", "y": "x", "xcount": 4, "ycount": 5, "xid": "ti", "yid": "it"};
    var firstA = "-1";
    for (var i = 0; i < theother[dirc + "count"]; i++) {
      $_id("tab_" + theother[dirc] + "_" + i).className = "default";
      if (checkViewTable[theother[dirc + "id"].replace("t", tag).replace("i", i)] == "-1") {
        $_id("tab_" + theother[dirc] + "_" + i).className = "disabled";
        if (checkViewTable[theother[dirc]] == i) {checkViewTable[theother[dirc]] = "-1";}
      }
      else {firstA = i;}
    }
    if (checkViewTable[theother[dirc]] == -1) {checkViewTable[theother[dirc]] = firstA.toString();}
    $_id("tab_" + theother[dirc] + "_" + checkViewTable[theother[dirc]]).className = "active";
    $_id("tab_" + dirc + "_" + checkViewTable[dirc]).className = "default";
    elem.className = "active";
    checkViewTable[dirc] = tag.toString();
    $_id("tab_" + checkViewTable[checkViewTable["x"] + checkViewTable["y"]]).className = "active";
    if (tabSwitchController) {
      tabSwitchController.load();
    }
  }

  function initView(arr) {
    checkViewTable["x"] = arr[0].toString();
    $_id("tab_x_" + arr[0]).className = "active";
    checkViewTable["y"] = arr[1].toString();
    $_id("tab_y_" + arr[1]).className = "active";
    $_id("tab_" + checkViewTable[arr.join("")]).className = "active";
  }

  function processDataArray(data1, data2, data3, colors) {
    data3 = isNaN(data3 * 1) ? "--" : (data3*1).toFixed(2);
    if (data2 * 1 > 0) {
      data2 = "+" + data2;
      data3 = '<span class="' + colors[0] + '">+' + data3 + "%</span>";
    }
    if (data2 * 1 < 0) {
      data3 = '<span class="' + colors[1] + '">' + data3 + "%</span>";
    }
                if (data2 * 1 == 0) {
                        data3 = data3 + '%';
                }
    return [data1, data2, data3];
  }
  function processData(config) {
    var colors = ["green", "red"];
    switch (config[4]) {
      case "stock":
        // 证券简称,今日开盘价,昨日收盘价,最近成交价,最高成交价,最低成交价,买入价,卖出价,成交数量,成交金额,买数量一,买价位一,买数量二,买价位二,买数量三,买价位三,买数量四,买价位四,买数量五,买价位五,卖数量一,卖价位一,卖数量二,卖价位二,卖数量三,卖价位三,卖数量四,卖价位四,卖数量五,卖价位五,行情日期,行情时间
        var data = window["hq_str_" + config[1]].split(",");
        var data1 = (data[3] * 1).toFixed(2);
        var data2 = (data[3] - data[2]).toFixed(2);
        var data3 = (data[3] - data[2]) * 100 / (data[2] * 1);
        colors = ["red","green"];
        break;
      case "int":
        // 名字,最新价,涨跌额,涨跌幅
        var data = window["hq_str_" + config[1]].split(",");
        var data1 = data[1];
        var data2 = data[2];
        var data3 = data[3];
        break;
      case "forex":
        // 时间,买入价,卖出价,昨收盘,点差,开盘价,最高价,最低价,最新价,名称
        var data = window["hq_str_" + config[1]].split(",");
        var data1 = (data[8] * 1).toFixed(4);
        var data2 = (data[8] - data[3]).toFixed(4);
        var data3 = (data[8] - data[3]) * 100 / (data[3] * 1);
        break;
      case "futures":
        // name,CurrentTime,OpenPrice,HighPrice,LowPrice,ClosePrice,BidPrice,AskPrice,NewPrice,CurrentAccountsPrice,LastAccountsPrice,BidVol,AskVol,TotalVol,DealVol
        var data = window["hq_str_" + config[1]].split(",");
        var data1 = (data[8] * 1).toFixed(2);
        var data2 = (data[8] - data[10]).toFixed(2);
        var data3 = (data[8] - data[10]) * 100 / (data[10] * 1);
        break;
      case "hk_futures":
        // hf_name=LAST,CHANGE,BID,ASK,HIGH,LOW,TIMEUPDATE,Prev,Open,TOTALVOL,BIDSIZE,ASKSIZE
        var data = window["hq_str_" + config[1]].split(",");
        var data1 = (data[0] * 1).toFixed(2);
        var data2 = (data[0] * 1 - data[7] * 1).toFixed(2);
        var data3 = (data[0] * 1 - data[7] * 1) * 100 / (data[7] * 1);
        break;
      case "cffex":
        // CFF_合约代码=今开盘,最高价,最低价, 最新价,成交量,成交金额,持仓量,今收盘,今结算,涨停板价,跌停板价,昨虚实度,今虚实度, 昨收盘,昨结算,昨持仓量,申买价一,申买量一,申买价二,申买量二, 申买价三,申买量三,申买价四,申买量四,申买价五,申买量五,申卖价一,申卖量一, 申卖价二,申卖量二,申卖价三,申卖量三,申卖价四,申卖量四,申卖价五,申卖量五,交易日,行情时间,行情时间毫秒
        var data = window["hq_str_" + config[1]].split(",");
        var data1 = (data[3] * 1).toFixed(2);
        var data2 = (data[3] - data[14]).toFixed(2);
        var data3 = (data[3] - data[14]) * 100 / (data[14] * 1);
        colors = ["red","green"];
        break;
    case 'SGE':
        var data = window["hq_str_" + config[1]].split(",");
        var data1 = (data[3] * 1).toFixed(2);
        var data2 = (data[3] - data[9]).toFixed(2);
        var data3 = (data[3] - data[9]) * 100 / (data[9] * 1);
        colors = ["red","green"];
        break;
      default:
        var data1 = "--";
        var data2 = "--";
        var data3 = "--";
    }
    return processDataArray(data1, data2, data3, colors);
  }
  var TabSwitchController = function (loader, targets) {
    this.elementLoader = loader;
    this.loadHQ = function (target) {
      var element = document.createElement("script");
      element.type = "text/javascript";
      element.charset = "gb2312";
      element.src = "//hq.sinajs.cn/rn=" + (new Date()).getTime() + "&list=" + target.list;
      element.object = this;
      element.target = target;
      element[document.all ? "onreadystatechange" : "onload"] = function () {
        if (document.all && this.readyState != "loaded" && this.readyState != "complete") {
          return;
        }
        var target = this.target;
        for (var i = 0; i < target.config.length; i++) {
          var data = processData(target.config[i]);
          target.lines[i][1].innerHTML = data[0];
          if (target.lines[i][2]) {
            target.lines[i][2].innerHTML = data[1];
          }
          target.lines[i][3].innerHTML = data[2];
        }
        this[document.all ? "onreadystatechange" : "onload"] = null;
        this.parentNode.removeChild(this);
      };
      this.elementLoader.appendChild(element);
    };
    this.targets = targets;
    this.load = function () {
      var object = arguments.callee.object;
      var targets = object.targets;
      for (var i = 0; i < targets.length; i++) {
        var target = targets[i];
        var config = target.getAttribute("config");
        if (target.className == "active") {
          if (target.innerHTML == "") {
            var arrayConfig = config.split("|");
            var targetTable = document.createElement("table");
            targetTable.cellPadding = 0;
            targetTable.cellSpacing = 0;
            target.lines = [];
            target.config = [];
            target.list = ""
            if (arrayConfig.length > 2) {
              targetTable.className = "table";
              targetTable.style.marginTop = "8px";
              for (var j = 0; j < arrayConfig.length; j++) {
                var stockConfig = arrayConfig[j].split(",");
                target.config.push(stockConfig);
                target.list += stockConfig[1] + ",";
                var tempTr1 = targetTable.insertRow(-1);
                tempTr1.className = "current";
                var tempName = tempTr1.insertCell(-1);
                tempName.className = "left";
                tempName.colSpan = 3;
                var tempNameLink = document.createElement("a");
                tempNameLink.target = "_blank";
                if (stockConfig[3]) {
                  tempNameLink.href = stockConfig[3];
                }
                tempNameLink.innerHTML = stockConfig[0];
                tempName.appendChild(tempNameLink);
                var tempTr2 = targetTable.insertRow(-1);
                var tempPrice = tempTr2.insertCell(-1);
                var tempPriceVolume = tempTr2.insertCell(-1);
                var tempPricePercent = tempTr2.insertCell(-1);
                target.lines.push([tempTr, tempPrice, tempPriceVolume, tempPricePercent]);
              }
              target.appendChild(targetTable);
            }
            else {
              targetTable.className = "table";
              for (var j = 0; j < arrayConfig.length; j++) {
                var stockConfig = arrayConfig[j].split(",");
                target.config.push(stockConfig);
                target.list += stockConfig[1] + ",";
                var tempTr = targetTable.insertRow(-1);
                tempTr.target = target;
                if (stockConfig[2]) {
                  var tempImageLink = document.createElement("a");
                  tempImageLink.className = "image";
                  tempImageLink.target = "_blank";
                  if (stockConfig[3]) {
                    tempImageLink.href = stockConfig[3];
                  }
                  var tempImage = document.createElement("img");
                  tempImage.src = stockConfig[2] + "?" + (new Date()).getTime();
                  tempImage.linkElement = tempImageLink;
                  tempImageLink.appendChild(tempImage);
                  tempImageLink.style.display = "none";
                  target.appendChild(tempImageLink);
                  tempTr.imageLink = tempImageLink;
                  tempTr.image = tempImage;
                  tempTr.style.cursor = "pointer";
                  tempTr.thread = -1;
                  tempTr.switchLine = function () {
                    var tr = arguments.callee.tr;
                    tr.thread = -1;
                    if (tr.target.currentLine) {
                      tr.target.currentLine.className = "";
                      tr.target.currentLine.imageLink.style.display = "none";
                      if (!tr.image.last) {
                        tr.image.last = (new Date()).getTime();
                      }
                    }
                    tr.className = "current";
                    tr.imageLink.style.display = "";
                    var rn = (new Date()).getTime();
                    if (rn - tr.image.last > 30000) {
                      tr.image.src = tr.image.src.replace(/\?\d*$/, "?" + rn);
                      tr.image.last = rn;
                    }
                    tr.target.currentLine = tr;
                  };
                  tempTr.switchLine.tr = tempTr;
                  tempTr.onmouseover = function () {
                    this.thread = setTimeout(this.switchLine, 200);
                  };
                  tempTr.onmouseout = function () {
                    if (this.thread != -1) {clearTimeout(this.thread);}
                  };
                }
                var tempName = tempTr.insertCell(-1);
                tempName.className = "name";
                var tempNameLink = document.createElement("a");
                tempNameLink.target = "_blank";
                if (stockConfig[3]) {
                  tempNameLink.href = stockConfig[3];
                }
                tempNameLink.innerHTML = stockConfig[0];
                tempName.appendChild(tempNameLink);
                var tempPrice = tempTr.insertCell(-1);
                var tempPricePercent = tempTr.insertCell(-1);
                target.lines.push([tempTr, tempPrice, null, tempPricePercent, (stockConfig[2] ? tempImage : false)]);
              }
              target.appendChild(targetTable);
              for (var j = 0; j < target.lines.length; j++) {
                if (target.lines[j][0].image) {
                  target.currentLine = target.lines[j][0];
                  target.currentLine.className = "current";
                  target.currentLine.imageLink.style.display = "";
                  break;
                }
              }
            }
            target.list = target.list.replace(/,$/, "")
            object.loadHQ(target);
          }
          else {
            var now = new Date();
            if (now.getSeconds() < 30 && now.getMinutes() % 3 == 0) {
              var rn = now.getTime();
              for (var j = 0; j < target.lines.length; j++) {
                if (target.lines[j][4] && target.lines[j][4].linkElement.style.display == "") {
                  target.lines[j][4].src = target.config[j][2] + "?" + rn;
                  target.lines[j][4].last = (new Date()).getTime();
                }
              }
            }
            object.loadHQ(target);
          }
          break;
        }
      }
    };
    this.load.object = this;
    this.start = function () {
      this.load();
      setInterval(this.load, 30000);
    }
  }
var tabSwitchController = new TabSwitchController($_id("tabss_script_loader"),[$_id("tab_0"),$_id("tab_1"),$_id("tab_2"),$_id("tab_3"),$_id("tab_4"),$_id("tab_5"),$_id("tab_6"),$_id("tab_7"),$_id("tab_8"),$_id("tab_9"),$_id("tab_10"),$_id("tab_11"),$_id("tab_12"),$_id("tab_13"),$_id("tab_14"),$_id("tab_15")]);
  initView([0, 0]);
  tabSwitchController.start();
</script>


    <!-- 全球市场 end -->
    <div class="sp_h10"></div>
    <!-- 大盘评述 -->

<div class="TMenu_05" id="blk_dppsup_01" >
  <ul>
    <li id="tab_dpps_01" class="selected"><a href="http://roll.finance.sina.com.cn/finance/zq1/gsjsy/index.shtml" target="_blank">大盘评述</a></li>
    <li id="tab_dpps_02"><a href="http://blog.sina.com.cn/lm/stock/" target="_blank">博客看市</a></li>
  </ul>
  <div class="t_more"><a href="http://blog.sina.com.cn/lm/stock/" target="_blank">更多</a></div>
</div>



<div class="blk_32" id="blk_dpps_01">
  <ul class="list_12 link_c666" data-sudaclick="fin2_dpps">

<!--t id="news_web_get_gspsdata" pid="1" tid="921" did="4" fid="sp_f23539" cname="财经通栏_大盘评述"-->
	  			<li><a href="http://blog.sina.com.cn/s/blog_98708c450102xvkg.html" target="_blank" >明天将有巨震 白马开始回归</a><span class="time"> 19:52</span></li>			<li><a href="http://blog.sina.com.cn/s/blog_66dd17cd0102xjnv.html" target="_blank" >下半周将有转机 明天茅台将破万亿？</a><span class="time"> 19:34</span></li>			<li><a href="http://blog.sina.com.cn/s/blog_165dba4cf0102xt0b.html" target="_blank" >证监会罕见发声 一类股紧急撤离</a><span class="time"> 15:45</span></li>			<li><a href="http://finance.sina.com.cn/stock/jsy/2018-06-04/doc-ihcmurvh5277007.shtml" target="_blank" >A股成交量259.95亿股 成交金额3454.51亿股</a><span class="time"> 15:21</span></li>

  </ul>
</div>


<div class="blk_32" id="blk_dpps_02" style="display:none;">
  <ul class="list_12 link_c666" data-sudaclick="fin2_bkks">

<!--t id="news_web_get_gspsdata" pid="1" tid="921" did="5" fid="sp_f23539" cname="财经通栏_博客看市"-->
				<li><a href="http://blog.sina.com.cn/s/blog_a2b12e010102xp7d.html" target="_blank" >A股入摩后资金面逐步改善 看好6月份行情</a><span class="time"><a href="http://blog.sina.com.cn/u/2729520641" target="_blank">众禄金融</a></span></li>			<li><a href="http://blog.sina.com.cn/s/blog_98708c450102xvkg.html" target="_blank" >明天将有巨震 白马开始回归</a><span class="time"><a href="http://blog.sina.com.cn/u/2557512773" target="_blank">天策府</a></span></li>			<li><a href="http://blog.sina.com.cn/s/blog_e0a1a53c0102xnuy.html" target="_blank" >大盘继续向上 明日重点关注这一板块</a><span class="time"><a href="http://blog.sina.com.cn/u/3768689980" target="_blank">股牛仔</a></span></li>			<li><a href="http://blog.sina.com.cn/s/blog_12e5ce83a0102xak7.html" target="_blank" >3000点附近大盘难有下行空间</a><span class="time"><a href="http://blog.sina.com.cn/u/5072807994" target="_blank">大满贯股</a></span></li>
  </ul>
</div>

    <script type="text/javascript">
       jsLoader(ARTICLE_JSS.common,function(){
          var subshow = new SubShowClass('none','onmouseover');
          subshow.addLabel('tab_dpps_01','blk_dpps_01');
          subshow.addLabel('tab_dpps_02','blk_dpps_02');
      });
    </script>
  <!-- left end -->
  </div>
  <div class="p_middle" data-sudaclick="fin2_list">
  <!-- middle begin -->


<!--t id="news_web_get_gspsdata" pid="1" tid="921" did="6" fid="sp_f23539" cname="财经通栏_中部列表"-->
	

<!-- 国内国际财经 -->
<div class="Tit_06" id="blk_cjxwgngjcjup_01">
  <div class="t_name"><a href="http://finance.sina.com.cn/china/" target="_blank">国内</a><span class="dot">·</span><a href="http://finance.sina.com.cn/world/" target="_blank">国际财经</a></div>
  <div class="t_more"><a href="http://finance.sina.com.cn/china/" target="_blank">更多</a></div>
</div>
<div class="blk_36" id="blk_cjxwgngjcj_01">
  <ul class="list_14">
			<li><a href="http://finance.sina.com.cn/chanjing/gsnews/2018-06-04/doc-ihcmurvh7162133.shtml" target="_blank" >范冰冰无锡公司纳税数据曝光：收入3500万但纳税0元</a><span class="time"> 19:56</span></li>			<li><a href="http://finance.sina.com.cn/world/2018-06-04/doc-ihcmurvh6919733.shtml" target="_blank" >国税总局发话查阴阳合同！影视股一天蒸发了百亿市值</a><span class="time"> 19:13</span></li>			<li><a href="http://finance.sina.com.cn/review/sbzt/2018-06-04/doc-ihcmurvh5712901.shtml" target="_blank" >即便崔永元说错了 范冰冰们天价片酬就拿得理所应当?</a><span class="time"> 16:17</span></li>			<li><a href="http://finance.sina.com.cn/chanjing/gsnews/2018-06-04/doc-ihcmurvh5449806.shtml" target="_blank" >兰陵美酒改制迷局:国有股拍卖牵出数千万国资0元转让</a><span class="time"> 15:43</span></li>			<li><a href="http://finance.sina.com.cn/china/2018-06-04/doc-ihcmurvh4788870.shtml" target="_blank" >下个月你的住房公积金或将调整 快看将如何变动？</a><span class="time"> 14:11</span></li>			<li><a href="http://finance.sina.com.cn/roll/2018-06-04/doc-ihcmurvh4621224.shtml" target="_blank" >楼市摇号抢购潮背后：市场上钱多又无更好投资途径</a><span class="time"> 13:48</span></li>  </ul>
</div>

<!-- 股票 -->
<div class="Tit_06" id="blk_cjxwgpggmgup_01">
  <div class="t_name"><a href="http://finance.sina.com.cn/stock/" target="_blank">股票</a><span class="dot">·</span><a href="http://finance.sina.com.cn/stock/hkstock/" target="_blank">港股</a><span class="dot">·</span><a href="http://finance.sina.com.cn/stock/usstock/" target="_blank">美股</a></div>
  <div class="t_more"><a href="http://finance.sina.com.cn/stock/" target="_blank">更多</a></div>
</div>
<div class="blk_36" id="blk_cjxwgpggmg_01">
  <ul class="list_14">
			<li><a href="http://finance.sina.com.cn/stock/s/2018-06-04/doc-ihcmurvh4467556.shtml" target="_blank" >上海深坑酒店转让背后 世茂集团同业竞争难题待解</a><span class="time"> 13:25</span></li>			<li><a href="http://finance.sina.com.cn/stock/marketresearch/2018-06-04/doc-ihcmurvh4276667.shtml" target="_blank" >行业“利空”冲击A股光伏板块 隆基股份等10股跌停</a><span class="time"> 12:49</span></li>			<li><a href="http://finance.sina.com.cn/stock/s/2018-06-04/doc-ihcmurvh3044568.shtml" target="_blank" >华谊兄弟等影视股大跌 超一线明星究竟收入几何？</a><span class="time"> 10:08</span></li>			<li><a href="http://finance.sina.com.cn/stock/marketresearch/2018-06-04/doc-ihcmurvh3030255.shtml" target="_blank" >皮海洲：33只不死鸟表明A股退市制度有待进一步完善</a><span class="time"> 10:02</span></li>			<li><a href="http://finance.sina.com.cn/stock/s/2018-06-04/doc-ihcmurvh2697343.shtml" target="_blank" >RIO锐澳从百亿单品到一夜崩盘 实控人能否玩出新花样</a><span class="time"> 09:17</span></li>			<li><a href="http://finance.sina.com.cn/stock/s/2018-06-04/doc-ihcmurvh2401671.shtml" target="_blank" >三聚环保复牌放大招 海淀国资收购公司80亿应收账款</a><span class="time"> 08:18</span></li>			<li><a href="http://finance.sina.com.cn/stock/s/2018-06-04/doc-ihcmurvh2388118.shtml" target="_blank" >康得新为何一年不到三次闪崩 市值缩水400亿？</a><span class="time"> 08:14</span></li>  </ul>
</div>
<!-- 理财 生活 -->
<div class="Tit_06" id="blk_cjxwlcshup_01">
  <div class="t_name"><a href="http://finance.sina.com.cn/money/" target="_blank">理财</a><span class="dot">·</span><a href="http://finance.sina.com.cn/consume/" target="_blank">生活</a></div>
  <div class="t_more"><a href="http://finance.sina.com.cn/consume/" target="_blank">更多</a></div>
</div>
<div class="blk_36" id="blk_cjxwlcsh_01">
  <ul class="list_14">
			<li><a href="http://finance.sina.com.cn/money/lczx/2018-06-01/doc-ihcikcev8297979.shtml" target="_blank" >美女加微信骗局起底:周期60天 背后都是“抠脚大叔”</a><span class="time"> 04:28</span></li>			<li><a href="http://finance.sina.com.cn/money/bank/bank_hydt/2018-05-31/doc-ihcffhsw0270857.shtml" target="_blank" >5月31日在售高收益银行理财产品一览</a><span class="time"> 07:07</span></li>
			<li><a href="http://finance.sina.com.cn/consume/puguangtai/2018-06-04/doc-ihcmurvh6535832.shtml" target="_blank" >这类热销儿童床被检出多款产品存安全隐患！(附名单)</a><span class="time"> 18:07</span></li>			<li><a href="http://finance.sina.com.cn/china/dfjj/2018-06-04/doc-ihcmurvh2090104.shtml" target="_blank" >湖南株洲药企超标污水排湘江 环保局长前后说法不一</a><span class="time"> 06:11</span></li>  </ul>
</div>


  <!-- middle end -->
  </div>
<!--XBLK_STARTX-->
  <div class="p_right bgc_f6f6f6">
  <!-- right begin -->
    <!-- 财经新闻排行 -->

<div class="Tit_07" id="blk_cjxwphup_01">
  <div class="t_name"><a href="http://finance.sina.com.cn/topnews/" target="_blank">财经新闻排行</a></div>
  <div class="t_more"><a href="http://finance.sina.com.cn/topnews/" target="_blank">更多</a></div>
</div>

<div class="blk_37" id="blk_cjxwph_01">
  <ol class="topList_12 link_c666" id="blk_cjxwph_011"  data-sudaclick="fin2_hot"></ol>
    <!-- 财经 begin -->
    <script type="text/javascript">

      jsLoader({
        url : '//top.finance.sina.com.cn/ws/GetTopDataList.php?top_type=day&top_cat=finance_0_suda&top_time=today&top_show_num=6&top_order=DESC&js_var=all_1_data&short_title=1&call_back=showContent10'
      })
      function showContent10(data_arr) {
    
        var html= '';
        data = data_arr['data'];
        var nu = 0;
        for(var i in data){
          ++nu;
          var tmptitle = data[i].title;
          if (nu<4) {
            html += '<li><span class="topNum num'+nu+'">'+nu+'</span><a target="_blank" href="'+data[i].url+'">'+data[i].title.gbCut(35)+'</a></li>';
          } else {
            html += '<li><span class="topNum">'+nu+'</span><a target="_blank" href="'+data[i].url+'">'+data[i].title.gbCut(35)+'</a></li>';
          }
        }
        document.getElementById('blk_cjxwph_011').innerHTML = html;
      }
    </script>
    <!-- 财经 end -->

</div>

    <!-- 天下财经 -->

<div class="Tit_07" id="blk_txcjup_01">
  <div class="t_name"><a href="http://slide.finance.sina.com.cn/" target="_blank">天下财经</a></div>
  <div class="t_more"><a href="http://slide.finance.sina.com.cn/" target="_blank">更多</a></div>
</div>

<div class="blk_38">
<div class="b_cont" id="blk_txcj_01">
    <div class="ct_p_05 clearfix" id="scrPic_txcj_01"  data-sudaclick="fin2_txcj">
<div class="ct_pic"><a href="http://slide.finance.sina.com.cn/slide_9_86514_530116.html#p=1" target="_blank"><img src="http://n.sinaimg.cn/finance/384/w240h144/20180604/hx-d-hcmurvh7410784.jpg" width="240" height="144" alt="" /><span class="ct_txt">90后上海美女靠干这一行年入800万</span></a></div>
<div class="ct_pic"><a href="http://slide.finance.sina.com.cn/slide_9_86514_529952.html#p=1" target="_blank"><img src="http://n.sinaimg.cn/finance/384/w240h144/20180601/BoBe-hcikcew3051258.jpg" width="240" height="144" alt="" /><span class="ct_txt">石家庄现最贵麦田 周边房价均价1万5</span></a></div>
<div class="ct_pic"><a href="http://slide.finance.sina.com.cn/slide_9_86514_528839.html#p=1" target="_blank"><img src="http://n.sinaimg.cn/finance/384/w240h144/20180525/Cfbi-fzrwiaz5912059.jpg" width="240" height="144" alt="" /><span class="ct_txt">女子5万卖亲生女 转头花6千买化妆品</span></a></div>
<div class="ct_pic"><a href="http://slide.finance.sina.com.cn/slide_9_86514_528207.html#p=1" target="_blank"><img src="http://n.sinaimg.cn/finance/384/w240h144/20180521/WY_H-hawmaua0553209.jpg" width="240" height="144" alt="" /><span class="ct_txt">美国这家餐厅女服务员配枪上岗</span></a></div>
    </div>
    <a href="javascript:void(0)" class="scrArrAbsLeft" id="scrArrLeft_txcj_01"></a>
    <a href="javascript:void(0)" class="scrArrAbsRight" id="scrArrRight_txcj_01"></a>
  </div>
  <div class="b_cons">
    <span class="scrDotList" id="scrDotList_txcj_01">
      <span></span>
    </span>
  </div>
</div>

<script type="text/javascript">
   jsLoader(ARTICLE_JSS.common,function(){
      var focusScroll = new ScrollPic();
      focusScroll.scrollContId  = "scrPic_txcj_01"; //内容容器ID

      focusScroll.dotListId   = "scrDotList_txcj_01";//点列表ID
      focusScroll.dotClassName  = "";//点className
      focusScroll.dotOnClassName = "on";//当前点className
      focusScroll.listType  = "";//列表类型(number:数字，其它为空)
      focusScroll.listEvent = "onmouseover"; //切换事件

      focusScroll.frameWidth  = 240;//显示框宽度
      focusScroll.pageWidth = 240; //翻页宽度
      focusScroll.upright = false; //垂直滚动
      focusScroll.speed   = 10; //移动速度(单位毫秒，越小越快)
      focusScroll.space   = 40; //每次移动像素(单位px，越大越快)
      focusScroll.autoPlay  = false; //自动播放
      focusScroll.autoPlayTime = 5; //自动播放间隔时间(秒)
      focusScroll.circularly = true;
      focusScroll.initialize(); //初始化
      document.getElementById('scrArrLeft_txcj_01').onmousedown = function(){
        focusScroll.pre();
        return false;
      }
      document.getElementById('scrArrRight_txcj_01').onmousedown = function(){
        focusScroll.next();
        return false;
      }
    
  });
</script>

    <!-- 高尔夫 -->
<div class="Tit_07" id="blk_cjxwgolfup_01">
  <div class="t_name"><a href="http://golf.sina.com.cn/" target="_blank">高尔夫</a></div>
  <div class="t_more"><a href="http://golf.sina.com.cn/" target="_blank">更多</a></div>
</div>

<div class="blk_39" id="blk_cjxwgolf_01" data-sudaclick="golfblk">

  <div class="ct_pt_07 clearfix">
    <div class="ct_pic"><a href="http://slide.sports.sina.com.cn/golf/slide_2_754_84164.html?img=1536535#p=1" target="_blank"><img src="http://www.sinaimg.cn/dy/temp/920/2013/0531/U2329P1T920D10F23498DT20150701172454.jpg" width="110" height="80" alt=""><span class="ct_tit">徕卡下的斯皮思</span></a></div>
    <div class="ct_txt">
      <ul class="list_12 link_c666">
<li><a href="http://golf.sina.com.cn/pgatour.html" target="_blank">斯皮思获第2高积分</a></li>


<li><a href="http://sports.sina.com.cn/golf/2015clpga/" target="_blank" >冯珊珊重返锦湖韩亚</a></li>

<li><a href="http://sports.sina.com.cn/golf/2015-07-01/09317645650.shtml" target="_blank">冯力源:想执裁奥运会</a></li>

<li><a href="http://slide.sports.sina.com.cn/golf/slide_2_754_84167.html#p=1" target="_blank">星辰下跃动的高尔夫</a></li>




</ul>
</div>
</div>
<ul class="list_12 link_c666">

<li><a href="http://sports.sina.com.cn/golf/2015-07-01/09267645645.shtml" target="_blank">美国断腿伤兵获外卡角逐威巡赛</a></li>

</ul>

</div>


  <!-- right end -->
  </div>

<!--XBLK_ENDX-->
</div>
<!-- part_finance end -->


<!-- AD tl06 begin -->
<!--XAD_STARTX-->
<!--_SINA_ADS_BEGIN_-->
<div><!-- 1000x90轮播通栏06广告 开始 -->
<div id="ad_47232">
  <script async charset="utf-8" src="//d5.sina.com.cn/litong/zhitou/sinaads/release/sinaads.js"></script><ins class="sinaads" data-ad-pdps="PDPS000000047232"></ins><script>(sinaads = window.sinaads || []).push({});</script>
</div></div>
<!--_SINA_ADS_END_-->
<!--XAD_ENDX-->
<!-- AD tl06 end -->


<div class="sp_h20"></div>

<!-- gsps收藏通栏 p_id=1&t_id=912&f_id=28327 -->
<!--t id="news_web_get_gspsdata" pid="1" tid="912" did="1" fid="sp_f28327" cname="收藏通栏"}}-->

<!-- part_collection begin -->
<div class="partTit_02" id="blk_spsctltop_01"  data-sudaclick="style2_tb">
	<div class="pT_name"><a href="http://collection.sina.com.cn/" target="_blank" class="titName ptn_33">收藏</a></div>
	<div class="pT_more"><a target="_blank" href="http://collection.sina.com.cn/ysmjrw/">艺术名家人物库</a> | <a target="_blank" href="http://data.collection.sina.com.cn/">艺术品行情数据库</a> | <a target="_blank" href="http://store.collection.sina.com.cn/art/index.php?retcode=0">藏品在线</a> | <a target="_blank" href="http://slide.collection.sina.com.cn/">高清图集</a> | <a target="_blank" href="http://blog.sina.com.cn/lm/collection/">收藏博客频道</a> | <a target="_blank" href="http://roll.collection.sina.com.cn/collection/zwyp/index.shtml">中外邮票</a> | <a target="_blank" href="http://roll.collection.sina.com.cn/collection/qbtd/index.shtml">钱币天地</a>  &nbsp;&nbsp&nbsp;&nbsp;<a target="_blank" href="http://collection.sina.com.cn/">更多&gt;</a></div>
</div>

<div class="part_03 clearfix">
	<div class="p_left" data-sudaclick="style2_01">
		<!-- left begin -->
		
<div class="blk_40" id="blk_spsc_01">
	<div class="ct_pt_07 clearfix">
		<div class="ct_pic">
			<a href="http://collection.sina.com.cn/cqyw/2018-06-01/doc-ihcikcev6110304.shtml"target="_blank"><img src="http://n.sinaimg.cn/collect/transform/500/w300h200/20180601/KgAh-hcikcev9893410.jpg" width="150"height="100" alt=""><span class="ct_tit">维米尔笔下怯怯凝视着的女孩 是否真嫁了个屠户</span></a>		</div>
		<div class="ct_txt">
			<ul class="list_12 link_c666">
				<li><a href="http://collection.sina.com.cn/yjjj/2018-06-03/doc-ihcmurvf6907843.shtml" target="_blank">北庭故城新出土数件文物</a></li><li><a href="http://collection.sina.com.cn/yjjj/2018-06-03/doc-ihcmurvf7083839.shtml" target="_blank">广西贵港旧城区挖出汉代护城壕</a></li><li><a href="http://collection.sina.com.cn/yjjj/2018-06-03/doc-ihcmurvf6899304.shtml" target="_blank">吉林汪清发现12处旧石器时代遗址</a></li><li><a href="http://collection.sina.com.cn/yjjj/2018-06-03/doc-ihcmurvf6885598.shtml" target="_blank">唐宋坊市遗址再现</a></li><li><a href="http://collection.sina.com.cn/yjjj/2018-05-31/doc-ihcffhsv7359698.shtml" target="_blank">朝阳消防支队开展文物古建消防安全专项行动</a></li>			</ul>
		</div>
	</div>
	<ul class="list_12 link_c666">
		<li><a href="http://collection.sina.com.cn/auction/pmgg/2018-06-01/doc-ihcikcev9523372.shtml" target="_blank">近代儒学第一人：马一浮赠毛主席周总理对联将拍卖</a></li><li><a href="http://collection.sina.com.cn/cjrw/2018-05-31/doc-ihcffhsw0912588.shtml" target="_blank">蔡康永：当代艺术很叛逆 但也可以很温柔</a></li>	</ul>
</div>
		<!-- left end -->
	</div>
	<div class="p_middle">
		<!-- middle begin -->

		<div class="blk_41" id="blk_spsc_02">
			<ul id="blk_spsc_021" data-sudaclick="style2_list">
				<li><a target="_blank" href="http://roll.collection.sina.com.cn/collection/yjjj/index.shtml">独家|</a>  <a target="_blank" href="http://collection.sina.com.cn/yjjj/2018-05-30/doc-ihcffhsv7559940.shtml" class="linkRed">艺术家发声回应演员袁立质疑</a> <a target="_blank" href="https://weibo.com/1195300800/Gj5BIrMKd?from=page_1006051195300800_profile&wvr=6&mod=weibotime&type=comment#_rnd1527734988450" class="linkRed">袁立回应事情经过</a></li>

<li><a target="_blank" href="http://roll.collection.sina.com.cn/collection/yjjj/index.shtml">业界|</a>  <a target="_blank" href="http://collection.sina.com.cn/exhibit/zlxx/2018-06-03/doc-ihcmurvf6954442.shtml">镜头下的山西唐宋古建筑</a> <a target="_blank" href="http://collection.sina.com.cn/cqyw/2018-06-03/doc-ihcmurvf7097716.shtml">宋徽宗治下的收藏之风</a></li>


<li><a target="_blank" href="http://roll.collection.sina.com.cn/collection/cpsc/index.shtml">展览| </a> <a target="_blank" href="http://collection.sina.com.cn/exhibit/zlxx/2018-06-03/doc-ihcmurvf6863198.shtml">庞贝古城出土文物开展</a> <a target="_blank" href="http://collection.sina.com.cn/exhibit/zlxx/2018-06-03/doc-ihcmurvf6835113.shtml">巨幅剪纸《端午》展出</a></li>


<li><a target="_blank" href="http://roll.collection.sina.com.cn/collection/yczs2/index.shtml">动态|</a> <a target="_blank" href="http://collection.sina.com.cn/yjjj/2018-06-03/doc-ihcmurvf6871477.shtml">北京推动中轴线文物修缮 规划建设考古遗址公园</a></li>





<li><a target="_blank" href="http://roll.collection.sina.com.cn/collection/yjjj/index.shtml">考古|</a>  <a target="_blank" href="http://collection.sina.com.cn/yjjj/2018-06-01/doc-ihcikcew1827210.shtml">秦皇岛抚宁棚改工地疑现汉代古墓 出土汉代陶器</a></li>


<li><a target="_blank" href="http://roll.collection.sina.com.cn/collection/jczs2/index.shtml">评论|</a> <a target="_blank" href="http://collection.sina.com.cn/yjjj/2018-06-03/doc-ihcmurvf6920254.shtml">丝路的前世今生</a> <a target="_blank" href="http://collection.sina.com.cn/cqyw/2018-06-03/doc-ihcmurvf7108774.shtml">地球上第一位艺术家竟不是人类</a></li>


<li><a target="_blank" href="http://roll.collection.sina.com.cn/collection/cqyw/index.shtml">非遗| </a>  <a target="_blank" href="http://collection.sina.com.cn/yjjj/2018-06-03/doc-ihcmurvf6849660.shtml">广州灰塑国家级非遗传承人 屋顶匠人风雨37载</a></li>











<li><a target="_blank" href="http://roll.collection.sina.com.cn/collection/yjjj/index.shtml">知识| </a><a target="_blank" href="http://collection.sina.com.cn/jczs/2018-06-03/doc-ihcmurvf6929010.shtml">鼻烟壶鉴定的小技巧</a> <a target="_blank" href="http://collection.sina.com.cn/jczs/2018-06-03/doc-ihcmurvf7124553.shtml">从古籍上刻工题名能知道啥</a></li>			</ul>
		</div>

		<!-- middle end -->
	</div>
	<!--XBLK_STARTX-->
	<div class="p_right">
		<!-- right begin -->

		<div class="blk_42" id="blk_spsc_03" data-sudaclick="style2_rpic">
			
<div class="ct_p_02 clearfix">
	<div class="ct_box"><a href="http://collection.sina.com.cn/auction/2018-05-31/doc-ihcffhsw0820838.shtml" target="_blank"><img width="110" height="80" src="http://n.sinaimg.cn/collect/transform/380/w220h160/20180531/9yZB-hcikcev5554051.jpg" /><span class="ct_txt">1.3亿 最贵天球瓶</span></a></div><div class="ct_box"><a href="http://collection.sina.com.cn/cpsc/2018-05-31/doc-ihcffhsv7384244.shtml" target="_blank"><img width="110" height="80" src="http://n.sinaimg.cn/collect/transform/380/w220h160/20180531/ObFb-hcikcev5615161.jpg" /><span class="ct_txt">天津市民善举捐文物</span></a></div></div>
<ul class="list_12 link_c666">
	<li><a href="http://collection.sina.com.cn/yjjj/2018-05-31/doc-ihcffhsw0972732.shtml" target="_blank">艺术品修复为何进度缓慢 因为科学家刚发现如何正确撕掉胶布</a></li><li><a href="http://collection.sina.com.cn/auction/2018-05-31/doc-ihcffhsw0854813.shtml" target="_blank">佳士得香港“乾隆三希”御窑瓷器成交逾1.6亿港币</a></li><li><a href="http://collection.sina.com.cn/yjjj/2018-05-31/doc-ihcffhsv7298270.shtml" target="_blank">泰州已出土明代服饰300余件 三品孔雀纹官服罕见</a></li></ul>
		</div>


		<!-- right end -->
	</div>
	<!--XBLK_ENDX-->
	<div class="p_bot"></div>
</div>

<!-- part_collection end -->

<div class="sp_h20"></div>

<!-- gsps房产通栏 p_id=1&t_id=912&f_id=28328 -->
<!--t id="news_web_get_gspsdata" pid="1" tid="912" did="1" fid="sp_f28328" cname="房产通栏"-->
<div class="partTit_02" id="blk_fctltop_01">
	<!-- 16:15:31 -->
<div class="pT_name"><a href="http://www.leju.com/#source=pc_sina_xwdh2&source_ext=pc_sina" target="_blank" class="titName ptn_34">房产</a></div>
  <div class="pT_more"><a href="http://search.leju.com/bj/news/" target="_blank">新闻</a> | <a href="http://news.leju.com/" target="_blank">深度</a> | <a href="http://bj.leju.com/zhuanti/" target="_blank">专题</a> | <a href="http://bj.leju.com/exhibit/" target="_blank">买房</a> | <a href="http://house.leju.com/bj/huxing/" target="_blank">户型</a> | <a href="http://bj.esf.leju.com/?bi=tg&type=sina-pc&pos=news-fcfl1" target="_blank">二手房</a> | <a href="http://bj.leju.com/bxjsq/" target="_blank">贷款计算</a> | <a href="http://map.house.leju.com/bj/" target="_blank">地图找房</a> | <a href="http://f.leju.com/channel/?city=bj" target="_blank">91乐居</a> | <a href="http://bj.leju.com/zhuanti/lejuzhongchou/" target="_blank">房产众筹</a> | <a href="http://m.leju.com/web/app/detail.html?id=3&source=xl_click" target="_blank">口袋乐居</a>  &nbsp;&nbsp&nbsp;&nbsp;<a href="http://bj.leju.com" target="_blank">更多&gt;</a></div></div>

<div class="part_03 clearfix">
	<div class="p_left" id="sina_house_link2">
		<!-- left begin -->
		<title>xinwen</title>
<div class="Tit_09" id="blk_fcup_01">
      <div class="t_name"><a href="http://house.leju.com/bj/search/" target="_blank" >新盘</a>·<a href="http://bj.leju.com/scan/dazhe/" target="_blank">打折</a>·

<a href="http://house.leju.com/bj/huxing/" target="_blank">户型</a>·<a href="http://house.leju.com/bj/yangban/" target="_blank">样板间</a>·<a href="http://esf.leju.com?bi=tg&type=sina-pc&pos=news-fcfl1" target="_blank">二手房</a></div>
      <div class="t_more"><a href="http://bj.leju.com/exhibit/" target="_blank">更多&gt;</a></div>
    </div>
<div class="blk_43" id="blk_fc_01">
  <div class="search">
        <form target="_blank" method="get" action="http://house.leju.com/bj/search/" name="sf">
        <select name="district" style="width:50px" size="1">
          <option selected="" value="">城区</option>
          
        </select>
        <select name="pricerange" style="width:100px">
          <option value="" selected="selected">价格范围</option>
          
        </select>
        <input type="text" name="keyword" class="text" value="" style="width:96px">
<input type="hidden" value="utf8" name="charset">
        <input type="submit" class="btn_01" onMouseOver="this.className='btn_01 btn_01_on'" 

onMouseOut="this.className='btn_01'" value="搜索" />
        </form>
      </div>
  <ul class="list_12 link_c666">
    <li><a href="http://bj.house.sina.com.cn/news/2018-05-23/17066404980174169092477.shtml" class="w_newsltem">石景山这条重要道路工程有望5月底完工</a></li>

<li><a target="_blank" href="http://bj.leju.com/news/2018-05-29/14176407112388050727471.shtml">快看！北京500万以内的地铁新房都在这里了！</a></li>
    <li><a href="http://bj.house.sina.com.cn/news/2018-05-23/15576404963364883443859.shtml" target="_blank">等了60年！北京地铁3号线终于要来了</a></li>
    <li><a href="http://survey.leju.com/2020.html" target="_blank">【免费报名】6月9日（六）乐居海河英才落户专线招募</a></li>
<li><a target="_blank" href="http://bj.leju.com/2018-03-14/5892968136931879910/6379620122063319545.html" >【我要买房】与买房大神一起交流 享受独家福利</a></li>   
  </ul>
</div>		<!-- left end -->
	</div>
	<div class="p_middle">
		<!-- middle begin -->
		<div class="blk_45" id="blk_fc_02">
			<ul>
				<li id="sina_house_link3"><strong>[</strong><a href="http://bj.leju.com/" target="_blank">新房</a><strong>]</strong> <a href="http://bj.leju.com/news/2018-05-28/20436406847221454909746.shtml" target="_blank" class="w_newsltem">限竞房难入市？昌平88平米mini3居洋房强势亮相</a></li>

<li id="sina_house_link4"><strong>[</strong><a href="http://bj.leju.com/" target="_blank">热点</a><strong>]</strong> <a target="_blank" href="http://bj.leju.com/news/2018-05-28/11106406703164732780686.shtml">重磅！北京限价房销售政策正式落地 基本零修改</a></li>

<li id="sina_house_link8"><strong>[</strong><a href="http://bj.leju.com/" target="_blank">关注</a><strong>]</strong> <a href="http://bj.leju.com/news/2018-05-29/16086407140368995102908.shtml" target="_blank">150㎡精工智能3居 南海子公园旁央企大盘新品入市 </a></li>				<li id="sina_house_link5"><strong>[</strong><a href="http://bj.leju.com/exhibit/" target="_blank">买房</a><strong>] </strong><a href="http://bj.house.sina.com.cn/news/2018-05-30/17526407528981926818771.shtml" target="_blank" class="w_newsltem">6月大北京预计16盘入市 限竞房迎供应高峰</a> 
</li>
<li id="sina_house_link6"><strong>[</strong><a href="http://bj.leju.com/exhibit/" target="_blank">淘房</a><strong>] </strong><a href="http://bj.leju.com/news/2018-05-29/11206407067892390867291.shtml
" target="_blank">京城那么大 乐居恒大品牌馆解密北京房企

</a></li>				<li><strong>[</strong><a href="http://jiaju.sina.com.cn/" target="_self">家居</a><strong>]</strong>
<a href="http://jiaju.sina.com.cn/news/20180604/6409227760908436316.shtml">卫浴品牌助推“厕所革命”
</a>
 <a href="http://jiaju.sina.com.cn/news/20180604/6409228913427678152.shtml">互联网家装如何进化？</a>
</li>


<li><strong>[</strong><a href="http://zx.jiaju.sina.com.cn/" target="_self">图库</a><strong>]</strong> <a href="http://zx.jiaju.sina.com.cn/anli/h1/?utm_source=snws&utm_medium=fcsection&utm_campaign=al_0063" target="_blank">豁然开朗80平</a> <a href="http://zx.jiaju.sina.com.cn/anli/s2/?utm_source=snws&utm_medium=fcsection&utm_campaign=al_0064" target="_blank">甜蜜106平怡然婚房</a> <a href="http://zx.jiaju.sina.com.cn/tupian/r7/?utm_source=snws&utm_medium=fcsection&utm_campaign=al_0065" target="_blank">简洁新颖16平</a></li>			</ul>
		</div>
		<!-- middle end -->
	</div>
	<div class="p_right">
		<!-- right begin -->
		<div class="Tit_09" id="blk_fcup_03">
      <div class="t_name"><a href="http://jiaju.sina.com.cn/" target="_blank">家居</a>·<a href="http://jiaju.sina.com.cn/decoration/" target="_blank">建材</a>·<a href="http://zx.jiaju.sina.com.cn/" target="_blank">图库</a>·<a href="http://zx.jiaju.sina.com.cn/anli/?utm_source=jjws-im" target="_blank">案例</a></div>
      <div class="t_more"><a href="http://jiaju.sina.com.cn/" target="_blank">更多&gt;</a></div>
    </div>
    <div class="blk_44" id="blk_fc_03">
      <div class="ct_pt_07 clearfix">
      <div class="ct_pic"><a href="http://jiaju.sina.com.cn/news/20180603/6408985171202474304.shtml" target="_blank">
<img src="http://src.leju.com/imp/imp/deal/14/89/2/e0351da177cc819770c6eb2c81a_p24_mk24.jpg" alt="" width="110" height="80" data-src="http://src.leju.com/imp/imp/deal/14/89/2/e0351da177cc819770c6eb2c81a_p24_mk24.jpg">
<span class="ct_tit">家居移邳州过得如何</span></a></div>
                 <div class="ct_txt">
          <ul class="list_12 link_c666">
            <li><a href="http://jiaju.sina.com.cn/news/20180531/6407769213481844979.shtml" target="_blank">毕业经济催旺二手家具销售</a></li>
            <li><a href="http://jiaju.sina.com.cn/news/20180531/6407774142455939484.shtml" target="_blank">五大顽疾困扰儿童家具消费</a></li>
            <li><a href="http://jiaju.sina.com.cn/news/20180528/6406836861293364215.shtml" target="_blank">实创事件后孙威做了啥</a></li>
            <li><a href="http://jiaju.sina.com.cn/news/20180529/6407043541746647445.shtml" target="_blank">家居进口需求旺</a></li>
          
          </ul>
        </div>
      </div>
      <ul class="list_12 link_c666">
    
<li>
<a href="http://cd.jiaju.sina.com.cn/cdjjz18.html" target="_blank"> 第18届成家具展</a>　
<a href="http://jiaju.sina.com.cn/zt/TATAsjs/" target="_blank">TATA木门世乒赛</a></li>
<li>
<a href="http://jiaju.sina.com.cn/zt/mangosay2seeking/" target="_blank">寻找心灵栖息地</a>
<a href="http://jiaju.sina.com.cn/news/j/20161124/6207394744403034497.shtml" target="_blank">感恩模式开启</a></li>
      </ul>
</div>		<!-- right end -->
	</div>
	<div class="p_bot"></div>
</div>

<script type="text/javascript" src="//bj.house.sina.com.cn/js/sina2009/location.js"></script>
<div class="sp_h20"></div>

<!-- gsps汽车通栏 p_id=1&t_id=912&f_id=28329 -->
<!--t id="news_web_get_gspsdata" pid="1" tid="912" did="1" fid="sp_f28329" cname="汽车通栏"-->
<div class="blk_09" id="blk_cjkjqcfc_01">
	<div class="partTit_02" id="blk_qctltop_01" data-sudaclick="auto2_tb">
		<div class="pT_name">
			<a href="http://auto.sina.com.cn/" target="_blank" class="titName ptn_35">汽车</a>
		</div>

		<div class="pT_more">
			<a href="http://db.auto.sina.com.cn/photo/" target="_blank">汽车图库</a> 
			| 
			<a href="http://auto.sina.com.cn/car_manual/index.d.html" target="_blank" class="linkRed">购车指南</a> 
			| 
			<a href="http://auto.sina.com.cn/guide/index.d.html" target="_blank">导购</a> 
			| 
			<a href="http://db.auto.sina.com.cn/price/" target="_blank">降价</a> 
			| 
			<a target="_blank" href="http://db.auto.sina.com.cn/">车型大全</a> 
			| <a target="_blank" href="http://db.auto.sina.com.cn/pk/car.html">车型对比</a> 
			| <a href="http://auto.sina.com.cn/wom/" target="_blank">口碑</a> 
			| <a href="http://auto.sina.com.cn/newcar/" target="_blank">新车</a> 
			| <a href="http://usedcar.auto.sina.com.cn/" target="_blank">二手车</a> 
			| <a href="http://auto.sina.com.cn/jishu/index.d.html" target="_blank">技术</a>
			| <a href="http://auto.sina.com.cn/review/" target="_blank">试车</a> 
			| <a href="http://db.auto.sina.com.cn/price/list-0-5-0-0-0-0-0-0-9-0-1.html" target="_blank">SUV</a> 
			| <a href="http://db.auto.sina.com.cn/tags/video/panggeshiche/" target="_blank">胖哥试车</a> 
			| <a href="http://auto.sina.com.cn/news/" target="_blank">新闻</a>
			| <a href="http://video.sina.com.cn/auto/" target="_blank">视频</a> 
			| <a href="http://auto.sina.com.cn/iphone/autogallery/" target="_blank" class="mobile_ico">手机/iPad客户端</a> &nbsp;&nbsp;&nbsp;&nbsp;<a href="http://auto.sina.com.cn/" target="_blank">更多&gt;  </a>    
		</div>
	</div>

	<div class="part_03 clearfix">
		<div class="p_left">
			<!-- left begin -->
			<div class="Tit_09" id="blk_qcup_01">
				<div class="t_name"><a href="http://auto.sina.com.cn/newcar/" target="_blank">新车</a>·<a href="http://photo.auto.sina.com.cn/" target="_blank">图片</a>·<a href="http://data.auto.sina.com.cn/" target="_blank">车型总汇</a></div>
				<div class="t_more"><a href="http://auto.sina.com.cn/" target="_blank">更多&gt;</a></div>
			</div>
			<div class="blk_46" id="blk_qc_01" data-sudaclick="auto2_01">
				<div class="ct_p_02 clearfix">
	<div class="ct_box">
<a href="http://db.auto.sina.com.cn/vr/986173a567a3389b/" target="_blank">
	<img width="150" height="90" src="http://n.sinaimg.cn/auto/transform/480/w300h180/20180523/2P1s-hawmauc5077293.jpg">
	<span class="ct_txt">全新逸动 品质国产车</span>
</a>
</div><div class="ct_box">
<a href="http://db.auto.sina.com.cn/vr/82c1a9e328d529a1/" target="_blank">
	<img width="150" height="90" src="http://n.sinaimg.cn/auto/transform/480/w300h180/20180523/TEhL-hawmauc5106131.jpg">
	<span class="ct_txt">颜值爆表 全新奥迪Q5L</span>
</a>
</div></div>

<div class="ct_p_02 clearfix">
	<div class="ct_box">
<a href="http://db.auto.sina.com.cn/vr/f796aba005896049/" target="_blank">
	<img width="150" height="90" src="http://n.sinaimg.cn/auto/transform/480/w300h180/20180523/d2am-fzrwiaz5789145.jpg">
	<span class="ct_txt">40万四驱车推荐:普拉多</span>
</a>
</div><div class="ct_box">
<a href="http://db.auto.sina.com.cn/vr/eaf3044dbf44cd90/" target="_blank">
	<img width="150" height="90" src="http://n.sinaimg.cn/auto/transform/480/w300h180/20180523/1ryv-hawmauc5127259.jpg">
	<span class="ct_txt">最接地气国车 红旗H5</span>
</a>
</div></div>
			</div>

			<!-- left end -->
		</div>
		
		<div class="p_middle" data-sudaclick="auto2_list">
			<!-- middle begin -->
			<div class="blk_36" id="blk_qc_02"><ul class="list_14">

<li><a href="http://k.sina.com.cn/article_6411485938_v17e2782f2001008rw1.html?from=auto" target="_blank">张扬外表沉稳初心-全新凯美瑞</a> 
<a href="http://k.sina.com.cn/article_5310047613_v13c80e57d001009qjb.html?from=auto&subch=bauto" target="_blank">家长注意别让娃这样做</a>
</li>

<li>
<a href="http://k.sina.com.cn/article_2008986745_v77beb47900100b8vj.html?from=auto&subch=iauto" target="_blank">进口车税下调离豪车又近一步</a> <a target="_blank" href="http://k.sina.com.cn/article_2511647472_v95b4b2f0001007231.html?from=auto&subch=nauto">2018马自达3:安全升级</a></li>

<li>
<a href="http://k.sina.com.cn/article_6100982176_v16ba599a000100f151.html?from=auto&subch=nauto" target="_blank">全新朗逸没你想的那么简单</a> <a target="_blank" href="http://k.sina.com.cn/article_2504345074_v954545f2001007o2t.html?from=auto&subch=uauto">8代凯美瑞安全媲美奔驰?</a></li>


<li>
<a href="http://k.sina.com.cn/article_5685395646_v152e040be0010070cx.html?from=auto" target="_blank">男人的烦恼:没地位因买错车?</a> <a target="_blank" href="http://k.sina.com.cn/article_1862727307_v6f06f68b001009f0j.html?from=auto">&quot;不务正业&quot;的轮胎企业</a>

</li>


<li><a href="http://k.sina.com.cn/article_6411485938_v17e2782f2001008il7.html?from=auto" target="_blank">女性角度看别克GL8 Avenir</a> <a target="_blank" href="http://k.sina.com.cn/article_5310047613_v13c80e57d001009ic5.html?from=auto">除凯越朗逸也要关注它们</a></li>

<li><a href="http://auto.sina.com.cn/newcar/j/2018-05-24/detail-ihaysviy2642807.shtml" target="_blank">最高降16.5万 奥迪全系进口车调价</a> <a target="_blank" href="http://auto.sina.com.cn/newcar/h/2018-05-24/detail-ihaysvix8872209.shtml">奔驰GLS最新谍照</a></li>

<li><a href="http://k.sina.com.cn/article_5189211414_v1354d1516001008gz5.html?from=auto&subch=uauto" target="_blank">为啥他的油耗比我低？</a> <a target="_blank" href="http://k.sina.com.cn/article_1463946293_v57420c350010064u1.html?from=auto">雅阁和凯美瑞最大的区别</a></li>



<li>
<a href="http://auto.sina.com.cn/guide/chexing/2018-05-22/detail-ihawmaua1445952.shtml" target="_blank">三国杀|高规格自主品牌SUV对比</a>  
<a href="http://auto.sina.com.cn/guide/chexing/2018-05-21/detail-iharvfht7748318.shtml" target="_blank">10万买哪款SUV？</a>
</li>

<li>
<a href="http://auto.sina.com.cn/newcar/2018-05-23/detail-ihawmauc1462146.shtml" target="_blank">含义很深 大众朗逸PLUS有何不同</a> 
<a href="http://auto.sina.com.cn/newcar/x/2018-05-20/detail-ihaturft3208490.shtml" target="_blank">瑞风S7售10.98万起</a>
</li></ul></div>
			<!-- middle end -->
		</div>
		<!--XBLK_STARTX-->
		<div class="p_right">
			<!-- right begin -->
			<div class="Tit_09" id="blk_qcup_03">
				<div class="t_name"><a href="http://t.auto.sina.com.cn/" target="_blank">微博</a>·<a href="http://auto.sina.com.cn/user/" target="_blank">社区</a>·<a href="http://auto.sina.com.cn/beauty/" target="_blank">车模</a></div>
				<div class="t_more"><a href="http://auto.sina.com.cn/user/" target="_blank">更多&gt;</a></div>
			</div>

			<div class="blk_44" id="blk_qc_03" style="padding-bottom:2px;" data-sudaclick="auto2_02">
				<!-- right begin -->
				
<div class="ct_pt_07 clearfix">
	<div class="ct_pic">
		<a href="http://db.auto.sina.com.cn/2326/" target="_blank"><img src="http://n.sinaimg.cn/auto/transform/20170217/-WPp-fyarrcc7608009.jpg" width="110" height="80"><span class="ct_tit">奔驰GLC</span></a>	</div>
	<div class="ct_txt">

		<ul class="list_12 link_c666">
			<li><a target="_blank" href="http://db.auto.sina.com.cn/9/">奥迪全新A4L称霸同级</a></li><li><a target="_blank" href="http://db.auto.sina.com.cn/626/">丰田紧凑SUV外观犀利</a></li><li><a target="_blank" href="http://db.auto.sina.com.cn/459/">大众神车出到第八代</a></li><li><a target="_blank" href="http://db.auto.sina.com.cn/357/">奔驰全新E级堪称小S</a></li>		</ul>
	</div>
</div>

<div class="ct_pt_07 clearfix" style="padding-top:0px;">
	<div class="ct_pic">
		<a href="http://db.auto.sina.com.cn/2325/" target="_blank"><img src="http://n.sinaimg.cn/auto/transform/20170217/F24d-fyarrcc7607285.jpg" width="110" height="80"><span class="ct_tit">吉利博越</span></a>	</div>
	<div class="ct_txt">
		<ul class="list_12 link_c666">	
			<li><a target="_blank" href="http://db.auto.sina.com.cn/680/">大众新SUV神车途观L</a></li><li><a target="_blank" href="http://db.auto.sina.com.cn/2166/">凯迪拉克CT6竞争BBA</a></li><li><a target="_blank" href="http://db.auto.sina.com.cn/406/">丰田最火B级车凯美瑞</a></li><li><a target="_blank" href="http://db.auto.sina.com.cn/2136/">传祺GS4要把H6拉下马</a></li>		</ul>
	</div>
</div>
<ul class="list_12 link_c666" style="padding-top:0px;padding-bottom:0px;">
	<li><a target="_blank"  class="linkRed" href="http://db.auto.sina.com.cn/">选车购车</a> 
		<a target="_blank" href="http://db.auto.sina.com.cn/list-0-5-0-0-0-0-0-0-9-0-1.html">SUV</a>
		<a target="_blank" href="http://db.auto.sina.com.cn/list-0-1-0-0-0-0-0-0-9-0-1.html">两厢</a>
		<a target="_blank" href="http://db.auto.sina.com.cn/list-0-2-0-0-0-0-0-0-9-0-1.html">三厢</a>
		<a target="_blank" href="http://db.auto.sina.com.cn/list-0-11-0-0-0-0-0-0-9-0-1.html">跑车</a> 
		<a target="_blank" href="http://db.auto.sina.com.cn/list-0-15-0-0-0-0-0-0-9-0-1.html">新能源</a> 
		<a target="_blank" href="http://db.auto.sina.com.cn/list-0-7-0-0-0-0-0-0-9-0-1.html">MPV</a></li>
</ul>

				<!-- right begin -->
			</div>

			<!-- right end -->
		</div>
		<!--XBLK_ENDX-->
		<div class="p_bot"></div>
	</div>
</div>



<!-- part_tech begin -->
<div class="partTit_01" id="blk_kjtltop_01" data-sudaclick="tech2_tb">
  <div class="pT_name"><a href="http://tech.sina.com.cn/" target="_blank" class="titName ptn_36">科技新闻</a></div>
  <div class="pT_more">
  <a href="http://zhongce.sina.com.cn/" target="_blank">众测</a> | <a href="http://shiqu.sina.com.cn/" target="_blank">识趣</a> | <a href="http://tech.sina.com.cn/t/4g/" target="_blank">4G</a> | <a href="http://mobile.sina.com.cn/" target="_blank">手机</a> | <a href="http://tech.sina.com.cn/apple/" target="_blank">苹果汇</a> | <a href="http://tech.sina.com.cn/digital/" target="_blank">数码</a> | <a href="http://tech.sina.com.cn/down/" target="_blank">下载</a> |  <a href="http://tech.sina.com.cn/notebook" target="_blank">笔记本</a> | <a href="http://tech.sina.com.cn/price/" target="_blank">产品报价</a> | <a href="http://tech.sina.com.cn/discovery" target="_blank">探索</a> | <a href="http://tech.sina.com.cn/d/photo/" target="_blank">趣图</a> &nbsp;&nbsp&nbsp;&nbsp;<a href="http://tech.sina.com.cn/" target="_blank">更多&gt;</a></div></div>

<div class="part_02 clearfix">
  <div class="p_left">
  <!-- left begin -->
  <div class="blk_new_10">
          <div class="blk_tit  mb_1">
                <ol>
                    <li class="techtab selected" id="techpic_lab01"><a href="http://tech.sina.com.cn/d/photo/" target="_blank">科技趣图</a></li>
                    <li class="techtab"  id="techpic_lab02"><a href="http://tech.sina.com.cn/discovery/" target="_blank">科学探索</a></li>
                    <li class="techtab"  id="techpic_lab03"><a href="http://tech.sina.com.cn/digi/photo/" target="_blank">数码摄影</a></li>
                    <li class="techtab"  id="techpic_lab04"><a href="http://mobile.sina.com.cn/" target="_blank">新款手机</a></li>
                </ol>
            </div>
            
            <div class="blk_main">
            <!-- 1 -->
            <div  id="techpic_cont01" class="blk_main_01">
            <div class="b_cont">
              <div class="ct_p_05 clearfix" id="scrPic_kjqt_01"  data-sudaclick="tech2_01">
<div class="ct_pic"><a href="http://slide.tech.sina.com.cn/d/slide_5_453_117029.html" target="_blank">
<img src="http://n.sinaimg.cn/tech/transform/490/w340h150/20180604/P4B8-hcmurvh3129693.jpg" width="340" height="150" alt="" /><span class="ct_txt">珍珠鲻鱼洄游产卵 遇仇敌海鸥插翅难逃</span></a></div>
<div class="ct_pic"><a href="http://slide.tech.sina.com.cn/d/slide_5_453_116932.html" target="_blank">
<img src="http://n.sinaimg.cn/tech/transform/490/w340h150/20180601/sd-R-hcikcev8960597.jpg" width="340" height="150" alt="" /><span class="ct_txt">用生命在拍照！摄影师“放血”拍蚊子特写</span></a></div>
<div class="ct_pic"><a href="http://slide.tech.sina.com.cn/d/slide_5_453_116887.html" target="_blank">
<img src="http://n.sinaimg.cn/tech/transform/490/w340h150/20180531/LG9c-hcikcev3105418.jpg" width="340" height="150" alt="" /><span class="ct_txt">各地震撼闪电奇观 自然之怒如末日来临</span></a></div>
<div class="ct_pic"><a href="http://slide.tech.sina.com.cn/d/slide_5_453_116830.html" target="_blank">
<img src="http://n.sinaimg.cn/tech/transform/490/w340h150/20180530/iLcI-hcffhsv4745298.jpg" width="340" height="150" alt="" /><span class="ct_txt">鳄鱼捕食剧毒蝰蛇 猛烈撕咬显凶残本性</span></a></div>
              </div>
              <a href="javascript:void(0)" class="scrArrAbsLeft" id="scrArrLeft_kjqt_01"></a>
              <a href="javascript:void(0)" class="scrArrAbsRight" id="scrArrRight_kjqt_01"></a>
            </div>
            
            <div class="b_cons">
              <span class="scrDotList" id="scrDotList_kjqt_01">
                <span></span>
              </span>
            </div>
        <script type="text/javascript">
           jsLoader(ARTICLE_JSS.common,function(){
              var focusScroll = new ScrollPic();
              focusScroll.scrollContId  = "scrPic_kjqt_01"; //内容容器ID
        
              focusScroll.dotListId   = "scrDotList_kjqt_01";//点列表ID
              focusScroll.dotClassName  = "";//点className
              focusScroll.dotOnClassName = "on";//当前点className
              focusScroll.listType  = "";//列表类型(number:数字，其它为空)
              focusScroll.listEvent = "onmouseover"; //切换事件
        
              focusScroll.frameWidth  = 340;//显示框宽度
              focusScroll.pageWidth = 340; //翻页宽度
              focusScroll.upright = false; //垂直滚动
              focusScroll.speed   = 10; //移动速度(单位毫秒，越小越快)
              focusScroll.space   = 40; //每次移动像素(单位px，越大越快)
              focusScroll.autoPlay  = false; //自动播放
              focusScroll.autoPlayTime = 5; //自动播放间隔时间(秒)
              focusScroll.circularly = true;
              focusScroll.initialize(); //初始化
              document.getElementById('scrArrLeft_kjqt_01').onmousedown = function(){
                focusScroll.pre();
                return false;
              }
              document.getElementById('scrArrRight_kjqt_01').onmousedown = function(){
                focusScroll.next();
                return false;
              }
          });
        </script>
            </div>
            <!-- 2 -->
            <div  id="techpic_cont02" class="blk_main_02">
        <div class="b_cont">
        
          <div class="ct_p_05 clearfix" id="scrPic_kjqt_02"   data-sudaclick="tech2_02">
<div class="ct_pic"><a href="http://slide.tech.sina.com.cn/d/slide_5_453_117030.html" target="_blank">
<img src="http://n.sinaimg.cn/tech/transform/490/w340h150/20180604/Mzwe-hcmurvh3134947.jpg" width="340" height="150" alt="" /><span class="ct_txt">动物百变发型 可以说是相当时尚</span></a></div>
<div class="ct_pic"><a href="http://slide.tech.sina.com.cn/d/slide_5_453_116929.html" target="_blank">
<img src="http://n.sinaimg.cn/tech/transform/490/w340h150/20180601/pVIM-hcikcev8964487.jpg" width="340" height="150" alt="" /><span class="ct_txt">被大白鲨吃掉是啥感觉？</span></a></div>
<div class="ct_pic"><a href="http://slide.tech.sina.com.cn/d/slide_5_453_116888.html" target="_blank">
<img src="http://n.sinaimg.cn/tech/transform/490/w340h150/20180531/nemR-hcikcev3110976.jpg" width="340" height="150" alt="" /><span class="ct_txt">小狮子通过打斗游戏练习捕猎技巧</span></a></div>
<div class="ct_pic"><a href="http://slide.tech.sina.com.cn/d/slide_5_453_116829.html" target="_blank">
<img src="http://n.sinaimg.cn/tech/transform/490/w340h150/20180530/SnKr-hcffhsv4749859.jpg" width="340" height="150" alt="" /><span class="ct_txt">老虎蓄势待发伏击鹿群结果扑空</span></a></div>
          </div>
            <a href="javascript:void(0)" class="scrArrAbsLeft" id="scrArrLeft_kjqt_02"></a>
            <a href="javascript:void(0)" class="scrArrAbsRight" id="scrArrRight_kjqt_02"></a>
        </div>
        
        <div class="b_cons">
          <span class="scrDotList" id="scrDotList_kjqt_02">
            <span></span>
          </span>
        </div>

        
        <script type="text/javascript">
          jsLoader(ARTICLE_JSS.common,function(){
              var focusScroll = new ScrollPic();
              focusScroll.scrollContId  = "scrPic_kjqt_02"; //内容容器ID
        
              focusScroll.dotListId   = "scrDotList_kjqt_02";//点列表ID
              focusScroll.dotClassName  = "";//点className
              focusScroll.dotOnClassName = "on";//当前点className
              focusScroll.listType  = "";//列表类型(number:数字，其它为空)
              focusScroll.listEvent = "onmouseover"; //切换事件
        
              focusScroll.frameWidth  = 340;//显示框宽度
              focusScroll.pageWidth = 340; //翻页宽度
              focusScroll.upright = false; //垂直滚动
              focusScroll.speed   = 10; //移动速度(单位毫秒，越小越快)
              focusScroll.space   = 40; //每次移动像素(单位px，越大越快)
              focusScroll.autoPlay  = false; //自动播放
              focusScroll.autoPlayTime = 5; //自动播放间隔时间(秒)
              focusScroll.circularly = true;
              focusScroll.initialize(); //初始化
              document.getElementById('scrArrLeft_kjqt_02').onmousedown = function(){
                focusScroll.pre();
                return false;
              }
              document.getElementById('scrArrRight_kjqt_02').onmousedown = function(){
                focusScroll.next();
                return false;
              }
          });
        </script>
            </div>
            <!-- 3 -->
            <div  id="techpic_cont03" class="blk_main_03">
        <div class="b_cont">
          <div class="ct_p_05 clearfix" id="scrPic_kjqt_03"   data-sudaclick="tech2_03">
<div class="ct_pic"><a href="http://tech.sina.com.cn/digi/photo/" target="_blank">
<img src="http://n.sinaimg.cn/tech/transform/490/w340h150/20180507/EXZI-hacuuvu2697328.jpg" width="340" height="150" alt="" /><span class="ct_txt">手机全景模式下的自然风光</span></a></div>
<div class="ct_pic"><a href="http://slide.tech.sina.com.cn/digi/slide_5_30939_115226.html" target="_blank">
<img src="http://n.sinaimg.cn/tech/transform/490/w340h150/20180507/d9zE-hacuuvu2702224.jpg" width="340" height="150" alt="" /><span class="ct_txt">风格浓郁的肖像 光影间诠释性感身姿</span></a></div>
          </div>
          <a href="javascript:void(0)" class="scrArrAbsLeft" id="scrArrLeft_kjqt_03"></a>
          <a href="javascript:void(0)" class="scrArrAbsRight" id="scrArrRight_kjqt_03"></a>
        </div>
        
        <div class="b_cons">
          <span class="scrDotList" id="scrDotList_kjqt_03">
            <span></span>
          </span>
        </div>
        
        <script type="text/javascript">
          jsLoader(ARTICLE_JSS.common,function(){
              var focusScroll = new ScrollPic();
              focusScroll.scrollContId  = "scrPic_kjqt_03"; //内容容器ID
        
              focusScroll.dotListId   = "scrDotList_kjqt_03";//点列表ID
              focusScroll.dotClassName  = "";//点className
              focusScroll.dotOnClassName = "on";//当前点className
              focusScroll.listType  = "";//列表类型(number:数字，其它为空)
              focusScroll.listEvent = "onmouseover"; //切换事件
        
              focusScroll.frameWidth  = 340;//显示框宽度
              focusScroll.pageWidth = 340; //翻页宽度
              focusScroll.upright = false; //垂直滚动
              focusScroll.speed   = 10; //移动速度(单位毫秒，越小越快)
              focusScroll.space   = 40; //每次移动像素(单位px，越大越快)
              focusScroll.autoPlay  = false; //自动播放
              focusScroll.autoPlayTime = 5; //自动播放间隔时间(秒)
              focusScroll.circularly = true;
              focusScroll.initialize(); //初始化
              document.getElementById('scrArrLeft_kjqt_03').onmousedown = function(){
                focusScroll.pre();
                return false;
              }
              document.getElementById('scrArrRight_kjqt_03').onmousedown = function(){
                focusScroll.next();
                return false;
              }
         
          });
        </script>
            </div>
            <!-- 4 -->
            <div  id="techpic_cont04" class="blk_main_04">
        <div class="b_cont">
          <div class="ct_p_05 clearfix" id="scrPic_kjqt_04"  data-sudaclick="tech2_04">
<div class="ct_pic"><a href="http://tech.sina.com.cn/mobile/n/c/2018-05-31/doc-ihcikcev5222436.shtml" target="_blank">
<img src="http://n.sinaimg.cn/tech/transform/160/w660h300/20180601/rb5e-hcikcew2132775.jpg" width="340" height="150" alt="" /><span class="ct_txt">小米8评测:与苹果的同和不同</span></a></div>
<div class="ct_pic"><a href="http://tech.sina.com.cn/mobile/n/n/2018-06-01/doc-ihcikcev9040491.shtml" target="_blank">
<img src="http://n.sinaimg.cn/tech/transform/160/w660h300/20180601/Hy58-hcikcew2139534.png" width="340" height="150" alt="" /><span class="ct_txt">外媒：小米8在设计上模仿了iPhone X</span></a></div>
<div class="ct_pic"><a href="http://tech.sina.com.cn/mobile/n/n/2018-06-01/doc-ihcikcev8791727.shtml" target="_blank">
<img src="http://n.sinaimg.cn/tech/transform/160/w660h300/20180601/hYkl-hcikcew2143076.jpg" width="340" height="150" alt="" /><span class="ct_txt">华硕计划推出ROG游戏手机 预计本月发</span></a></div>
<div class="ct_pic"><a href="http://tousu.sina.com.cn/complaint/view/17347221500/" target="_blank">
<img src="http://n.sinaimg.cn/tech/transform/160/w660h300/20180411/BnQj-fytnfyp2391500.jpg" width="340" height="150" alt="" /><span class="ct_txt">黑猫投诉:京东二次销售退换主板</span></a></div>
          </div>
          <a href="javascript:void(0)" class="scrArrAbsLeft" id="scrArrLeft_kjqt_04"></a>
          <a href="javascript:void(0)" class="scrArrAbsRight" id="scrArrRight_kjqt_04"></a>
        </div>
        
        <div class="b_cons">
          <span class="scrDotList" id="scrDotList_kjqt_04">
            <span></span>
          </span>
        </div>
        
        <script type="text/javascript">
          jsLoader(ARTICLE_JSS.common,function(){
              var focusScroll = new ScrollPic();
              focusScroll.scrollContId  = "scrPic_kjqt_04"; //内容容器ID
        
              focusScroll.dotListId   = "scrDotList_kjqt_04";//点列表ID
              focusScroll.dotClassName  = "";//点className
              focusScroll.dotOnClassName = "on";//当前点className
              focusScroll.listType  = "";//列表类型(number:数字，其它为空)
              focusScroll.listEvent = "onmouseover"; //切换事件
        
              focusScroll.frameWidth  = 340;//显示框宽度
              focusScroll.pageWidth = 340; //翻页宽度
              focusScroll.upright = false; //垂直滚动
              focusScroll.speed   = 10; //移动速度(单位毫秒，越小越快)
              focusScroll.space   = 40; //每次移动像素(单位px，越大越快)
              focusScroll.autoPlay  = false; //自动播放
              focusScroll.autoPlayTime = 5; //自动播放间隔时间(秒)
              focusScroll.circularly = true;
              focusScroll.initialize(); //初始化
              document.getElementById('scrArrLeft_kjqt_04').onmousedown = function(){
                focusScroll.pre();
                return false;
              }
              document.getElementById('scrArrRight_kjqt_04').onmousedown = function(){
                focusScroll.next();
                return false;
              }
         
          });
        </script>
            </div>
        
            </div>

            <script type="text/javascript" id="js_tab_7">
            jsLoader(ARTICLE_JSS.common,function(){
                var subshow = new SubShowClass('none','onmouseover');
                subshow.addLabel('techpic_lab01','techpic_cont01');
                subshow.addLabel('techpic_lab02','techpic_cont02');
                subshow.addLabel('techpic_lab03','techpic_cont03');
                subshow.addLabel('techpic_lab04','techpic_cont04');
            });
            </script>


        </div>
  <div class="blk_new_11">
      <div class="blk_tit">
            <ol>
                <li class="selected "><a href="http://tech.sina.com.cn/digital/" target="_blank">数码精选</a></li>
            </ol>
            <div class="tit_more"><a href="http://tech.sina.com.cn/digital/" target="_blank">更多</a></div>
        </div>
        <div class="blk_main clearfix">
                  <ul  data-sudaclick="tech2_05">
<li><a class="zt_pic_w" href="http://shiqu.sina.com.cn/" target="_blank"><img data-src="http://n.sinaimg.cn/tech/transform/500/w320h180/20180601/SDJg-hcikcew2089982.jpg" border="0"><span class="zt_txt">100%可回收帐篷</span></a></li>
<li><a class="zt_pic_w" href="http://tech.sina.com.cn/q/toy/2018-06-01/doc-ihcikcev5834805.shtml" target="_blank"><img data-src="http://n.sinaimg.cn/tech/transform/500/w320h180/20180601/1EIT-hcikcew2094619.jpg" border="0"><span class="zt_txt">“美味”的乐高玩具</span></a></li>
<li><a class="zt_pic_w" href="http://tech.sina.com.cn/q/auto/2018-06-01/doc-ihcikcev4150007.shtml" target="_blank"><img data-src="http://n.sinaimg.cn/tech/transform/500/w320h180/20180601/fnDU-hcikcew2111348.jpg" border="0"><span class="zt_txt">车牌升级到了墨水屏</span></a></li>
<li><a class="zt_pic_w" href="http://slide.tech.sina.com.cn/mobile/slide_5_22298_116910.html/d/1#p=1" target="_blank"><img data-src="http://n.sinaimg.cn/tech/transform/500/w320h180/20180523/ZoY1-hawmauc3163299.jpg" border="0"><span class="zt_txt">小米8开箱图赏</span></a></li>
<li><a class="zt_pic_w" href="http://slide.tech.sina.com.cn/mobile/slide_5_22298_116488.html/d/1#p=1" target="_blank"><img data-src="http://n.sinaimg.cn/tech/transform/500/w320h180/20180523/Me9v-hawmauc3146138.jpg" border="0"><span class="zt_txt">vivo X21世界杯非凡版图赏</span></a></li>
<li><a class="zt_pic_w" href="http://slide.tech.sina.com.cn/mobile/slide_5_22298_116439.html/d/1#p=1" target="_blank"><img data-src="http://n.sinaimg.cn/tech/transform/500/w320h180/20180523/tqoY-hawmauc3156810.jpg" border="0"><span class="zt_txt">Elite Active 65t耳机体验</span></a></li>
                  </ul>
                </div>
    </div>

  <!-- left end -->
  </div>
  <div class="p_middle"  data-sudaclick="tech2_list">
  <div style="height:7px; overflow:hidden;font-size:0;line-height:0;"></div>
  <!-- middle begin -->
<!-- 互联网 IT业界 电信 -->
<div class="Tit_06" id="blk_kjxwhlwup_01">
  <div class="t_name"><a href="http://tech.sina.com.cn/internet/" target="_blank">互联网</a><span class="dot">·</span><a href="http://tech.sina.com.cn/it/" target="_blank">IT业界</a><span class="dot">·</span><a href="http://tech.sina.com.cn/tele/" target="_blank">电信</a><span class="dot">·</span><a href="http://tech.sina.com.cn/t/4g/" target="_blank">4G</a></div>
  <div class="t_more"><a href="http://tech.sina.com.cn/" target="_blank">更多</a></div>
</div>
<div class="blk_33" id="blk_kjxwhlw_01">
  <ul class="list_14">
<!--t id="news_web_get_gspsdata" pid="1" tid="922" did="9" fid="sp_f23876" cname="二类互联网"-->
	  			<li><a href="http://tech.sina.com.cn/i/2018-06-04/doc-ihcmurvh4140056.shtml" target="_blank" >直击|今日头条：腾讯封禁头条系产品 还进行污名化</a><span class="time"> 12:25</span></li>			<li><a href="http://tech.sina.com.cn/i/2018-06-03/doc-ihcmurvf7409710.shtml" target="_blank" >多方申领“空姐遇害案”滴滴赏金 悬赏被指缺乏诚意</a><span class="time"> 10:36</span></li>			<li><a href="http://tech.sina.com.cn/i/2018-06-03/doc-ihcmurvf6953589.shtml" target="_blank" >生活靠一单单跑出来 7000万“网约工”缺保障机制</a><span class="time"> 07:56</span></li>			<li><a href="http://tech.sina.com.cn/i/2018-06-01/doc-ihcikcew4031912.shtml" target="_blank" >今日头条：已对腾讯的不正当竞争行为提出诉讼</a><span class="time"> 23:06</span></li>			<li><a href="http://tech.sina.com.cn/i/2018-06-01/doc-ihcikcew4001065.shtml" target="_blank" >“腾头之诉”仅1元  荣誉战还是入口之争？</a><span class="time"> 22:55</span></li>			<li><a href="http://tech.sina.com.cn/i/2018-06-01/doc-ihcikcew3820748.shtml" target="_blank" >上海共享单车管理办法征求意见：禁止车辆设商业广告</a><span class="time"> 20:26</span></li>			<li><a href="http://tech.sina.com.cn/i/2018-06-01/doc-ihcikcew3034344.shtml" target="_blank" >阿里王帅：腾讯起诉是要让人闭嘴 我挺今日头条</a><span class="time"> 19:26</span></li>
  </ul>
</div>
<!-- 科技探索 -->
<div class="Tit_06" id="blk_kjxwkjtsup_01">
  <div class="t_name"><a href="http://tech.sina.com.cn/discovery" target="_blank">科学探索</a><span class="dot">·</span><a href="http://tech.sina.com.cn/d/photo/" target="_blank">趣图</a></div>
  <div class="t_more"><a href="http://tech.sina.com.cn/discovery" target="_blank">更多</a></div>
</div>
<div class="blk_33" id="blk_kjxwkjts_01">
  <ul class="list_14">
<!--t id="news_web_get_gspsdata" pid="1" tid="922" did="9" fid="sp_f23877" cname="二类科学探索"-->
	  			<li><a href="http://tech.sina.com.cn/d/a/2018-06-04/doc-ihcmurvh2623639.shtml" target="_blank" >宠物眼里的世界是什么样？不同物种间视力差别巨大</a><span class="time"> 09:05</span></li>			<li><a href="http://tech.sina.com.cn/d/s/2018-06-04/doc-ihcmurvh2592927.shtml" target="_blank" >活跃的冥王星：星球表面发现固态甲烷形成的沙丘</a><span class="time"> 09:00</span></li>			<li><a href="http://tech.sina.com.cn/d/s/2018-06-04/doc-ihcmurvh2507253.shtml" target="_blank" >暗物质有可能消失吗？可能由多种粒子构成的新理论</a><span class="time"> 08:44</span></li>			<li><a href="http://tech.sina.com.cn/d/f/2018-05-31/doc-ihcffhsv9576158.shtml" target="_blank" >华大基因汪建再成媒体焦点：基因狂人还是营销大师？</a><span class="time"> 01:17</span></li>			<li><a href="http://tech.sina.com.cn/it/2018-05-28/doc-ihcffhsu5579053.shtml" target="_blank" >最新！建设世界科技强国，习近平提出这样干</a><span class="time"> 22:10</span></li>
  </ul>
</div>
<!-- 手机 -->
<div class="Tit_06" id="blk_kjxwsjxjbjbup_01">
  <div class="t_name"><a href="http://mobile.sina.com.cn/" target="_blank">手机</a><span class="dot">·</span><a href="http://tech.sina.com.cn/digital/" target="_blank">相机</a><span class="dot">·</span><a href="http://tech.sina.com.cn/notebook/" target="_blank">笔记本</a></div>
  <div class="t_more"><a href="http://digi.sina.com.cn/" target="_blank">更多</a></div>
</div>
<div class="blk_33" id="blk_kjxwsjxjbjb_01">
  <ul class="list_14" id="blk_kjxwsjxjbjb_011">
<li><a href="http://tousu.sina.com.cn/" target="_blank">[黑猫投诉]</a>     <a target="_blank" href="http://tousu.sina.com.cn/complaint/view/17347222315/">在转转平台购买手机 到货后不是买的那款</a></li>


<li><a href="http://mobile.sina.com.cn" target="_blank">[苹果汇]</a> <a target="_blank" href="http://tech.sina.com.cn/zt_d/wwdc18/">WWDC2018开发者大会专题</a> <a target="_blank" href="http://video.sina.com.cn/p/others/o/doc/2018-06-04/081468741123.html">探营视频</a> <a target="_blank" href="http://slide.tech.sina.com.cn/mobile/slide_5_22298_117026.html/d/1#p=1">图集</a></li><li>[<a href="http://zhongce.sina.com.cn/" target="_blank">众测</a>]
<a target="_blank" href="http://zhongce.sina.com.cn/article/view/9438/">选购蓝牙音箱看什么？</a> 
<a target="_blank" href="http://zhongce.sina.com.cn/article/view/9414/">如何选适合自己相机？</a>

</li>



<li>[<a href="http://zhongce.sina.com.cn/task" target="_blank">热聊</a>]

<a target="_blank" href="http://zhongce.sina.com.cn/task">过六一晒出你的童年照</a>
<a target="_blank" href="http://zhongce.sina.com.cn/task/activity/view/142/">你身边人都用什么手机</a></li><li>
<a href="http://tech.sina.com.cn/notebook/" target="_blank">[电脑]</a>
<a target="_blank" href="http://tech.sina.com.cn/n/k/2018-06-04/doc-ihcmurvh2425303.shtml">骁龙1000笔记本处理器曝光 </a> <a target="_blank" href="http://tech.sina.com.cn/i/2018-06-04/doc-ihcmurvh1288302.shtml">英特尔AMD爱恨情仇</a></li>  </ul>
</div>


  <!-- middle end -->
  </div>

<!--XBLK_STARTX-->

<!-- 新浪众测 -->
<style type="text/css">
  .blk_new_12 .zc_block{
    position: relative;
    padding: 0 10px;
    margin:0;
    width: 240px;
  }
  .zc_block{color:#666}
  .zc_block a:link{color:#666}
  .zc_block a:visited{color:#666}
  .zc_block a:hover{color:#8d0000}
  .zc_block h3{
    font-size: 16px;
    line-height: 38px;
  }
  .zc_block .pic{
    height: 90px;
  }
  .zc_block .pic img{
    display: block;
    float: left;
    width: 120px;
    height: 80px;
  }
  .zc_block .pic .txt{
    width: 110px;
    float: left;
    margin-left: 10px;
    padding-top:5px;
  }
  .zc_block .pic p{
    line-height: 20px;
    height: 20px;
    overflow: hidden;
  }
  .zc_block .pic span{
    color: #d00;
  }
  .zc_block .pic .btn{
    margin-top: 5px;
    height: 24px;
    overflow: hidden;
  }
  .zc_block .btn a{
    display: block;
    width: 70px;
    height: 24px;
    line-height: 24px;
    text-align: center;
    text-decoration: none;
    color: #fff;
    background: #1f3b7b;
    overflow: hidden;
  }
  .zc_block .btn a:visited,.zc_block .btn a:hover{color: #fff;}
  .zc_block .list{
    border-top:1px solid #c5cad9;
  }
  .zc_block .list p{
    position: relative;
    float: left;
    width: 120px;
    height: 26px;
    line-height: 26px;
    text-align: center;
    overflow: hidden;
  }
</style>


  <div class="p_right bgc_f6f6f6">
    <div class="blk_new_12">
      <div class="Tit_12" style="border-top:none;" id="blk_cswbup_01">
          <div class="t_cont" style="border-top-color:#e7e8eb;">
            <div class="t_name"><a href="http://zhongce.sina.com.cn/" target="_blank">新浪众测</a></div>
            <div class="t_more"><a href="http://zhongce.sina.com.cn/" target="_blank">更多</a></div>
          </div>
        </div>
        <div class="zc_block blk_main clearfix">

            <h3><a href="http://zhongce.sina.com.cn/" target="_blank">免费送:Bobot无线电动拖地机</a></h3>
            <div class="pic clearfix">
              <a href="http://zhongce.sina.com.cn/" target="_blank"><img src="http://n.sinaimg.cn/tech/transform/200/w120h80/20180531/WGPs-hcikcev2693149.png"></a>
              <div class="txt">
                <p>价格：<span>¥1499</span></p>
                <p>数量：<span>20台</span></p>
                <p class="btn"><a href="http://zhongce.sina.com.cn/activity/view/276/" target="_blank">免费申请</a></p>
              </div>
            </div>
            <div class="list clearfix">
              <p><a href="http://zhongce.sina.com.cn/activity/view/275/" target="_blank">国文阅读器</a></p>
              <p><a href="http://zhongce.sina.com.cn/activity/view/274/" target="_blank">极米无屏电视H2</a></p>
            </div>
        </div>
        
    </div>
    <div class="sp_h10"></div>
    <div class="blk_new_12">
      <div class="Tit_12" style="border-top:none;" id="blk_cswbup_01">
          <div class="t_cont" style="border-top-color:#e7e8eb;">
            <div class="t_name"><a href="http://tech.sina.com.cn/zl/" target="_blank">创事记</a></div>
            <div class="t_more"><a href="http://tech.sina.com.cn/zl/" target="_blank">更多</a></div>
          </div>
        </div>
        <div class="blk_main"  data-sudaclick="tech2_07">
          <ul class="clearfix">
<li><a class="zt_pic_w" href="http://tech.sina.com.cn/csj/2018-06-04/doc-ihcmurvh2609791.shtml" target="_blank"><img class="zt_img" alt="" data-src="http://n.sinaimg.cn/tech/transform/420/w240h180/20180604/vEZp-hcmurvh3420606.jpg"><span class="zt_txt">头条没那么重要了</span></a></li> 
<li><a class="zt_pic_w" href="http://tech.sina.com.cn/csj/2018-06-04/doc-ihcmurvh2847341.shtml" target="_blank"><img class="zt_img" alt="" data-src="http://n.sinaimg.cn/tech/transform/420/w240h180/20180604/aenj-hcmurvh3425662.jpg"><span class="zt_txt">下半场要拼协同效应</span></a></li> 
          </ul>
            <ol class="link_c666 ul_c666">
<li><a href="http://tech.sina.com.cn/csj/2018-06-04/doc-ihcmurvh2609791.shtml" target="_blank">
头条已经没那么重要了</a></li>

<li><a href="http://tech.sina.com.cn/csj/2018-06-04/doc-ihcmurvh2847341.shtml" target="_blank">
曾鸣：互联网的下半场，拼的是协同效应</a></li>            </ol>

        </div>
        
    </div>
    <div class="sp_h10"></div>
    <div class="blk_new_12">
      <div class="Tit_12" style="border-top:none;" id="blk_cswbup_01">
          <div class="t_cont" style="border-top-color:#e7e8eb;">
            <div class="t_name"><a href="http://tech.sina.com.cn/zt/mobile/" target="_blank">专题策划</a></div>
            <div class="t_more"><a href="http://tech.sina.com.cn/zt/mobile/" target="_blank">更多</a></div>
          </div>
        </div>
        <div class="blk_main"  data-sudaclick="tech2_08">
          <ul class="clearfix">
<li><a class="zt_pic_w" href="http://tech.sina.com.cn/zt_d/teslaaccident/" target="_blank"><img class="zt_img" alt="" data-src="http://n.sinaimg.cn/tech/transform/40/w480h360/20180427/Vok--fztkpip3147924.jpg"><span class="zt_txt">特斯拉“生死时速”</span></a></li> 
<li><a class="zt_pic_w" href="http://tech.sina.com.cn/zt_d/meizustruggle/" target="_blank"><img class="zt_img" alt="" data-src="http://n.sinaimg.cn/tech/transform/40/w480h360/20180427/jdUa-fztkpip3163837.jpg"><span class="zt_txt">魅族内讧风波</span></a></li> 
          </ul>
            <ol class="link_c666 ul_c666">
<li><a href="http://tech.sina.com.cn/zt_d/youtubeshot/"  target="_blank">YouTube总部附近发生枪击案：3人受伤</a></li>
<li><a href="http://tech.sina.com.cn/zt_d/dsj/" target="_blank">多公司被曝大数据杀熟 住宿出行是重灾区</a></li>
<li><a href="http://tech.sina.com.cn/zt_d/gioneecrisis/"  target="_blank">金立债务危机90天：裁员50%自救</a></li>            </ol>

        </div>
    </div>
  
  </div>
<!--XBLK_ENDX-->
</div>
<!-- part_tech end -->




<!-- gsps博客读书教育育儿通栏 p_id=1&t_id=912&f_id=28331 -->
<!--t id="news_web_get_gspsdata" pid="1" tid="912" did="1" fid="sp_f28331" cname="博客读书教育育儿通栏"-->
<!-- part_blogbookedubaby begin -->
<div class="part_05 clearfix">
	<div class="p_left">
		<!-- left begin -->
		<div class="partTit_02" id="blk_bktltop_01" data-sudaclick="blog2_tb">
			<div class="pT_name"><a href="http://blog.sina.com.cn/" target="_blank" class="titName ptn_37">博客</a></div>
			<div class="pT_more"><a href="http://blog.sina.com.cn/lm/pic/" target="_blank">图片</a> | <a href="http://blog.sina.com.cn/lm/search/school/" target="_blank">校园</a> | <a href="http://blog.sina.com.cn/lm/zt/" target="_blank">专题</a> | <a href="http://blog.sina.com.cn/lm/mediablog/" target="_blank">媒体</a> | <a href="http://search.blog.sina.com.cn/" target="_blank">搜索</a> | <a href="http://qing.weibo.com/" target="_blank">Qing</a>  　　　<a href="http://blog.sina.com.cn/lm/top/rank/" target="_blank">人气总排行</a> <a href="http://blog.sina.com.cn/lm/rank/" target="_blank">热文排行</a> <a href="http://blog.sina.com.cn/lm/search/class/" target="_blank">名录</a> &nbsp;&nbsp&nbsp;&nbsp;<a href="http://blog.sina.com.cn/" target="_blank">更多&gt;</a></div>
		</div>

		<div class="p_box clearfix">
			<div class="pb_left">

				<!-- 休闲 -->
				<div class="Tit_10" id="blk_blogxxup_01">
					<div class="t_cont">
						<div class="t_name"><a href="http://blog.sina.com.cn/lm/ruiblog/" target="_blank">休闲</a></div>
						<div class="t_more"><a href="http://blog.sina.com.cn/lm/ruiblog/" target="_blank">更多</a></div>
					</div>
				</div>
				<div class="blk_54" id="blk_blogxx_01"  data-sudaclick="blog2_01" style="overflow:hidden;">
					
<div class="ct_p_02 clearfix">
	<div class="ct_box">
	<a href="http://blog.sina.com.cn/s/blog_5d7a54630102xkyv.html" target="_blank">
		<img width="150" height="90" src="http://n.sinaimg.cn/www/transform/480/w300h180/20180531/J5vl-hcikcev5384210.jpg">
		<span class="ct_txt">西藏有个结巴村</span>
	</a>
</div><div class="ct_box">
	<a href="http://blog.sina.com.cn/s/blog_4da73f9f0102xlb0.html" target="_blank">
		<img width="150" height="90" src="http://n.sinaimg.cn/www/transform/480/w300h180/20180531/R6gv-hcikcev5390167.jpg">
		<span class="ct_txt">我镜头里的世界各国的孩子们</span>
	</a>
</div></div>
<ul class="list_12 link_c666">
	<li style="float: left;">
	<a href="http://blog.sina.com.cn/s/blog_bc4d7d7a0102xhr3.html" target="_blank">田园小格子怎么搭有法式风情</a>
</li><li style="float: left;">
	<a href="http://blog.sina.com.cn/s/blog_473d53360102xmtw.html" target="_blank">李银河：新世纪的爱情</a>
</li></ul>
				</div>

				<!-- 星座 -->
				<div class="Tit_10" id="blk_blogxzup_01">
					<div class="t_cont">
						<div class="t_name"><a href="http://astro.sina.com.cn/" target="_blank">星座</a></div>
						<div class="t_more"><a href="http://blog.sina.com.cn/lm/astro/" target="_blank">更多</a></div>
					</div>
				</div>

				<div class="blk_53" id="blk_blogxz_01">
					<div class="ct_pt_07 clearfix"  data-sudaclick="astro2_01">
						<div class="ct_pic">
	<a href="http://slide.astro.sina.com.cn/gif/slide_52_42283_63603.html" target="_blank">
	<img src="http://www.sinaimg.cn/dy/temp/928/2013/0531/U5246P1T928D1F23722DT20180510164000.gif" width="150" height="90"><span class="ct_tit">12星座的神奇一天</span>
</a></div>
<div class="ct_txt">
	<ul class="list_12 link_c666">
		<li><a href="http://astro.sina.com.cn/fate_day_Shu/" target="_blank">[生肖运]</a> <a href="http://blog.sina.com.cn/s/blog_50350d150102xc1n.html" target="_blank">6月逐日吉凶预报</a></li>
        <li><a href="http://astro.sina.com.cn/fate_day_Aries/" target="_blank">[星座运]</a> <a href="http://blog.sina.com.cn/s/blog_be7808710102x4j1.html" target="_blank">克莉丝汀下周运</a></li>
        <li><a href="http://blog.sina.com.cn/s/blog_14552df340102xb7w.html" target="_blank">20天内必翻身的3个生肖</a></li>
        <li><a href="http://blog.sina.com.cn/s/blog_5bd1ddf60102xtdl.html" target="_blank">说说命理中的“好与不好”</a></li>	</ul>
</div>
					</div>
				</div>

			</div>
			<div class="pb_right">
				<div class="blk_55" id="blk_bloglist_01"  data-sudaclick="blog2_list">
					
<div class="ct_t_02" id="blk_bloglist_011">
	<h1><a href="http://blog.sina.com.cn/" target="_blank">崔永元撕范冰冰：娱乐圈掀起多大波澜</a></h1>
</div>

<ul class="list_14">
	<li><a href="http://blog.sina.com.cn/s/blog_1513edc920102xqun.html" target="_blank">移动支付“战役”已进入中场阶段</a></li><li><a href="http://blog.sina.com.cn/s/blog_5f7396520102yk5u.html" target="_blank">律师丁金坤：明星违法逃税法律分析</a></li><li><a href="http://blog.sina.com.cn/s/blog_5054769e0102xzjh.html" target="_blank">马未都：这不能多掺，掺多了没良心</a></li>	<li><a href="http://blog.sina.com.cn/s/blog_4b9c2b820102xe93.html" target="_blank">在普吉岛看西蒙人妖秀</a>    <a href="http://blog.sina.com.cn/s/blog_518cc2930102xkzd.html" target="_blank">夏日清凉性感美女</a></li></ul>

<div class="line_01"></div>

<ul class="list_14">
	<li><a href="http://blog.sina.com.cn/s/blog_49818dcb0102yfrt.html?tj=1" target="_blank">小城房价飞起秘密在这里</a> <a href="http://blog.sina.com.cn/s/blog_5054769e0102xtva.html?tj=1" target="_blank">马未都：风靡全国的懒汉鞋</a></li>

<li><a href="http://blog.sina.com.cn/s/blog_5951b3310102y822.html?tj=1" target="_blank">区块链：恰是裸泳的好地方</a> <a href="http://blog.sina.com.cn/s/blog_70db28510102wz26.html?tj=1" target="_blank">惊！这款网红玩具有剧毒</a></li>

<li><a href="http://blog.sina.com.cn/s/blog_7d75a1df0102xxz0.html?tj=1" target="_blank">90后真正变老的3个标志</a> <a href="http://blog.sina.com.cn/s/blog_4bdc7dbf0102yfx3.html?tj=1" target="_blank">最不好脱单女生类型排行榜</a></li>

<li><a href="http://blog.sina.com.cn/s/blog_1670822940102xo0m.html?tj=1" target="_blank">讨好型人格，是种什么病</a> <a href="http://blog.sina.com.cn/s/blog_7d75a1df0102xy2u.html?tj=1" target="_blank">一个人开始废掉的3种迹象</a></li>

<li><a href="http://blog.sina.com.cn/s/blog_4ee5029e0102xztr.html?tj=1" target="_blank">走起！清华大学赏花攻略</a> <a href="http://blog.sina.com.cn/s/blog_1573584ec0102xw29.html?tj=1" target="_blank">2018年哪些人有机会发大财</a></li></ul>
					<div class="line_01"></div>
				</div>
			</div>
		</div>

		<!-- 读书 -->
		<div class="partTit_02" id="blk_dstltop_01"  data-sudaclick="book2_tb">
			<div class="pT_name"><a href="http://book.sina.com.cn/" target="_blank" class="titName ptn_38">读书</a></div>
			<div class="pT_more"><a href="http://vip.book.sina.com.cn/weibobook/cate.php?cate_id=1036&pos=202053" target="_blank">都市校园</a> | <a href="http://vip.book.sina.com.cn/weibobook/cate.php?cate_id=1006004&pos=202053" target="_blank">总裁豪门</a> | <a href="http://vip.book.sina.com.cn/weibobook/cate.php?cate_id=1003&pos=202053" target="_blank">玄幻奇幻</a> | <a href="http://vip.book.sina.com.cn/weibobook/cate.php?cate_id=1006005&pos=202053" target="_blank">穿越重生</a>&nbsp;&nbsp;&nbsp;&nbsp;<a href="http://book.sina.com.cn/" target="_blank">更多&gt;</a></div>
		</div>

		<div class="p_box clearfix">
			<div class="pb_left">
				<div class="sp_h5"></div>
				<!-- 文史频道 -->

				<div class="blk_new_13" tab-type="tab-wrap"  data-sudaclick="book2_hot">
					<div class="Tit_08 t_mr0">
	<div class="t_name"><a href="http://vip.book.sina.com.cn/weibobook/rank.php" target="_blank">排行</a></div>
	<div class="t_more"><a href="http://vip.book.sina.com.cn/weibobook/rank.php" target="_blank">更多</a></div>
</div>

<div class="blk_main" style="">
	<ul class="tit_list clearfix">
		<li tab-type="tab-nav" class="selected"><a href="http://vip.book.sina.com.cn/weibobook/man.php" target="_blank">男生</a></li>
		<li tab-type="tab-nav"><a href="http://vip.book.sina.com.cn/weibobook/girl.php" target="_blank" style="cursor:default;">女生</a></li>
	</ul>
	<!--{读书排行}-->
	<ol style="" class="topList_12 link_c666" tab-type="tab-cont">
		<li><span class="topNum num1">1</span><a href="http://vip.book.sina.com.cn/weibobook/sina_reader.php?bid=5395792" target="_blank">超级小神医</a></li>

<li><span class="topNum num2">2</span><a target="_blank" href="http://vip.book.sina.com.cn/weibobook/sina_reader.php?bid=5386757" target="_blank">九阳神王</a></li>

<li><span class="topNum num3">3</span><a href="http://vip.book.sina.com.cn/weibobook/sina_reader.php?bid=5372596" target="_blank">绝世武魂</a></li>

<li><span class="topNum num4">4</span><a target="_blank" href="http://vip.book.sina.com.cn/weibobook/sina_reader.php?bid=5372757" target="_blank">另类保镖：美女总裁爱上我</a></li>

<li><span class="topNum num5">5</span><a target="_blank" href="http://vip.book.sina.com.cn/weibobook/sina_reader.php?bid=5387975">万古丹帝</a></li>	</ol>

	<ol style="display:none;" class="topList_12 link_c666" tab-type="tab-cont">
		<li><span class="topNum num1">1</span><a href="http://vip.book.sina.com.cn/weibobook/sina_reader.php?bid=5386863" target="_blank">错嫁替婚总裁</a></li>

<li><span class="topNum num2">2</span><a href="http://vip.book.sina.com.cn/weibobook/sina_reader.php?bid=5350213" target="_blank">天价宠儿：总裁的新妻</a></li>

<li><span class="topNum num3">3</span><a href="http://vip.book.sina.com.cn/weibobook/sina_reader.php?bid=5399975" target="_blank">残王傻妃：代嫁神医七小姐</a></li>

<li><span class="topNum num4">4</span><a target="_blank" href="http://vip.book.sina.com.cn/weibobook/sina_reader.php?bid=5373077" target="_blank">蔓蔓婚路</a></li>
        
<li><span class="topNum num5">5</span><a target="_blank" href="http://vip.book.sina.com.cn/weibobook/sina_reader.php?bid=5386270" target="_blank">情深入骨：帝少的独家宠溺</a></li>	</ol>
</div>
				</div>

			</div>
			<div class="pb_right">
				<div class="blk_56" id="blk_booklist_01" data-sudaclick="book2_list">
					<div class="ct_t_02" id="blk_booklist_011">
  <h1><a href="http://vip.book.sina.com.cn/weibobook/sina_reader.php?bid=5394749">许你诺言，赠我欢颜</a></h1>
</div><div class="clearfix">
  <ul class="list_14">
<li><a href="http://vip.book.sina.com.cn/weibobook/sina_reader.php?bid=5390667" target="_blank">村夫凶猛：特种兵王在山村</a></li> 
<li><a href="http://vip.book.sina.com.cn/weibobook/sina_reader.php?bid=5394291" target="_blank">传奇再现：都市逍遥小符医</a></li>
<li><a href="http://vip.book.sina.com.cn/weibobook/sina_reader.php?bid=5352242" target="_blank">回到晚清特种狙击手的逆袭</a></li>
<li><a href="http://vip.book.sina.com.cn/weibobook/sina_reader.php?bid=5385352" target="_blank">夜店红人：花花世界情感颂</a></li> 
<li><a href="http://vip.book.sina.com.cn/weibobook/sina_reader.php?bid=5372731" target="_blank">斗天武神：废材逆袭斗天地</a></li>
<li><a href="http://vip.book.sina.com.cn/weibobook/sina_reader.php?bid=240984" target="_blank">从蛮荒走出的强者征战四方</a></li>
      </ul>
<ul class="list">
<li><a href="http://vip.book.sina.com.cn/weibobook/sina_reader.php?bid=5373279" target="_blank">战王宠妻入骨：绝色小医妃</a></li> 
<li><a href="http://vip.book.sina.com.cn/weibobook/sina_reader.php?bid=5372753" target="_blank">豪门圈宠：失守的绯色游戏</a></li>
<li><a href="http://vip.book.sina.com.cn/weibobook/sina_reader.php?bid=5388804" target="_blank">鬼医宠妃，冷傲王爷请走开</a></li>
<li><a href="http://vip.book.sina.com.cn/weibobook/sina_reader.php?bid=5400129" target="_blank">拒嫁前夫：顾少，别强撩</a></li> 
<li><a href="http://vip.book.sina.com.cn/weibobook/sina_reader.php?bid=5390659" target="_blank">闪婚蜜爱：慕少的心尖萌妻</a></li>
<li><a href="http://vip.book.sina.com.cn/weibobook/sina_reader.php?bid=5401026" target="_blank">神帝嗜宠：九尾狐妃千千岁</a></li></ul>
</div>
				</div>
			</div>
		</div>


		<!-- 教育 -->
		<div class="partTit_02" id="blk_jytltop_01"  data-sudaclick="edu2_tb">
			<div class="pT_name"><a href="http://edu.sina.com.cn/" target="_blank" class="titName ptn_39">教育</a><a href="http://edu.sina.com.cn/gaokao/" target="_blank" class="titName ptn_40">考试</a></div>
			<div class="pT_more"><a href="http://edu.sina.com.cn/gaokao/" target="_blank">高考</a> <a href="http://edu.sina.com.cn/college/" target="_blank">大学院校库</a> <a href="http://zhiyuan.edu.sina.com.cn/" target="_blank">高考志愿通</a>|<a href="http://edu.sina.com.cn/kaoyan/" target="_blank">考研</a>|<a href="http://edu.sina.com.cn/official/" target="_blank">公务员</a>|<a href="http://edu.sina.com.cn/zhongkao/" target="_blank">中考</a>|<a href="http://edu.sina.com.cn/zxx/" target="_blank">中小学</a>|<a href="http://edu.sina.com.cn/foreign/" target="_blank">外语</a>|<a href="http://edu.sina.com.cn/a/" target="_blank">出国</a>|<a href="http://edu.sina.com.cn/bschool/" target="_blank">商学院</a>|<a href="http://edu.sina.com.cn/ischool/gjxxzx/" target="_blank">国际学校</a> <a href="http://edu.sina.com.cn/" target="_blank">更多&gt;</a></div>
		</div>

		<div class="p_box clearfix">
			<div class="pb_left" style="border-bottom:none;">
				<div class="sp_h10"></div>
				<div class="blk_54" id="blk_jywspd_01">
					<div class="ct_p_02 clearfix"  data-sudaclick="edu2_01">
						
<div class="blk_54" id="blk_jywspd_01">
	<div class="ct_p_02 clearfix">
		<div class="ct_box"><a href="http://slide.edu.sina.com.cn/slide_11_611_381721.html" target="_blank">
<img width="150" height="90" src="http://n.sinaimg.cn/edu/transform/480/w300h180/20180528/8tHT-hcaquev4479359.jpg">
<span class="ct_txt">清新校花竟酷似刘诗诗</span>
</a></div><div class="ct_box"><a href="http://slide.edu.sina.com.cn/slide_11_611_381785.html" target="_blank">
<img width="150" height="90" src="http://n.sinaimg.cn/edu/transform/480/w300h180/20180528/qip4-hcaquev4482612.jpg">
<span class="ct_txt">首批“00后”备战高考</span>
</a></div>	</div>
</div>
					</div>
				</div>

				<div class="sp_h10"></div>
				<div class="Tit_11" id="blk_jyxwphmore_01">
					<div class="t_name"><a href="http://edu.sina.com.cn/toplist/day_hotnews.shtml" target="_blank">教育新闻排行</a></div>
					<div class="t_more"><a href="http://edu.sina.com.cn/toplist/day_hotnews.shtml" target="_blank">更多</a></div>
				</div>

				<div class="TMenu_07x" id="blk_jyxwphup_01">
					<ul>
						<li id="tab_jyxwph_05" class="selected"><a href="http://edu.sina.com.cn/gaokao/" target="_blank">高考</a></li>
						<li id="tab_jyxwph_01"><a href="http://edu.sina.com.cn/bschool/" target="_blank">商学院</a></li>
						<li id="tab_jyxwph_02"><a href="http://edu.sina.com.cn/a/" target="_blank">出国</a></li>
						<li id="tab_jyxwph_03"><a href="http://edu.sina.com.cn/zxx/" target="_blank">中小学</a></li>
						<li id="tab_jyxwph_04"><a href="http://edu.sina.com.cn/foreign/" target="_blank">外语</a></li>
						<li id="tab_jyxwph_06"><a href="http://edu.sina.com.cn/official/" target="_blank">公务员</a></li>
					</ul>
				</div>

				<div class="blk_57" id="blk_jyxwph_05">
					<ol class="topList_12 link_c666" id="blk_jyxwph_015"  data-sudaclick="edu2_hot01"></ol>
					<!-- 高考 begin -->
					<script type="text/javascript">
						function showContentgaokao(data_arr) {
							var html= '';
							data = data_arr['data'];
							var nu = 0;
							for(var i in data){
								++nu;
								var tmptitle = data[i].title;
								if (nu<4) {
									html += '<li><span class="topNum num'+nu+'">'+nu+'</span><a target="_blank" href="'+data[i].url+'">'+data[i].title.gbCut(44)+'</a></li>';
								} else {
									html += '<li><span class="topNum">'+nu+'</span><a target="_blank" href="'+data[i].url+'">'+data[i].title.gbCut(44)+'</a></li>';
								}
							}
							document.getElementById('blk_jyxwph_015').innerHTML = html;
						}
					</script>
					<!-- 高考 end -->
				</div>

				<div class="blk_57" id="blk_jyxwph_01" style="display:none">
					<ol class="topList_12 link_c666" id="blk_jyxwph_011" data-sudaclick="edu2_hot02">
						<!-- 商学院 begin -->
						<script type="text/javascript">
							function showContentbschool(data_arr) {
								var html= '';
								data = data_arr['data'];
								var nu = 0;
								for(var i in data){
									++nu;
									var tmptitle = data[i].title;
									if (nu<4) {
										html += '<li><span class="topNum num'+nu+'">'+nu+'</span><a target="_blank" href="'+data[i].url+'">'+data[i].title.gbCut(44)+'</a></li>';
									} else {
										html += '<li><span class="topNum">'+nu+'</span><a target="_blank" href="'+data[i].url+'">'+data[i].title.gbCut(44)+'</a></li>';
									}
								}
								document.getElementById('blk_jyxwph_011').innerHTML = html;
							}
						</script>
						<!-- 商学院 end -->
					</ol>
				</div>
				<div class="blk_57" id="blk_jyxwph_02" style="display:none">
					<ol class="topList_12 link_c666" id="blk_jyxwph_012" data-sudaclick="edu2_hot03"></ol>
					<!-- 留学 begin -->
					<script type="text/javascript">
						function showContentstudyaboard(data_arr) {
							var html= '';
							data = data_arr['data'];
							var nu = 0;
							for(var i in data){
								++nu;
								var tmptitle = data[i].title;
								if (nu<4) {
									html += '<li><span class="topNum num'+nu+'">'+nu+'</span><a target="_blank" href="'+data[i].url+'">'+data[i].title.gbCut(44)+'</a></li>';
								} else {
									html += '<li><span class="topNum">'+nu+'</span><a target="_blank" href="'+data[i].url+'">'+data[i].title.gbCut(44)+'</a></li>';
								}
							}
							document.getElementById('blk_jyxwph_012').innerHTML = html;
						}
					</script>
					<!-- 留学 end -->

				</div>
				<div class="blk_57" id="blk_jyxwph_03" style="display:none">
					<ol class="topList_12 link_c666" id="blk_jyxwph_013" data-sudaclick="edu2_hot04"></ol>
					<!-- 中小学 begin -->
					<script type="text/javascript">
						function showContentzxiaoxue(data_arr) {
							var html= '';
							data = data_arr['data'];
							var nu = 0;
							for(var i in data){
								++nu;
								var tmptitle = data[i].title;
								if (nu<4) {
									html += '<li><span class="topNum num'+nu+'">'+nu+'</span><a target="_blank" href="'+data[i].url+'">'+data[i].title.gbCut(44)+'</a></li>';
								} else {
									html += '<li><span class="topNum">'+nu+'</span><a target="_blank" href="'+data[i].url+'">'+data[i].title.gbCut(44)+'</a></li>';
								}
							}
							document.getElementById('blk_jyxwph_013').innerHTML = html;
						}
					</script>
					<!-- 中小学 end -->

				</div>
				<div class="blk_57" id="blk_jyxwph_04" style="display:none">
					<ol class="topList_12 link_c666" id="blk_jyxwph_014" data-sudaclick="edu2_hot05"></ol>
					<!-- 外语 begin -->
					<script type="text/javascript">
						function showContentenglish(data_arr) {
							var html= '';
							data = data_arr['data'];
							var nu = 0;
							for(var i in data){
								++nu;
								var tmptitle = data[i].title;
								if (nu<4) {
									html += '<li><span class="topNum num'+nu+'">'+nu+'</span><a target="_blank" href="'+data[i].url+'">'+data[i].title.gbCut(44)+'</a></li>';
								} else {
									html += '<li><span class="topNum">'+nu+'</span><a target="_blank" href="'+data[i].url+'">'+data[i].title.gbCut(44)+'</a></li>';
								}
							}
							document.getElementById('blk_jyxwph_014').innerHTML = html;
						}
					</script>
					<!-- 外语 end -->

				</div>

				<div class="blk_57" id="blk_jyxwph_06" style="display:none">
					<ol class="topList_12 link_c666" id="blk_jyxwph_016" data-sudaclick="edu2_hot06"></ol>
					<!-- 公务员 begin -->
					<script type="text/javascript">
						function showContentoffical(data_arr) {
							var html= '';
							data = data_arr['data'];
							var nu = 0;
							for(var i in data){
								++nu;
								var tmptitle = data[i].title;
								if (nu<4) {
									html += '<li><span class="topNum num'+nu+'">'+nu+'</span><a target="_blank" href="'+data[i].url+'">'+data[i].title.gbCut(44)+'</a></li>';
								} else {
									html += '<li><span class="topNum">'+nu+'</span><a target="_blank" href="'+data[i].url+'">'+data[i].title.gbCut(44)+'</a></li>';
								}
							}
							document.getElementById('blk_jyxwph_016').innerHTML = html;
						}
					</script>
					<!-- 公务员 end -->

				</div>

				<script type="text/javascript">
					jsLoader(ARTICLE_JSS.common,function(){
						var subshow = new SubShowClass('none','onmouseover');
						//subshow.addLabel('tab_jyxwph_01','blk_jyxwph_01', '', 'jsLoader("http://top.blog.sina.com.cn/ws/GetTopDataList.php?top_type=day&top_cat=jy&top_time=today&top_show_num=5&top_order=DESC&js_var=jy_1_data&call_back=showContentblog")');

						subshow.addLabel('tab_jyxwph_05','blk_jyxwph_05', '', 'jsLoader("http://top.edu.sina.com.cn/ws/GetTopDataList.php?top_type=day&top_cat=edu_gaokao_suda&top_time=today&top_show_num=5&top_order=desc&js_var=gaokao_1_data&call_back=showContentgaokao")');
						subshow.addLabel('tab_jyxwph_01','blk_jyxwph_01', '', 'jsLoader("http://top.edu.sina.com.cn/ws/GetTopDataList.php?top_type=day&top_cat=edu_bschool_suda&top_time=today&top_show_num=5&top_order=desc&js_var=bschool_1_data&call_back=showContentbschool")');
						subshow.addLabel('tab_jyxwph_02','blk_jyxwph_02', '', 'jsLoader("http://top.edu.sina.com.cn/ws/GetTopDataList.php?top_type=day&top_cat=edu_chuguo_suda&top_time=today&top_show_num=5&top_order=desc&js_var=studyaboard_1_data&call_back=showContentstudyaboard")');
						subshow.addLabel('tab_jyxwph_03','blk_jyxwph_03', '', 'jsLoader("http://top.edu.sina.com.cn/ws/GetTopDataList.php?top_type=day&top_cat=edu_zxx_suda&top_time=today&top_show_num=5&top_order=desc&js_var=zxiaoxue_1_data&call_back=showContentzxiaoxue")');
						subshow.addLabel('tab_jyxwph_04','blk_jyxwph_04', '', 'jsLoader("http://top.edu.sina.com.cn/ws/GetTopDataList.php?top_type=day&top_cat=edu_waiyu_suda&top_time=today&top_show_num=5&top_order=desc&js_var=english_1_data&call_back=showContentenglish")');
						subshow.addLabel('tab_jyxwph_06','blk_jyxwph_06', '', 'jsLoader("http://top.edu.sina.com.cn/ws/GetTopDataList.php?top_type=day&top_cat=edu_official_suda&top_time=today&top_show_num=5&top_order=desc&js_var=offical_1_data&call_back=showContentoffical")');
						//subshow.random(1,1,1,1,1,1);
						subshow.random(1,0,0,0,0,0);

					});
				</script>

			</div>
			<div class="pb_right">
				<div class="blk_56" id="blk_jylist_01" data-sudaclick="edu2_list">
					<div class="ct_t_02" id="blk_jylist_011"><h1><a target="_blank" href="http://edu.sina.com.cn/">“00后”登场加分政策收紧 今年高考新特征</a></h1></div><div class="clearfix">
<ul class="list_14">
<li><a target="_blank" href="http://edu.sina.com.cn/gaokao/">男老师扮华妃祝福学生高考</a></li>
<li><a target="_blank" href="http://edu.sina.com.cn/gaokao/2018-06-04/doc-ihcmurvh2787326.shtml">高考期间华北高温华南台风</a></li>
<li><a target="_blank" href="http://edu.sina.com.cn/gaokao/2018-06-02/doc-ihcikcew2754749.shtml">2018考生必知的考场规则</a></li>
<li><a target="_blank" href="http://edu.sina.com.cn/gaokao/2018-06-03/doc-ihcikcew2812606.shtml">如何有效缓解考前焦虑？</a></li>
<li><a target="_blank" href="http://edu.sina.com.cn/gaokao/2018-06-03/doc-ihcmurvf8131113.shtml">营养师告诉你高考前怎么吃</a></li>
<li><a target="_blank" href="http://edu.sina.com.cn/gaokao/2018-06-04/doc-ihcmurvh6135849.shtml">避免高分落榜的3个诀窍！</a></li>







<li><a target="_blank" href="http://edu.sina.com.cn/gaokao/2018-06-01/doc-ihcikcew1793008.shtml">如何利用高校历年分数线？</a></li>


<li><a target="_blank" href="http://edu.sina.com.cn/gaokao/2018-05-31/doc-ihcikcev5956805.shtml">误解分数线差点高分落榜！</a></li>
<li><a target="_blank" href=" http://edu.sina.com.cn/zxx/">小学老师“跪求”辞职爆红</a></li>
<li><a target="_blank" href="http://edu.sina.com.cn/zxx/2018-06-03/doc-ihcmurvf8283086.shtml">香港小一派位6月2日揭晓</a></li>
<li><a target="_blank" href="http://edu.sina.com.cn/l/2018-06-01/doc-ihcikcew2328077.shtml">周报：阿里或入局宝宝树</a></li>

</ul>
<ul class="list">
<li><a target="_blank" href="http://edu.sina.com.cn/a">世界大学排名中心新榜出炉</a></li>
<li><a target="_blank" href="http://edu.sina.com.cn/a/2018-06-04/doc-ihcmurvh2962783.shtml">华裔反对纽约特殊高中改革</a></li>
<li><a target="_blank" href="http://edu.sina.com.cn/a/2018-06-04/doc-ihcmurvh3286111.shtml">中华文化成留学申请加分项</a></li>
<li><a target="_blank" href="http://edu.sina.com.cn/a/2018-06-04/doc-ihcmurvh3205998.shtml">在美留学生与父母失联数日</a></li>
<li><a target="_blank" href="http://edu.sina.com.cn/ischool">严管学籍催生另类上学难</a></li>
<li><a href="http://edu.sina.com.cn/ischool/2018-06-04/doc-ihcmurvh3083736.shtml" target="_blank">印度人在美做CEO我们呢</a></li>
<li><a href="http://blog.sina.com.cn/s/blog_9ec6cf980102xyxu.html" target="_blank">美国孩子要“背单词”吗？</a></li>
<li><a href="http://blog.sina.com.cn/s/blog_4cd1c1670102xhwh.html" target="_blank">日本农村竟如此重视教育</a></li>
<li><a href="http://edu.sina.com.cn/bschool/" target="_blank">如何在职场上高效的沟通？</a></li>
<li><a href="http://v.sina.com.cn/2018-06-04/detail-ihcmurvh2883083.d.html" target="_blank" class="videoNewsLeft">万名考生放孔明灯祈福</a></li><li><a href="http://edu.sina.com.cn/bschool/2018-06-04/doc-ihcmurvh2995076.shtml" target="_blank">国内需要这几类MBA的人才</a></li></ul></div>
				</div>
			</div>
		</div>
		<!-- left end -->
	</div>
	<!--XBLK_STARTX-->
	<div class="p_right">
		<!-- right begin -->

		<!-- 城市 微博 -->

		<div class="Tit_12" style="border-top:none;" id="blk_cswbup_01">
			<div class="t_cont" style="border-top-color:#e7e8eb;">
				<div class="t_name"><a href="http://city.sina.com.cn/" target="_blank">城市</a><span class="dot">·</span><a href="http://weibo.com/happycity/" target="_blank">微博</a></div>
				<div class="t_more"><a href="http://city.sina.com.cn/" target="_blank">更多</a></div>
			</div>
		</div>
		<div class="blk_58" id="blk_cswb_01"  data-sudaclick="blk_city">
			<div class="ct_pt_07 clearfix">
	<div class="ct_pic">
		<a href="http://city.sina.com.cn/" target="_blank"><img src="http://n.sinaimg.cn/default/transform/380/w190h190/20180604/HyDY-hcmurvh4628752.jpg" width="85" height="85" alt=""><span class="ct_tit">甘肃“天路”</span></a>	</div>
	<div class="ct_txt">
		<ul class="list_12 link_c666">
			<li><a href="http://city.sina.com.cn/" target="_blank">6月1日政务热点简报</a></li><li><a href="http://city.sina.com.cn/focus/t/2018-06-04/detail-ihcmurvh3393903.shtml" target="_blank">11座城市上榜传销黑名单</a></li><li><a href="http://city.sina.com.cn/focus/t/2018-06-04/detail-ihcmurvh3408132.shtml" target="_blank">多城市出台招揽人才政策</a></li><li><a href="http://city.sina.com.cn/focus/t/2018-06-04/detail-ihcmurvh3428935.shtml" target="_blank">长三角一体化路线图发布</a></li>		</ul>
	</div>
</div>
<ul class="list_12 link_c666">
	<li><a href="http://city.sina.com.cn/focus/t/2018-06-04/detail-ihcmurvh3360721.shtml" target="_blank">北京5324个开墙打洞点今年集中修补</a></li><li><a href="http://city.sina.com.cn/focus/t/2018-06-04/detail-ihcmurvh3497828.shtml" target="_blank">粤港两地将合作参与国家“一带一路”建设</a></li></ul>
		</div>

		<!-- 图片 -->
		<div class="Tit_12" id="blk_tpup_01">
			<div class="t_cont">
				<div class="t_name"><a href="http://blog.sina.com.cn/lm/pic/" target="_blank">图片</a></div>
				<div class="t_more"><a href="http://blog.sina.com.cn/lm/pic/" target="_blank">更多</a></div>
			</div>
		</div>

		<div class="blk_58" id="blk_tp_01">
			<div class="ct_pt_07 clearfix"   data-sudaclick="blog2_pic">
				

<div class="ct_pic">
	<a href="http://blog.sina.com.cn/lm/pic/" target="_blank"><img src="http://www.sinaimg.cn/dy/2018/0521/U4362P1DT20180521151908.jpg" width="85" height="85" alt="" /><span class="ct_tit">真实的肯尼亚</span></a></div>
<div class="ct_txt">
	<ul class="list_12 link_c666">
		<li><a href="http://blog.sina.com.cn/s/blog_49e7fd870102y652.html" target="_blank">白色恋人娄艺潇</a></li><li><a href="http://blog.sina.com.cn/s/blog_5dcf3a360102xy2d.html" target="_blank">去桃源仙谷看山泉瀑布</a></li><li><a href="http://blog.sina.com.cn/s/blog_7115eb140102xkm2.html" target="_blank">南宁的美食街太惊艳</a></li><li><a href="http://blog.sina.com.cn/s/blog_4e3ccfdd0102xce6.html" target="_blank">他们在这里一吻定情</a></li>	</ul>
</div>
			</div>
		</div>


		<!-- 育儿 -->
		<div class="Tit_12" id="blk_yrup_01">
			<div class="t_cont">
				<div class="t_name"><a href="http://baby.sina.com.cn/" target="_blank">育儿</a></div>
				<div class="t_more"><a href="http://baby.sina.com.cn/" target="_blank">更多</a></div>
			</div>
		</div>

		<div class="blk_58" id="blk_yr_01" data-sudaclick="baby2_01">
			<div class="b_tc" >
				<a href="http://baby.sina.com.cn/photo/" target="_blank">图库</a> |<!-- <a href="http://baby.sina.com.cn/tv/" target="_blank">百家百问百答</a>-->  <a href="http://baby.sina.com.cn/zt_d/yyxy" target="_blank">母婴营养学院</a> | <a href="http://baby.sina.com.cn/z/sinababyapp/" target="_blank" class="linkRed">育儿专家问答客户端</a>
			</div>

			<div class="line_01"></div>

			
<div class="ct_pt_07 clearfix">
		<div class="ct_pic">
				<p><a href="http://baby.sina.com.cn/" target="_blank">
			<img src="http://n.sinaimg.cn/baby/165/w80h85/20180604/4WA8-hcmurvh2671592.jpg" width="80" height="85" alt="">		   
			<span class="ct_tit">六一爸妈听我说</span></a>
		</p>
	</div>

	<div class="ct_txt">
		<ul class="list_12 link_c666">
			<li><a href="http://baby.sina.com.cn" target="_blank">余文乐晒儿子大长腿</a></li><li><a href="http://baby.sina.com.cn/health/mmjk/hzbhy/2018-06-04/doc-ihcikcev9626633.shtml" target="_blank">子宫内膜损伤能生娃</a></li><li><a href="http://baby.sina.com.cn/health/mmjk/hfmq/2018-06-04/doc-ihcikcew0431980.shtml" target="_blank">下雨不能剖宫产？</a></li><li><a href="http://baby.sina.com.cn/health/mmjk/hzbhy/2018-06-04/doc-ihcikcev3895062.shtml" target="_blank">高考遇大姨妈怎办</a></li>	
		</ul>
	</div>	
</div>

<div class="ct_pt_07 clearfix">
		<div class="ct_pic">
				<p><a href="http://slide.baby.sina.com.cn/bbshai/slide_10_846_391795.html" target="_blank">
			<img src="http://n.sinaimg.cn/baby/165/w80h85/20180604/_ICQ-fzrwiaz6252467.jpg" width="80" height="85" alt="">		   
			<span class="ct_tit">阿拉蕾变小仙女</span></a>
		</p>
	</div>

	<div class="ct_txt">
		<ul class="list_12 link_c666">
			<li><a href="http://baby.sina.com.cn/wemedia/edu/2018-06-04/doc-ihcikcew1963413.shtml" target="_blank">戏精妈妈有多可怕？</a></li><li><a href="http://baby.sina.com.cn/wemedia/edu/2018-06-04/doc-ihcikcew1943502.shtml" target="_blank">鼓励孩子别只夸聪明</a></li><li><a href="http://baby.sina.com.cn/wemedia/ask/2018-06-04/doc-ihcikcew2187812.shtml" target="_blank">宝宝肚子疼的原因</a></li><li><a href="http://baby.sina.com.cn/wemedia/health/2018-06-04/doc-ihcikcew1242838.shtml" target="_blank">孕期哪件事你最关心</a></li>	
		</ul>
	</div></div>
<ul class="list_12 link_c666">
	<li><a href="http://slide.baby.sina.com.cn/mxx/slide_10_846_391804.html" target="_blank">蔡国庆晒儿</a> 
<a href="http://slide.baby.sina.com.cn/bbshai/slide_10_846_391801.html" target="_blank">嗯哼见容祖儿</a>
<a href="http://slide.baby.sina.com.cn/mxx/slide_10_846_391927.html" target="_blank">雪梨办百日宴</a></li>

<li>
<a href="https://weibo.com/1655524143/Gh4M2xr0M" target="_blank">无痛分娩推广难</a> 
<a href="https://weibo.com/1655524143/Gh6r7rQzt" target="_blank">生命奇迹</a>  
<a href="https://weibo.com/1655524143/GhbncfDS1" target="_blank">迪士尼神秘套房</a></li>


<li>
<a href="http://baby.sina.com.cn/health/bbjk/hxlq/2018-06-04/doc-ihcffhsu8502306.shtml" target="_blank">儿童尿床早治疗</a> 
<a target="_blank" href="http://baby.sina.com.cn/health/bbjk/hxlq/2018-06-04/doc-ihcikcew0359014.shtml">孩患心病怎办</a> 
<a target="_blank" href="http://baby.sina.com.cn/health/bbjk/hxlq/2018-06-04/doc-ihcffhsv5490783.shtml">备考少吃甜</a></li>


<li>
<a href="http://baby.sina.com.cn/edu/xlxwyy/2018-06-02/doc-ifysqfnf7665563.shtml" target="_blank">没表扬或强迫症</a> 
<a href="http://baby.sina.com.cn/edu/jtjy/2018-06-02/doc-ihaysviy5981982.shtml" target="_blank">狼性教育极端</a> 
<a target="_blank" href="http://baby.sina.com.cn/edu/jtjy/2018-06-02/doc-ihaysviy7052219.shtml">非常规教子</a></li>

<li>
<a target="_blank" href="http://baby.sina.com.cn/original/dakayuer/4/">黄奕谈女儿</a> 
<a target="_blank" href="http://baby.sina.com.cn/original/dakayuer/7/">关喆如何带二孩</a> 
<a target="_blank" href="http://baby.sina.com.cn/z/zhangziyi/">章子怡育儿观</a></li>

<li><a href="http://baby.sina.com.cn/news/2018-06-04/doc-ihcmurvh2517339.shtml" target="_blank">宫颈癌疫苗怎打</a>  
<a href="http://baby.sina.com.cn/news/2018-06-04/doc-ihcmurvh2390451.shtml" target="_blank">租房入学</a> 
<a target="_blank" href="http://baby.sina.com.cn/news/2018-06-04/doc-ihcmurvh2424319.shtml">感冒啥时吃药</a></li></ul>

		</div>
		<!-- 活动合作 -->
		<div class="Tit_12" id="blk_hdhzup_01">
			<div class="t_cont">
				<div class="t_name"><a href="http://open.sina.com.cn/" target="_blank">精彩教育视频</a></div>
				<div class="t_more"><a href="http://open.sina.com.cn/" target="_blank">更多</a></div>
			</div>
		</div>

		<div class="blk_58" id="blk_hdhz_01">
			<ul class="list_12 link_c666" data-sudaclick="edu2_jysp">
				
<li><a href="http://video.sina.com.cn/p/edu/news/doc/2018-05-29/110468615237.html" target="_blank" class="videoNewsLeft" class="linkRed">美院毕业展雕塑作品神还原表情包</a></li><li><a href="http://video.sina.com.cn/p/edu/news/doc/2018-05-28/100968597112.html" target="_blank" class="videoNewsLeft" class="linkRed">高考数学“命题帝”葛军今年还出题吗</a></li>
			</ul>
		</div>

		<!-- right end -->
		<div style="padding-top:20px; background:#fff;"  data-sudaclick="city_pic">
			<a href="http://city.sina.com.cn/city/zwxmtxy/index.shtml" target="_blank"><img width="260" height="120"  src="http://www.sinaimg.cn/dy/2017/0313/U4220P1DT20170313141055.jpg" alt="" /></a>
		</div>
	</div>
	<!--XBLK_ENDX-->
</div>
<!-- part_blogbookedubaby end -->



<!-- AD tl07 begin -->
<!--XAD_STARTX-->
<!--_SINA_ADS_BEGIN_-->
<div style="margin-top:10px;text-align:center;"></div>
<!--_SINA_ADS_END_-->
<!--XAD_ENDX-->
<!-- AD tl07 end -->


<!-- gsps历史通栏 p_id=1&t_id=912&f_id=28332 -->
<!--t id="news_web_get_gspsdata" pid="1" tid="912" did="1" fid="sp_f28332" cname="历史通栏"-->
<!-- part_history begin -->
<div class="partTit_02" id="blk_nxtltop_01"  data-sudaclick="ls2_tb">
	<div class="pT_name"><a href="http://history.sina.com.cn/" target="_blank" class="titName ptn_new_01">历史</a></div>
	<div class="pT_more"><a href="http://history.sina.com.cn/zt/" target="_blank">重磅策划</a> | <a href="http://history.sina.com.cn/digest/" target="_blank">史海钩沉</a> | <a href="http://blog.sina.com.cn/lm/book/" target="_blank">博客</a> | <a href="http://cul.history.sina.com.cn/" target="_blank">文化频道</a>&nbsp;&nbsp&nbsp;&nbsp;<a href="http://history.sina.com.cn/" target="_blank">更多&gt;</a></div>
</div>

<div class="part_03 clearfix">
	<div class="p_left">
		<div class="blk_54" id="blk_bookwspd_01"   data-sudaclick="ls2_01">
			<div class="ct_p_02 clearfix">
	<div class="ct_box"><a href="http://blog.sina.com.cn/s/blog_50d4ea0e0102wd6y.html?tj=hist" target="_blank"><img width="150" height="90" src="http://n.sinaimg.cn/history/3fce06bf/20160307/hh8.jpg"><span class="ct_txt">80年代农村精彩老照片</span></a></div><div class="ct_box"><a href="http://blog.sina.com.cn/s/blog_5ec5b67a0102w32q.html?tj=1" target="_blank"><img width="150" height="90" src="http://n.sinaimg.cn/history/3fce06bf/20160307/fpr.jpg"><span class="ct_txt">侵华鬼子兵的45只饭盒</span></a></div></div>
<ul class="list_12 link_c666">
	<li><a href="http://blog.sina.com.cn/s/blog_4b3398b60102w9ee.html?tj=1" target="_blank">南谭北许：与许世友齐名的武林高手</a></li><li><a href="http://blog.sina.com.cn/s/blog_b38c044d0102wasq.html?tj=1" target="_blank">毛泽东在上海收获革命“第一桶金”</a></li><li><a href="http://blog.sina.com.cn/s/blog_62de07120102wdmq.html" target="_blank">明犯强汉者虽远必诛：说这话差点被灭族</a></li><li><a href="http://blog.sina.com.cn/s/blog_a1929b370102wiu7.html?tj=1" target="_blank">谁是大唐终结者：乱世枭雄朱温</a></li></ul>
		</div>
	</div>
	<div class="p_middle">
		<div class="blk_56" data-sudaclick="ls2_list">
			
<div class="ct_t_02" id="blk_booklist_011" style="padding-bottom:13px;">
  <h1><a target="_blank" href="http://blog.sina.com.cn/lm/history/">虚构机关重重？盗墓最怕遇到什么</a></h1>
</div>
<div class="clearfix">
	<ul class="list_14">
		<li><a target="_blank" href="http://blog.sina.com.cn/s/blog_9ceb761b0102xk0f.html">权谋韩非：法术势与性恶论</a></li><li><a target="_blank" href="http://blog.sina.com.cn/s/blog_4c622f220102x0ci.html">历史上近乎完美的太子萧统</a></li><li><a target="_blank" href="http://blog.sina.com.cn/s/blog_5fd385580102xn0i.html">奈何闯王李自成只愿做宋江</a></li><li><a target="_blank" href="http://blog.sina.com.cn/s/blog_4f8cf1540102xlbl.html">“五胡乱华”对汉族的影响</a></li><li><a target="_blank" href="http://blog.sina.com.cn/s/blog_603ca7490102xz2l.html">李颙：大儒达到的读书至境</a></li>	</ul>
	<ul class="list">
		<li><a target="_blank" href="http://blog.sina.com.cn/s/blog_4c45664e0102xsld.html">梁贵人如何赢得了皇后宝座</a></li><li><a target="_blank" href="http://blog.sina.com.cn/s/blog_5815b8340102xm5x.html">看风水看出的《富春山居图》</a></li><li><a target="_blank" href="http://blog.sina.com.cn/s/blog_146e884ce0102xir9.html">抗击外族的民族英雄邓子龙</a></li><li><a target="_blank" href="http://blog.sina.com.cn/s/blog_562775eb0102y4dw.html">政治天才贾谊玩儿不了政治</a></li><li><a target="_blank" href="http://blog.sina.com.cn/s/blog_a1929b370102xt7f.html">东条英机：顶罪的头号战犯</a></li>	</ul>
</div>
		</div>
	</div>
	<!--XBLK_STARTX-->
	<div class="p_right">
		<div class="blk_51" id="blk_new_read">
			<div class="b_cont">
				<div class="ct_p_05 clearfix" id="scrPic_new_read" data-sudaclick="ls2_02" style="padding-top:24px;">
					
<div class="ct_pic"><a href="http://blog.sina.com.cn/s/blog_475b012a0102wb13.html" target="_blank"><img src="http://n.sinaimg.cn/history/3fce06bf/20160307/sjj.jpg" width="240" height="144" />
<span class="ct_txt">20世纪精彩的历史瞬间</span></a></div><div class="ct_pic"><a href="http://blog.sina.com.cn/s/blog_131809e140102w6uq.html" target="_blank"><img src="http://n.sinaimg.cn/history/e2da3f0c/20160225/crhb.jpg" width="240" height="144" />
<span class="ct_txt">日本侵华时期战时刊物</span></a></div><div class="ct_pic"><a href="http://slide.history.sina.com.cn/y/slide_61_40602_65896.html" target="_blank"><img src="http://www.sinaimg.cn/dy/2015/1228/U3093P1DT20151228094608.jpg" width="240" height="144" />
<span class="ct_txt">别看韩剧了！这才是百年前真实朝鲜</span></a></div><div class="ct_pic"><a href="http://slide.history.sina.com.cn/y/slide_61_40602_65950.html" target="_blank"><img src="http://www.sinaimg.cn/dy/2015/1228/U3093P1DT20151228094610.jpg" width="240" height="144" />
<span class="ct_txt">古代女性为了追时尚蛮拼的</span></a></div>
				</div>
				<a href="javascript:void(0)" class="scrArrAbsLeft" id="scrArrLeft_new_read"></a>
				<a href="javascript:void(0)" class="scrArrAbsRight" id="scrArrRight_new_read"></a>
			</div>
			<div class="b_cons">
				<span class="scrDotList" id="scrDotList_new_read">
					<span></span>
				</span>
			</div>
		</div>

		<script type="text/javascript">
			jsLoader(ARTICLE_JSS.common,function(){
				var focusScroll = new ScrollPic();
				focusScroll.scrollContId  = "scrPic_new_read"; //内容容器ID

				focusScroll.dotListId   = "scrDotList_new_read";//点列表ID
				focusScroll.dotClassName  = "";//点className
				focusScroll.dotOnClassName = "on";//当前点className
				focusScroll.listType  = "";//列表类型(number:数字，其它为空)
				focusScroll.listEvent = "onmouseover"; //切换事件

				focusScroll.frameWidth  = 240;//显示框宽度
				focusScroll.pageWidth = 240; //翻页宽度
				focusScroll.upright = false; //垂直滚动
				focusScroll.speed   = 10; //移动速度(单位毫秒，越小越快)
				focusScroll.space   = 40; //每次移动像素(单位px，越大越快)
				focusScroll.autoPlay  = false; //自动播放
				focusScroll.autoPlayTime = 5; //自动播放间隔时间(秒)
				focusScroll.circularly = true;
				focusScroll.initialize(); //初始化
				document.getElementById('scrArrLeft_new_read').onmousedown = function(){
					focusScroll.pre();
					return false;
				}
				document.getElementById('scrArrRight_new_read').onmousedown = function(){
					focusScroll.next();
					return false;
				}

			});
		</script>
	</div>
	<!--XBLK_ENDX-->
</div>

<!-- part_history end -->
	
<!--品牌聚焦通栏 Start-->
<ins class="sinaads" data-ad-pdps="PDPS000000057935"></ins>
<script>(sinaads = window.sinaads || []).push({})</script>
<!--品牌聚焦通栏 End-->	
	
<div class="sp_h15"></div>

<!-- gsps时尚女性星座通栏 p_id=1&t_id=912&f_id=28333 -->
<!--t id="news_web_get_gspsdata" pid="1" tid="912" did="1" fid="sp_f28333" cname="时尚女性星座通栏"-->
	<!-- fashion start -->
<div class="newpart">
<style>
.newpart .ptn_42{width:50px;vertical-align:top;background:url(http://www.sinaimg.cn/dy/main/index13/01/tit01.png) no-repeat 0 0;}
.newpart .ptn_41{width:50px;vertical-align:top;background:url(http://www.sinaimg.cn/dy/main/index13/01/tit01.png) no-repeat -50px 0;}
.newpart .ptn_41_n{width:50px;height:20px;vertical-align:top;background:url(http://www.sinaimg.cn/dy/main/index13/01/tit01.png) no-repeat -100px 0;}
.newpart .Tit_07,.newpart .Tit_10{padding-top:10px;}

.newpart_l{float:left;display:inline;width:340px;background:#f6f6f6;height:713px;}
.newpart_m{float:left;display:inline;width:360px;margin-left:20px;height:713px;}
.newpart_r{float:right;display:inline;width:260px;background:#f6f6f6;height:713px;}

.newpart_l .ct_p_02{margin-left:0;margin-top:0;}
.newpart_l .ct_p_02 .ct_box{width:150px;padding:10px 10px 0;margin:0;}

.newpart_l02{}
.newpart_l02_cont{margin:0 10px;}
.newpart_l02 form{display:block;overflow:hidden;zoom:1;padding:17px 0 14px 0;}
.newpart_l_q{float:left;display:inline;width:244px;height:18px;border:1px solid #7e9dbb;color:#999999;padding:0;}
.newpart_l_q:focus{color:#000;}
.newpart_l_s{float:right;display:inline;width:62px;height:20px;border:1px solid #aeaeae;padding:0;}

.newpart_l_cont{float:left;display:inline;width:245px;height:218px;border:1px solid #999;}
.newpart_l_cont a{display:block;margin-bottom:5px;}
.newpart_l_cont a:link,.newpart_l_cont a:visited{color:#fff;text-decoration:none;}
.newpart_l_cont a:hover{zoom:1;text-decoration:underline;}
.newpart_l_cont img{display:block;width:245px;height:198px;}
.newpart_l_cont span{display:block;height:20px;background:#666666;text-align:center;color:#fff;}
.newpart_l_cont a:hover span{text-decoration:underline;}
.newpart_l_lab{float:right;display:inline;width:70px;}
.newpart_l_lab a{display:block;width:68px;height:68px;border:1px solid #999;margin-bottom:5px;}

.newpart_l03{}
.newpart_l03_cont{}
.newpart_l03 .list{padding:10px 0 8px 10px;}

.newpart_r01{position:relative;zoom:1;}
.newpart_r_slide{position:relative;overflow:hidden;zoom:1;width:260px;height:350px;margin-top:16px;}
.newpart_r_slide_items{float:left;display:inline;width:260px;height:350px;position:relative;}
.newpart_r_slide_items a{display:block;width:260px;height:350px;position:relative;zoom:1;}
.newpart_r_slide_items a:link,.newpart_r_slide_items a:visited{color:#fff;text-decoration:none;}
.newpart_r_slide_items a:hover{color:#fff;text-decoration:underline;}
.newpart_r_slide_items span{position:absolute;width:100%;height:20px;left:0;bottom:0;text-align:center;font:500 14px/20px 'Microsoft Yahei','微软雅黑','Simsun','宋体';background:rgba(0,0,0,0.5);filter:progid:DXImageTransform.Microsoft.gradient(GradientType=0,startColorstr='#88000000',endColorstr='#88000000')\9;}
:root .newpart_r_slide_items span{filter:none\9;}
.newpart_r01 .scrDotList{text-align:center;}

.newpart_r .blk_59 .b_pt{padding:0;}
.newpart_r .blk_59 .ct_pic{width:134px;}
.newpart_r .blk_59 .ct_txt li{width:107px;white-space:nowrap;overflow:hidden;zoom:1;}
.newpart_r .blk_59 .ct_txt li.selected{width:113px;}
.newpart_r .t_size_01 li{width:15px;padding-left:4px;}
.newpart_r .blk_77 li a{width:42px;background:url(http://www.sinaimg.cn/dy/main/index13/01/b01.png) no-repeat 0 0;}
.newpart_r .blk_77{padding-left:0;}
</style>
<div class="partTit_02" id="blk_nxtltop_01" data-sudaclick="ela2_tb">
	<div class="pT_name"><a href="http://fashion.sina.com.cn/" target="_blank" class="titName ptn_42">时尚</a><a href="http://eladies.sina.com.cn/" target="_blank" class="titName ptn_41">女性</a><a href="http://astro.sina.com.cn/" target="_blank" class="titName ptn_41_n">星座</a></div>
	<div class="pT_more"><a href="http://eladies.sina.com.cn/beauty/" target="_blank">美容</a> | <a href="http://eladies.sina.com.cn/fat/" target="_blank">减肥</a> | <a href="http://eladies.sina.com.cn/fashion/" target="_blank">服饰</a> | <a href="http://eladies.sina.com.cn/feel/" target="_blank">情感</a> | <a href="http://eladies.sina.com.cn/news/" target="_blank">八卦</a> | <a href="http://eladies.sina.com.cn/hunjia/" target="_blank">婚嫁</a> | <a href="http://blog.sina.com.cn/lm/eladies/" target="_blank">女性博客</a> | <a href="http://fashion.sina.com.cn/try/" target="_blank">免费试用</a> | <a href="http://fashion.sina.com.cn/video/" target="_blank">时尚视频</a> &nbsp;&nbsp&nbsp;&nbsp;<a href="http://eladies.sina.com.cn/" target="_blank">更多&gt;</a></div>
</div>

<div class="newpart_cont clearfix">
	<div class="newpart_l">
		<div class="newpart_l01">
			<div class="Tit_10">
				<div class="t_cont">
					<div class="t_name"><a href="http://fashion.sina.com.cn/zt/" target="_blank">时尚特辑</a></div>
					<div class="t_more"><a href="http://fashion.sina.com.cn/zt/" target="_blank">更多</a></div>
				</div>
			</div>
			<div class="ct_p_02 clearfix" data-sudaclick="ela2_sstj">
				
<div class="ct_box"><a href="http://fashion.sina.com.cn/s/in/2018-06-01/1638/doc-ihcikcew2062503.shtml" target="_blank">
<img width="150" height="90" src="http://n.sinaimg.cn/fashion/240/w150h90/20180604/elwl-hcmurvh5502151.jpg">
<span class="ct_txt">Bella撞衫苹果保鲜膜</span>
</a></div><div class="ct_box"><a href="http://fashion.sina.com.cn/style/man/2018-06-01/1537/doc-ihcikcev4793268.shtml" target="_blank">
<img width="150" height="90" src="http://n.sinaimg.cn/fashion/480/w300h180/20180604/Hw04-hcmurvh3093105.jpg">
<span class="ct_txt">30岁男人如何自救</span>
</a></div>
			</div>
		</div>
		<div class="newpart_l02">
			<div class="Tit_10">
				<div class="t_cont">
					<div class="t_name"><a href="http://fashion.sina.com.cn/cosmetics/" target="_blank">化妆品库</a></div>
					<div class="t_more"><a href="http://fashion.sina.com.cn/cosmetics/" target="_blank">更多</a></div>
				</div>
			</div>
			<div class="newpart_l02_cont"  data-sudaclick="ela2_hzpk">
				<div class="clearfix">
				<form action="http://fashion.sina.com.cn/cosmetics/c/list.php" method="get" target="_blank"><input type="text" name="k" class="newpart_l_q" value="输入化妆品名称" onfocus="if(this.value=='输入化妆品名称'){this.value='';}" onblur="if(this.value==''){this.value='输入化妆品名称';}" />			<input type="hidden" name="dpc" value="1"><input type="submit" class="newpart_l_s" value="搜索" />
				</form>

				</div>
				<div class="clearfix">
					<div class="newpart_l_cont">
		<div id="newpart_l_cont01" style=""><a href="http://slide.fashion.sina.com.cn/b/slide_24_86328_115975.html#p=1" target="_blank"><img src="http://n.sinaimg.cn/fashion/448/w229h219/20180523/8En5-hawmauc3070574.jpg" width="245px" height="198px" /><span>诗佳秀善蕙润防晒亮彩气垫粉底评测</span></a></div>	<div id="newpart_l_cont02" style="display:none;"><a href="http://fashion.sina.com.cn/b/te/2018-04-03/1025/doc-ifysvppp7838704.shtml" target="_blank"><img src="http://n.sinaimg.cn/fashion/transform/448/w229h219/20180409/Haio-fyvtmxe2844944.jpg" width="245px" height="198px" /><span>克丽缇娜月见草御颜系列评测</span></a></div>	<div id="newpart_l_cont03" style="display:none;"><a href="http://fashion.sina.com.cn/b/te/2018-03-06/0630/doc-ifxipenn2362550.shtml" target="_blank"><img src="http://n.sinaimg.cn/fashion/transform/w229h219/20180306/xuUw-fxipenn5202926.jpg" width="245px" height="198px" /><span>FOREO UFO智臻面膜仪评测</span></a></div></div>
<div class="newpart_l_lab">
		<a href="http://slide.fashion.sina.com.cn/b/slide_24_86328_115975.html#p=1" target="_blank" id="newpart_l_lab01"><img src="http://n.sinaimg.cn/fashion/448/w229h219/20180523/8En5-hawmauc3070574.jpg" width="68px" height="68px" /></a>	<a href="http://fashion.sina.com.cn/b/te/2018-04-03/1025/doc-ifysvppp7838704.shtml" target="_blank" id="newpart_l_lab02"><img src="http://n.sinaimg.cn/fashion/transform/448/w229h219/20180409/Haio-fyvtmxe2844944.jpg" width="68px" height="68px" /></a>	<a href="http://fashion.sina.com.cn/b/te/2018-03-06/0630/doc-ifxipenn2362550.shtml" target="_blank" id="newpart_l_lab03"><img src="http://n.sinaimg.cn/fashion/transform/w229h219/20180306/xuUw-fxipenn5202926.jpg" width="68px" height="68px" /></a></div>
				<script type="text/javascript">
				   jsLoader(ARTICLE_JSS.common,function(){
					  var subshow = new SubShowClass('none','onmouseover');
					  subshow.addLabel('newpart_l_lab01','newpart_l_cont01');
					  subshow.addLabel('newpart_l_lab02','newpart_l_cont02');
					  subshow.addLabel('newpart_l_lab03','newpart_l_cont03');
				  });
				</script>
			</div>
			</div>
		</div>
		<div class="newpart_l03">
			<div class="Tit_10">
				<div class="t_cont">
					<div class="t_name"><a href="http://eladies.sina.com.cn/z/" target="_blank">女性热点话题</a></div>
					<div class="t_more"><a href="http://eladies.sina.com.cn/z/" target="_blank">更多</a></div>
				</div>
			</div>
			<div class="newpart_l03_cont">
				<div class="blk_60" data-sudaclick="ela2_01">
					<div class="ct_p_02 clearfix">
	<div class="ct_box"><a href="http://eladies.sina.com.cn/feel/xinli/2018-06-04/0758/doc-ihcikcev3342653.shtml" target="_blank">
<img width="150" height="90" src="http://n.sinaimg.cn/www/transform/240/w150h90/20180604/z3hl-hcmurvh3016874.jpg"><span class="ct_txt">年轻人最好要接触的东西</span>
</a></div><div class="ct_box"><a href="http://eladies.sina.com.cn/news/star/2018-06-04/0800/doc-ihcikcew2225878.shtml" target="_blank">
<img width="150" height="90" src="http://n.sinaimg.cn/www/transform/240/w150h90/20180604/WQhJ-hcmurvh3021154.jpg"><span class="ct_txt">范冰冰《巴清传》将播出</span>
</a></div></div>
<div class="b_cont link_c666 clearfix">
	<ul class="list_12">
		<li><a href="http://eladies.sina.com.cn/feel/xinli/2018-06-04/0759/doc-ihcikcev3607883.shtml"target="_blank">越少说两个字婚姻会越好</a></li><li><a href="http://eladies.sina.com.cn/feel/xinli/2018-06-04/0759/doc-ihcikcev2655760.shtml"target="_blank">你能接受自己是替补吗？</a></li><li><a href="http://eladies.sina.com.cn/feel/xinli/2018-06-04/0759/doc-ihcikcev3608427.shtml"target="_blank">婚姻法不保护这样的女人</a></li><li><a href="http://eladies.sina.com.cn/feel/xinli/2018-06-04/0758/doc-ifxvyrit2572264.shtml"target="_blank">我饿的能吞下一头象</a></li><li><a href="http://eladies.sina.com.cn/feel/xinli/2018-06-04/0758/doc-ihcikcev2655431.shtml"target="_blank">你养的是男孩还是女孩</a></li>	</ul>
	<ul class="list">
		<li><a href="http://eladies.sina.com.cn/news/star/2018-06-04/0801/doc-ihcikcew2882890.shtml"target="_blank">张艺兴现身医院被偶遇</a></li><li><a href="http://eladies.sina.com.cn/news/star/2018-06-04/0800/doc-ihcikcew2840962.shtml"target="_blank">陈妍希高调晒娃晒老公</a></li><li><a href="http://eladies.sina.com.cn/news/bagua/2018-06-04/0800/doc-ihcikcew1303056.shtml"target="_blank">大古装回归表现受关注</a></li><li><a href="http://eladies.sina.com.cn/news/star/2018-06-03/0950/doc-ihcikcew2678262.shtml"target="_blank">孙燕姿怀二胎素颜作画</a></li><li><a href="http://eladies.sina.com.cn/news/star/2018-06-02/0830/doc-ihcikcew2275115.shtml"target="_blank">郑爽节目中失控狂发飙</a></li>	</ul>
</div>
				</div>
			</div>
		</div>
    </div>
	<div class="newpart_m"  data-sudaclick="ela2_mlist">
		
<div class="ct_t_02">
	<h1><a href="http://fashion.sina.com.cn/" target="_blank">慎点有毒 时尚圈的另类“包包种草机”</a></h1>
</div>
<div class="sp_h15"></div>
<div class="Tit_06">
	<div class="t_name"><a href="http://fashion.sina.com.cn/style/" target="_blank">时装</a><span class="dot">·</span><a href="http://fashion.sina.com.cn/beauty/" target="_blank">美容</a></div>
	<div class="t_more"><a href="http://fashion.sina.com.cn/style/" target="_blank">更多</a></div>
</div>
<ul class="list_14">
	<li><a target="_blank" href="http://fashion.sina.com.cn/style/man/2018-06-04/1846/doc-ihcmurvh6749043.shtml">蔡徐坤鞋带当腰带 机场T台怎么走得漂亮</a></li><li><a target="_blank" href="http://fashion.sina.com.cn/s/fo/2018-06-04/1753/doc-ihcmurvh6411619.shtml">上架半小时狂卖320万 侃爷《YE》周边服饰还可以直邮中国</a></li><li><a target="_blank" href="http://fashion.sina.com.cn/s/ce/2018-06-04/1905/doc-ihcmurvh6250337.shtml">机场即秀场 这些年你被谁的机场造型骗到？</a></li><li><a target="_blank" href="http://fashion.sina.com.cn/b/sk/2018-06-04/1725/doc-ihcmurvh6214582.shtml">掌握好这门美白功课 黄皮再也不用怕夏天</a></li><li><a target="_blank" href="http://fashion.sina.com.cn/s/fo/2018-06-04/1725/doc-ihcmurvh6213441.shtml">英国天然美妆品牌Lush被迫再度退出巴西市场</a></li><li><a target="_blank" href="http://fashion.sina.com.cn/s/fo/2018-06-04/1807/doc-ihcmurvh6156989.shtml">航空界的颜值担当 现实版冲上云霄了解下</a></li><li><a target="_blank" href="http://fashion.sina.com.cn/s/fo/2018-06-04/1716/doc-ihcmurvh6149052.shtml">Balenciaga推出古怪T恤衬衫 官网售价1290美元</a></li></ul>
<div class="sp_h15"></div>
<div class="Tit_06">
	<div class="t_name"><a href="http://fashion.sina.com.cn/luxury/" target="_blank">尚品</a><span class="dot">·</span><a href="http://fashion.sina.com.cn/wedding/" target="_blank">婚嫁</a></div>
	<div class="t_more"><a href="http://fashion.sina.com.cn/luxury/" target="_blank">更多</a></div>
</div>
<ul class="list_14">
	<li><a target="_blank" href="http://fashion.sina.com.cn/l/wa/to/2018-06-04/1750/doc-ihcmurvh6385786.shtml">瑞士历峰集团收购Watchfinder 首次涉足二手手表业务</a></li><li><a target="_blank" href="http://fashion.sina.com.cn/l/wa/to/2018-06-04/1713/doc-ihcmurvh6123396.shtml">你真的会使用计时码表吗？</a></li><li><a target="_blank" href="http://fashion.sina.com.cn/l/wa/buy/2018-06-04/1644/doc-ihcmurvh5908061.shtml">硬汉风不过时 最帅腕表怎能少了飞行表</a></li><li><a target="_blank" href="http://fashion.sina.com.cn/l/sn/2018-06-04/1520/doc-ihcmurvh5258937.shtml">可口可乐在澳大利亚承诺全线“降糖”</a></li><li><a target="_blank" href="http://fashion.sina.com.cn/luxury/de/2018-06-04/1431/doc-ihcmurvh4888878.shtml">谁说老房子就不酷？这些改造太让人惊喜！</a></li></ul>
<div class="ct_t_02" id="blk_nxss_021">
	<h1>
		<a href="http://eladies.sina.com.cn/" target="_blank">有哪些事“年轻人最好要接触”</a>	</h1>
</div>
<div class="ct_t_04">
	<ul class="list_14 clearfix" id="blk_nxss_031">
		    <li  class="ct_r2" ><a href="http://eladies.sina.com.cn/wzx/focus/2018-06-04/1807/doc-ihcmurvh6510304.shtml" target="_blank">微整形假药案被侦破</a></li>    <li  ><a href="http://eladies.sina.com.cn/wzx/bkzs/2018-06-04/1237/doc-ihcffhsv1934089.shtml" target="_blank">祛了眼袋会复发吗</a></li>    <li  class="ct_r2" ><a href="http://eladies.sina.com.cn/news/star/2018-06-04/1156/doc-ihcmurvh3905290.shtml" target="_blank">三浦翔承认与桐谷美玲恋情</a></li>    <li  ><a href="http://eladies.sina.com.cn/wzx/bkzs/2018-06-04/1130/doc-ihcffhsv1934235.shtml" target="_blank">挤痘痘你真的会吗</a></li>    <li  class="ct_r2" ><a href="http://eladies.sina.com.cn/news/star/2018-06-04/1118/doc-ihcmurvh3608192.shtml" target="_blank">林允揭机场时尚内幕</a></li>    <li  ><a href="http://eladies.sina.com.cn/news/star/2018-06-04/1110/doc-ihcmurvh3541671.shtml" target="_blank">李荣浩为杨丞琳庆生</a></li>    <li  class="ct_r2" ><a href="http://eladies.sina.com.cn/wzx/bkzs/2018-06-04/1015/doc-ihcffhsv1308640.shtml" target="_blank">溶脂瘦脸针的区别</a></li>    <li  ><a href="http://eladies.sina.com.cn/wzx/bkzs/2018-06-04/0931/doc-ihcffhsu4824115.shtml" target="_blank">不动骨的换头案例</a></li>    <li  class="ct_r2" ><a href="http://eladies.sina.com.cn/wzx/star/2018-06-04/0928/doc-ihcffhsu5278470.shtml" target="_blank">胡定欣的眉毛竟然这样</a></li>    <li  ><a href="http://eladies.sina.com.cn/wzx/star/2018-06-04/0844/doc-ihcffhsu5902835.shtml" target="_blank">雪莉仙女裙很能打</a></li>    <li  class="ct_r2" ><a href="http://eladies.sina.com.cn/wzx/star/2018-06-04/0816/doc-ihcaqueu9038606.shtml" target="_blank">贫乳像男人巨乳显胖</a></li>    <li  ><a href="http://eladies.sina.com.cn/wzx/bkzs/2018-06-04/0810/doc-ihcffhsv0995705.shtml" target="_blank">这几个部位凹陷显老</a></li>    <li  class="ct_r2" ><a href="http://eladies.sina.com.cn/news/star/2018-06-04/0801/doc-ihcikcew2882890.shtml" target="_blank">张艺兴低调现身医院</a></li>    <li  ><a href="http://eladies.sina.com.cn/news/star/2018-06-04/0800/doc-ihcikcew2840962.shtml" target="_blank">陈妍希高调晒老公</a></li>    <li  class="ct_r2" ><a href="http://eladies.sina.com.cn/news/star/2018-06-04/0800/doc-ihcikcew2225878.shtml" target="_blank">范冰冰《巴清传》或7月播</a></li>    <li  ><a href="http://eladies.sina.com.cn/news/bagua/2018-06-04/0800/doc-ihcikcew1303056.shtml" target="_blank">荧屏新剧相继定档</a></li>    <li  class="ct_r2" ><a href="http://eladies.sina.com.cn/feel/xinli/2018-06-04/0759/doc-ihcikcev3607883.shtml" target="_blank">婚姻怎么变的更好</a></li>    <li  ><a href="http://eladies.sina.com.cn/feel/xinli/2018-06-04/0759/doc-ihcikcev3608427.shtml" target="_blank">婚姻法不保护的女人</a></li>	</ul>
</div>
	</div>

<!--XBLK_STARTX-->

	<div class="newpart_r">
		<div class="newpart_r01">
			<div class="Tit_07">
				<div class="t_name"><a href="http://fashion.sina.com.cn/photo/" target="_blank">时尚大片</a></div>
				<div class="t_more"><a href="http://fashion.sina.com.cn/photo/" target="_blank">更多</a></div>
			</div>
			<div class="newpart_r_slide" id="newpart_r_slide" data-sudaclick="ela2_ssdp">
				
<div class="newpart_r_slide_items">
<a href="http://fashion.sina.com.cn/s/ce/2018-06-04/0747/doc-ihcikcew2241284.shtml" target="_blank">
<img src="http://n.sinaimg.cn/fashion/transform/610/w260h350/20180604/Oh6L-hcmurvh5507835.jpg" width="260px" height="350px" />
<span>时尚圈的另类“包包种草机”</span>
</a></div><div class="newpart_r_slide_items">
<a href="http://fashion.sina.com.cn/style/man/2018-06-01/1526/doc-ihcikcev7123042.shtml" target="_blank">
<img src="http://n.sinaimg.cn/fashion/610/w260h350/20180604/U-ql-hcmurvh3116771.jpg" width="260px" height="350px" />
<span>舒淇林青霞被圈粉 姜文为啥招女人喜欢</span>
</a></div><div class="newpart_r_slide_items">
<a href="http://slide.fashion.sina.com.cn/s/slide_24_84625_114404.html" target="_blank">
<img src="http://n.sinaimg.cn/eladies/b3660fdf/20180417/1.jpg" width="260px" height="350px" />
<span>胡杏儿大片硬朗柔美兼具</span>
</a></div><div class="newpart_r_slide_items">
<a href="http://fashion.sina.com.cn/d/2018-06-04/0749/doc-ihcikcev3060596.shtml" target="_blank">
<img src="http://n.sinaimg.cn/fashion/transform/610/w260h350/20180604/Y_eJ-hcmurvh3016612.jpg" width="260px" height="350px" />
<span>女星2米上镜腿都是怎么拍出来的</span>
</a></div>
			</div>
			<div class="scrDotList" id="newpart_r_slide_dots"></div><a href="javascript:;" class="scrArrAbsLeft" id="newpart_r_slide_prev"></a><a href="javascript:;" class="scrArrAbsRight" id="newpart_r_slide_next"></a>
			<script>
			jsLoader(ARTICLE_JSS.common,function(){
				var sp = new ScrollPic();
				sp.scrollContId  = "newpart_r_slide"; //内容容器ID
				sp.arrLeftId = "newpart_r_slide_prev";
				sp.arrRightId = "newpart_r_slide_next";
				sp.dotListId   = "newpart_r_slide_dots";//点列表ID
				sp.dotClassName  = "";//点className
				sp.dotOnClassName = "on";//当前点className
				sp.listType  = "";//列表类型(number:数字，其它为空)
				sp.listEvent = "onmouseover"; //切换事件
				sp.frameWidth  = 260;//显示框宽度
				sp.pageWidth = 260; //翻页宽度
				sp.upright = false; //垂直滚动
				sp.speed   = 10; //移动速度(单位毫秒，越小越快)
				sp.space   = 5; //每次移动像素(单位px，越大越快)
				sp.autoPlay  = false; //自动播放
				sp.autoPlayTime = 5; //自动播放间隔时间(秒)
				sp.circularly = true;
				sp.initialize(); //初始化
			});
			</script>
		</div>
		<div class="newpart_r02">
			<div class="Tit_07">
				<div class="t_name"><a href="http://astro.sina.com.cn/" target="_blank">星座</a></div>
				<div class="t_more"><a href="http://astro.sina.com.cn/" target="_blank">更多</a></div>
			</div>
			<div class="newpart_r02_cont">
				<div class="blk_59">
					<div class="b_pt clearfix" data-sudaclick="astro2_02">
							<div class="ct_pic" id="blk_xztp_01" ><a href="http://slide.astro.sina.com.cn/gif/slide_52_42283_63088.html"target="_blank"><img src="http://www.sinaimg.cn/dy/temp/928/2013/0624/U5246P1T928D3F23722DT20180507184825.gif" width="134" height="116" alt=""></a></div> 	<div class="ct_pic" id="blk_xztp_02"  style="display:none"><a href="http://slide.astro.sina.com.cn/gif/slide_52_42283_63127.html"target="_blank"><img src="http://www.sinaimg.cn/dy/temp/928/2013/0624/U5246P1T928D3F23723DT20180507184825.gif" width="134" height="116" alt=""></a></div> 	<div class="ct_pic" id="blk_xztp_03"  style="display:none"><a href="http://slide.astro.sina.com.cn/gif/slide_52_42283_62811.html"target="_blank"><img src="http://www.sinaimg.cn/dy/temp/928/2013/0624/U5246P1T928D3F23724DT20180507184825.gif" width="134" height="116" alt=""></a></div> 	<div class="ct_pic" id="blk_xztp_04"  style="display:none"><a href="http://slide.astro.sina.com.cn/gif/slide_52_42283_62811.html"target="_blank"><img src="http://www.sinaimg.cn/dy/temp/928/2013/0624/U5246P1T928D3F23725DT20180507184825.gif" width="134" height="116" alt=""></a></div> 	<div class="ct_pic" id="blk_xztp_05"  style="display:none"><a href="http://slide.astro.sina.com.cn/gif/slide_52_42283_61876.html"target="_blank"><img src="http://www.sinaimg.cn/dy/temp/928/2013/0624/U5246P1T928D3F24729DT20180419173325.gif" width="134" height="116" alt=""></a></div> 
<div class="ct_txt">
	<ul class="b_list">
			<li   class="selected" id="tab_xztp_01"><a href="http://slide.astro.sina.com.cn/gif/slide_52_42283_63088.html" target="_blank">12星座尴尬瞬间..</a></li>	<li  id="tab_xztp_02"><a href="http://slide.astro.sina.com.cn/gif/slide_52_42283_63127.html" target="_blank">瑟瑟发抖的12星座</a></li>	<li  id="tab_xztp_03"><a href="http://slide.astro.sina.com.cn/gif/slide_52_42283_62811.html" target="_blank">让人满脸？的星座</a></li>	<li  id="tab_xztp_04"><a href="http://slide.astro.sina.com.cn/gif/slide_52_42283_62811.html" target="_blank">12星座又在搞啥？</a></li>	<li  id="tab_xztp_05"><a href="http://slide.astro.sina.com.cn/gif/slide_52_42283_61876.html" target="_blank">12星座杠精上身啦</a></li>	</ul>
</div>
<script type="text/javascript">
	jsLoader(ARTICLE_JSS.common,function(){
		var subshow = new SubShowClass('none','onmouseover');
		subshow.addLabel('tab_xztp_01','blk_xztp_01');
		subshow.addLabel('tab_xztp_02','blk_xztp_02');
		subshow.addLabel('tab_xztp_03','blk_xztp_03');
		subshow.addLabel('tab_xztp_04','blk_xztp_04');
		subshow.addLabel('tab_xztp_05','blk_xztp_05');
	});
</script>
<div class="clearit"></div>
<div class="b_search">
	<form onsubmit="if (this.url.value) window.open(this.url.value);return false;">
		<select name="url" style="width:210px;margin-right:3px;">
			<option value="http://product.astro.sina.com.cn/?top=1072">八字测算 她是不是旺夫的女人</option>
			<option value="http://product.astro.sina.com.cn/?top=1077">结婚锦囊 你一生的姻缘走势</option>
			<option value="http://product.astro.sina.com.cn/?top=1034">占星告诉你  天生命好优势在哪儿？</option>
			<option value="http://product.astro.sina.com.cn/?top=1080">2018年 婚姻、事业运势</option>
			<option value="http://product.astro.sina.com.cn/?top=1018">转运改名  新生儿起名</option>
			<option value="http://product.astro.sina.com.cn/?top=1020">未来十年的财运走向</option>
			<option value="http://product.astro.sina.com.cn/?top=1012">定制你的专属职业发展指南</option>
			<option value="http://product.astro.sina.com.cn/?top=1031">占星：看你未来另一半的模样</option>
			<option value="http://product.astro.sina.com.cn/?top=1048">你和心爱的他是绝配吗？</option>
			<option value="http://product.astro.sina.com.cn/?top=1085" selected>2018年单身桃花哪里找</option>
		</select><input type="submit" class="btn_01" onmouseover="this.className='btn_01 btn_01_on'" onmouseout="this.className='btn_01'" value="测试" /><input type="hidden" name="from" value="channel" />
	</form>
</div>
					</div>
					<div class="line_01"></div>
					<div class="TMenu_07 t_size_01">
						<ul>
							<li id="tab_xzys_01"  class="selected"><a href="http://club.astro.sina.com.cn/forum-6-1.html" target="_blank">白羊</a></li>
							<li id="tab_xzys_02"><a href="http://club.astro.sina.com.cn/forum-7-1.html" target="_blank">金牛</a></li>
							<li id="tab_xzys_03"><a href="http://club.astro.sina.com.cn/forum-8-1.html" target="_blank">双子</a></li>
							<li id="tab_xzys_04"><a href="http://club.astro.sina.com.cn/forum-9-1.html" target="_blank">巨蟹</a></li>
							<li id="tab_xzys_05"><a href="http://club.astro.sina.com.cn/forum-10-1.html" target="_blank">狮子</a></li>
							<li id="tab_xzys_06"><a href="http://club.astro.sina.com.cn/forum-11-1.html" target="_blank">处女</a></li>
							<li id="tab_xzys_07"><a href="http://club.astro.sina.com.cn/forum-12-1.html" target="_blank">天秤</a></li>
							<li id="tab_xzys_08"><a href="http://club.astro.sina.com.cn/forum-13-1.html" target="_blank">天蝎</a></li>
							<li id="tab_xzys_09"><a href="http://club.astro.sina.com.cn/forum-14-1.html" target="_blank">射手</a></li>
							<li id="tab_xzys_10"><a href="http://club.astro.sina.com.cn/forum-15-1.html" target="_blank">魔羯</a></li>
							<li id="tab_xzys_11"><a href="http://club.astro.sina.com.cn/forum-16-1.html" target="_blank">水瓶</a></li>
							<li id="tab_xzys_12"><a href="http://club.astro.sina.com.cn/forum-17-1.html" target="_blank">双鱼</a></li>
						</ul>
					</div>
					<div id="blk_xzys_01" class="blk_77">
						<ul>
							<li><a href="http://astro.sina.com.cn/fate_day_Aries/" target="_blank">今日运</a></li>
                            <li><a href="http://astro.sina.com.cn/fate_tomorrow_Aries/" target="_blank">明日运</a></li>
                            <li><a href="http://astro.sina.com.cn/fate_week_Aries/" target="_blank">本周运</a></li>
                            <li><a href="http://astro.sina.com.cn/fate_month_Aries/" target="_blank">本月运</a></li>
                            <li><a href="http://astro.sina.com.cn/fate_year_Aries/" target="_blank">年运势</a></li>
                            <li><a href="http://astro.sina.com.cn/fate_year_love_Aries/" target="_blank">爱情运</a></li>
						</ul>
					</div>
					<div id="blk_xzys_02" class="blk_77" style="display:none">
						<ul>
							<li><a href="http://astro.sina.com.cn/fate_day_Taurus/" target="_blank">今日运</a></li>
                            <li><a href="http://astro.sina.com.cn/fate_tomorrow_Taurus/" target="_blank">明日运</a></li>
                            <li><a href="http://astro.sina.com.cn/fate_week_Taurus/" target="_blank">本周运</a></li>
                            <li><a href="http://astro.sina.com.cn/fate_month_Taurus/" target="_blank">本月运</a></li>
                            <li><a href="http://astro.sina.com.cn/fate_year_Taurus/" target="_blank">年运势</a></li>
                            <li><a href="http://astro.sina.com.cn/fate_year_love_Taurus/" target="_blank">爱情运</a></li>
						</ul>
					</div>
					<div id="blk_xzys_03" class="blk_77" style="display:none">
						<ul>
							<li><a href="http://astro.sina.com.cn/fate_day_Gemini/" target="_blank">今日运</a></li>
                            <li><a href="http://astro.sina.com.cn/fate_tomorrow_Gemini/" target="_blank">明日运</a></li>
                            <li><a href="http://astro.sina.com.cn/fate_week_Gemini/" target="_blank">本周运</a></li>
                            <li><a href="http://astro.sina.com.cn/fate_month_Gemini/" target="_blank">本月运</a></li>
                            <li><a href="http://astro.sina.com.cn/fate_year_Gemini/" target="_blank">年运势</a></li>
                            <li><a href="http://astro.sina.com.cn/fate_year_love_Gemini/" target="_blank">爱情运</a></li>
						</ul>
					</div>
					<div id="blk_xzys_04" class="blk_77" style="display:none">
						<ul>
							<li><a href="http://astro.sina.com.cn/fate_day_Cancer/" target="_blank">今日运</a></li>
                            <li><a href="http://astro.sina.com.cn/fate_tomorrow_Cancer/" target="_blank">明日运</a></li>
                            <li><a href="http://astro.sina.com.cn/fate_week_Cancer/" target="_blank">本周运</a></li>
                            <li><a href="http://astro.sina.com.cn/fate_month_Cancer/" target="_blank">本月运</a></li>
                            <li><a href="http://astro.sina.com.cn/fate_year_Cancer/" target="_blank">年运势</a></li>
                            <li><a href="http://astro.sina.com.cn/fate_year_love_Cancer/" target="_blank">爱情运</a></li>
						</ul>
					</div>
					<div id="blk_xzys_05" class="blk_77" style="display:none">
						<ul>
							<li><a href="http://astro.sina.com.cn/fate_day_leo/" target="_blank">今日运</a></li>
                            <li><a href="http://astro.sina.com.cn/fate_tomorrow_leo/" target="_blank">明日运</a></li>
                            <li><a href="http://astro.sina.com.cn/fate_week_leo/" target="_blank">本周运</a></li>
                            <li><a href="http://astro.sina.com.cn/fate_month_leo/" target="_blank">本月运</a></li>
                            <li><a href="http://astro.sina.com.cn/fate_year_leo/" target="_blank">年运势</a></li>
                            <li><a href="http://astro.sina.com.cn/fate_year_love_leo/" target="_blank">爱情运</a></li>
						</ul>
					</div>
					<div id="blk_xzys_06" class="blk_77" style="display:none">
						<ul>
							<li><a href="http://astro.sina.com.cn/fate_day_Virgo/" target="_blank">今日运</a></li>
                            <li><a href="http://astro.sina.com.cn/fate_tomorrow_Virgo/" target="_blank">明日运</a></li>
                            <li><a href="http://astro.sina.com.cn/fate_week_Virgo/" target="_blank">本周运</a></li>
                            <li><a href="http://astro.sina.com.cn/fate_month_Virgo/" target="_blank">本月运</a></li>
                            <li><a href="http://astro.sina.com.cn/fate_year_Virgo/" target="_blank">年运势</a></li>
                            <li><a href="http://astro.sina.com.cn/fate_year_love_Virgo/" target="_blank">爱情运</a></li>
						</ul>
					</div>
					<div id="blk_xzys_07" class="blk_77" style="display:none">
						<ul>
							<li><a href="http://astro.sina.com.cn/fate_day_Libra/" target="_blank">今日运</a></li>
                            <li><a href="http://astro.sina.com.cn/fate_tomorrow_Libra/" target="_blank">明日运</a></li>
                            <li><a href="http://astro.sina.com.cn/fate_week_Libra/" target="_blank">本周运</a></li>
                            <li><a href="http://astro.sina.com.cn/fate_month_Libra/" target="_blank">本月运</a></li>
                            <li><a href="http://astro.sina.com.cn/fate_year_Libra/" target="_blank">年运势</a></li>
                            <li><a href="http://astro.sina.com.cn/fate_year_love_Libra/" target="_blank">爱情运</a></li>
						</ul>
					</div>
					<div id="blk_xzys_08" class="blk_77" style="display:none">
						<ul>
							<li><a href="http://astro.sina.com.cn/fate_day_Scorpio/" target="_blank">今日运</a></li>
                            <li><a href="http://astro.sina.com.cn/fate_tomorrow_Scorpio/" target="_blank">明日运</a></li>
                            <li><a href="http://astro.sina.com.cn/fate_week_Scorpio/" target="_blank">本周运</a></li>
                            <li><a href="http://astro.sina.com.cn/fate_month_Scorpio/" target="_blank">本月运</a></li>
                            <li><a href="http://astro.sina.com.cn/fate_year_Scorpio/" target="_blank">年运势</a></li>
                            <li><a href="http://astro.sina.com.cn/fate_year_love_Scorpio/" target="_blank">爱情运</a></li>
						</ul>
					</div>
					<div id="blk_xzys_09" class="blk_77" style="display:none">
						<ul>
							<li><a href="http://astro.sina.com.cn/fate_day_Sagittarius/" target="_blank">今日运</a></li>
                            <li><a href="http://astro.sina.com.cn/fate_tomorrow_Sagittarius/" target="_blank">明日运</a></li>
                            <li><a href="http://astro.sina.com.cn/fate_week_Sagittarius/" target="_blank">本周运</a></li>
                            <li><a href="http://astro.sina.com.cn/fate_month_Sagittarius/" target="_blank">本月运</a></li>
                            <li><a href="http://astro.sina.com.cn/fate_year_Sagittarius/" target="_blank">年运势</a></li>
                            <li><a href="http://astro.sina.com.cn/fate_year_love_Sagittarius/" target="_blank">爱情运</a></li>
						</ul>
					</div>
					<div id="blk_xzys_10" class="blk_77" style="display:none">
						<ul>
							<li><a href="http://astro.sina.com.cn/fate_day_Capricorn/" target="_blank">今日运</a></li>
                            <li><a href="http://astro.sina.com.cn/fate_tomorrow_Capricorn/" target="_blank">明日运</a></li>
                            <li><a href="http://astro.sina.com.cn/fate_week_Capricorn/" target="_blank">本周运</a></li>
                            <li><a href="http://astro.sina.com.cn/fate_month_Capricorn/" target="_blank">本月运</a></li>
                            <li><a href="http://astro.sina.com.cn/fate_year_Capricorn/" target="_blank">年运势</a></li>
                            <li><a href="http://astro.sina.com.cn/fate_year_love_Capricorn/" target="_blank">爱情运</a></li>
						</ul>
					</div>
					<div id="blk_xzys_11" class="blk_77" style="display:none">
						<ul>
							<li><a href="http://astro.sina.com.cn/fate_day_Aquarius/" target="_blank">今日运</a></li>
                            <li><a href="http://astro.sina.com.cn/fate_tomorrow_Aquarius/" target="_blank">明日运</a></li>
                            <li><a href="http://astro.sina.com.cn/fate_week_Aquarius/" target="_blank">本周运</a></li>
                            <li><a href="http://astro.sina.com.cn/fate_month_Aquarius/" target="_blank">本月运</a></li>
                            <li><a href="http://astro.sina.com.cn/fate_year_Aquarius/" target="_blank">年运势</a></li>
                            <li><a href="http://astro.sina.com.cn/fate_year_love_Aquarius/" target="_blank">爱情运</a></li>
						</ul>
					</div>
					<div id="blk_xzys_12" class="blk_77" style="display:none">
						<ul>
							<li><a href="http://astro.sina.com.cn/fate_day_Pisces/" target="_blank">今日运</a></li>
                            <li><a href="http://astro.sina.com.cn/fate_tomorrow_Pisces/" target="_blank">明日运</a></li>
                            <li><a href="http://astro.sina.com.cn/fate_week_Pisces/" target="_blank">本周运</a></li>
                            <li><a href="http://astro.sina.com.cn/fate_month_Pisces/" target="_blank">本月运</a></li>
                            <li><a href="http://astro.sina.com.cn/fate_year_Pisces/" target="_blank">年运势</a></li>
                            <li><a href="http://astro.sina.com.cn/fate_year_love_Pisces/" target="_blank">爱情运</a></li>
						</ul>
					</div>
					<script type="text/javascript">
					jsLoader(ARTICLE_JSS.common,function(){
						var subshow = new SubShowClass('none','onmouseover');
						subshow.addLabel('tab_xzys_01','blk_xzys_01');
						subshow.addLabel('tab_xzys_02','blk_xzys_02');
						subshow.addLabel('tab_xzys_03','blk_xzys_03');
						subshow.addLabel('tab_xzys_04','blk_xzys_04');
						subshow.addLabel('tab_xzys_05','blk_xzys_05');
						subshow.addLabel('tab_xzys_06','blk_xzys_06');
						subshow.addLabel('tab_xzys_07','blk_xzys_07');
						subshow.addLabel('tab_xzys_08','blk_xzys_08');
						subshow.addLabel('tab_xzys_09','blk_xzys_09');
						subshow.addLabel('tab_xzys_10','blk_xzys_10');
						subshow.addLabel('tab_xzys_11','blk_xzys_11');
						subshow.addLabel('tab_xzys_12','blk_xzys_12');
					});
					</script>
				</div>
			</div>
		</div>
	</div>

<!--XBLK_ENDX-->

</div>
  <div class="p_bot"></div>

</div>
<!-- fashion end -->

<div class="sp_h20"></div>

<div class="sp_h20"></div>

	




<div class="partTit_02" id="blk_yxtltop_01" data-sudaclick="game2_tb">
  <div class="pT_name"><a href="http://games.sina.com.cn/" target="_blank" class="titName ptn_43">游戏新闻</a></div>
  <div class="pT_more">

		<a href="http://games.sina.com.cn/newgame/" target="_blank">新网游</a> | 
		<a href="http://games.sina.com.cn/hot/" target="_blank">原创报道</a> | 
		<a href="http://games.sina.com.cn/pc/" target="_blank">单机游戏</a> | 
		<a href="http://games.sina.com.cn/tv/" target="_blank">电视游戏</a> | 
		<a href="http://ka.sina.com.cn/" target="_blank">新手卡</a> | 
		<a href="http://kan.sina.com.cn/" target="_blank">看游戏</a> | 
		<a href="http://top.sina.com.cn/" target="_blank">网游排行榜</a> | 
		<a href="http://kf.games.sina.com.cn/" target="_blank">最新页游</a> | 
		<a href="http://gameapi.g.sina.com.cn/statiApi.php?action=doRedirect&label=sinaMainGameNews" target="_blank">APP</a> | 

  	&nbsp;&nbsp;&nbsp;&nbsp;<a href="http://games.sina.com.cn/" target="_blank">更多&gt;</a>
  </div>

</div>

<!-- gsps游戏通栏 p_id=1&t_id=912&f_id=28334 -->
<!--t id="news_web_get_gspsdata" pid="1" tid="912" did="1" fid="sp_f28334" cname="游戏通栏"-->
	
<!-- part_games begin -->
<div class="part_03 clearfix">
	<div class="p_left bgc_f6f6f6">
		<!-- left begin -->
		<div class="sp_h10"></div>
		<!-- 今日焦点 精美图集 -->
		<div class="Tit_11" id="blk_yxxwjrjdup_01">
			<div class="t_name"><a href="http://games.sina.com.cn/" target="_blank">今日焦点</a><span class="dot">·</span><a href="http://games.sina.com.cn/photo/" target="_blank">精美图集</a></div>
			<div class="t_more"><a href="http://games.sina.com.cn/" target="_blank">更多</a></div>
		</div>

		<div class="blk_54" id="blk_yxxwjrjd_01" data-sudaclick="game2_01">
			<div class="ct_p_02 clearfix"> 
<div class="ct_box"> <a href="http://games.sina.com.cn/o/n/2018-06-04/hcmurvh3389946.shtml" target="_blank"> <img width="150" height="90" alt="侏罗纪世界进化新视频" data-src="http://n.sinaimg.cn/games/240/w150h90/20180604/tphI-hcmurvh3690029.jpg"><span class="ct_txt">侏罗纪世界进化新视频</span></a></div>


<div class="ct_box"> <a href="http://games.sina.com.cn/o/n/2018-06-04/hcmurvh3331181.shtml" target="_blank"> <img width="150" height="90" alt="《叛变：沙漠风暴》PC版" data-src="http://n.sinaimg.cn/games/240/w150h90/20180604/P6BV-hcmurvh3695413.jpg"><span class="ct_txt">《叛变：沙漠风暴》PC版</span></a></div>



</div>

<div class="ct_p_02 clearfix"> 
<div class="ct_box">  <a href="http://games.sina.com.cn/" target="_blank"> <img width="150" height="90" alt="泄露Switch新游戏SKU" data-src="http://n.sinaimg.cn/games/240/w150h90/20180604/9mAz-hcmurvh3699863.jpg"><span class="ct_txt">泄露Switch新游戏SKU</span></a></div>

<div class="ct_box"> <a href="http://games.sina.com.cn/t/n/2018-06-04/hcmurvh3445612.shtml" target="_blank"> <img width="150" height="90" alt="超人游戏或E3亮相" data-src="http://n.sinaimg.cn/games/240/w150h90/20180604/bnq7-hcmurvh3704038.jpg"><span class="ct_txt">超人游戏或E3亮相</span></a> </div>

</div>
		</div>

		<div class="sp_h5"></div>
		<div class="Tit_11" id="blk_yxxwspup_01">
			<div class="t_name"><a href="http://games.sina.com.cn/video/" target="_blank">视频</a><span class="dot">·</span><a href="http://kan.sina.com.cn/" target="_blank">看游戏</a></div>
			<div class="t_more"><a href="http://games.sina.com.cn/video/" target="_blank">更多</a></div>
		</div>

		<div class="blk_62" id="blk_yxxwsp_01">
			<div class="ct_p_01 clearfix" id="blk_xlsp_01"  data-sudaclick="game2_02">
				<div class="ct_box"><a href="http://games.sina.com.cn/o/z/wow/2018-05-30/hcffhsv6026361.shtml" target="_blank"><img width="150" height="90" alt="28层大秘境永夜大教堂" data-src="http://n.sinaimg.cn/games/240/w150h90/20180531/NQln-hcikcev4097565.jpg"><s class="play_icon"></s><span class="ct_txt">28层大秘境永夜大教堂</span></a></div>

    <div class="ct_box"><a href="http://games.sina.com.cn/o/z/wow/2018-05-30/hcffhsv5872811.shtml" target="_blank"><img width="150" height="90" alt="29层残暴阿格洛诺克斯" data-src="http://n.sinaimg.cn/games/240/w150h90/20180531/V454-hcikcev4101705.jpg"><s class="play_icon"></s><span class="ct_txt">29层残暴阿格洛诺克斯</span></a></div>
			</div>
		</div>

		<!-- left end -->
	</div>
	<div class="p_middle">
		<!-- middle begin -->
		<div class="blk_63" id="blk_yxxw_02"  data-sudaclick="game2_list">
			<div class="blk_63" id="blk_yxxw_02"> 
	<div class="ct_t_02">
	<h1><a href="http://games.sina.com.cn/" target="_blank">4AM收获TPP冠军 携手OMG进军德国</a></h1> 
	
	</div> 
	<ul class="list_14"> 		

			


		 	  <li><a href="http://games.sina.com.cn/wjzx/g/2018-06-04/hcmurvh3280375.shtml" target="_blank">《辐射76》E3展会壁画完成样图曝光 在6月11日完工</a></li>
		
<li><a href="http://games.sina.com.cn/t/n/2018-06-04/hcmurvh3521034.shtml" target="_blank">使命召唤15在E3提供试玩</a> <a href="http://games.sina.com.cn/t/n/2018-06-04/hcmurvh3445612.shtml" target="_blank">Rocksteady超人或E3亮相</a></li>

<li><a href="http://games.sina.com.cn/t/n/2018-06-04/hcmurvh3401931.shtml" target="_blank">GOG游戏平台这夏有得玩</a> <a href="http://games.sina.com.cn/g/g/2018-06-04/hcmurvh3827086.shtml" target="_blank">《蜘蛛侠》外传回炉重制</a></li>

<li><a href="http://games.sina.com.cn/g/g/2018-06-04/hcmurvh3834458.shtml" target="_blank">新世界福音战士明日香</a> <a href="http://games.sina.com.cn/g/g/2018-06-04/hcmurvh3827106.shtml" target="_blank">神奇动物在哪里3剧本在写</a></li>


			
	
	</ul> 
	<div class="line_01"> </div> 
	<ul class="list_14"> 

												


        <li><a href="http://games.sina.com.cn/o/n/2018-06-04/hcmurvh3291516.shtml" target="_blank">索尼正开发《血源》和《地平线》新作 或在E3公布</a></li>



<li><a href="http://games.sina.com.cn/g/g/2018-06-04/hcmurvh3790698.shtml" target="_blank" >《鬼泣5》域名已经被注册</a> <a href="http://games.sina.com.cn/g/g/2018-06-04/hcmurvh3428023.shtml" target="_blank" >《银魂2》将推真人日剧</a></li>

<li><a href="http://games.sina.com.cn/g/g/2018-06-04/hcmurvh3217866.shtml" target="_blank">无敌破坏王2新海报曝光</a>  <a href="http://games.sina.com.cn/g/g/2018-06-04/hcmurvh2882748.shtml" target="_blank">国外老爹模仿《守望先锋》</a></li>
		
	
	
	</ul> 
	<div class="sp_h10"></div> 
	<div class="Tit_06"> 
	<div class="t_name"><a href="http://games.sina.com.cn/newgame/" target="_blank">网游</a><span class="dot">·</span><a href="http://www.97973.com/" target="_blank">手游资讯</a></div> 
	<div class="t_more"><a href="http://games.sina.com.cn/testlist.html" target="_blank">本周开测新游一览</a></div> 
	</div> 
	<ul class="list_14"> 
	
	    	<li><a href="http://games.sina.com.cn/o/n/2018-06-04/hcmurvh3319034.shtml" target="_blank">《圣歌》新预告被曝将在6月9日发布 宣传片超酷炫</a></li>
	

<li><a href="http://games.sina.com.cn/wm/2018-06-03/doc-ihcmurvf9800572.shtml" target="_blank" >零售商GameStop泄露新作</a> <a href="http://games.sina.com.cn/wjzx/g/2018-06-04/hcmurvh3178257.shtml" target="_blank" >宝可梦Let's GO全新系列</a></li>

<li><a href="http://games.sina.com.cn/o/n/2018-06-04/hcmurvh3418723.shtml" target="_blank">小米冲击高端的雄心失落</a>  <a href="http://games.sina.com.cn/o/n/2018-06-04/hcmurvh3398381.shtml" target="_blank">让人失望的小米8周年旗舰</a></li>


	</ul> 
	</div>
		</div>

		<!-- middle end -->
	</div>
	<!--XBLK_STARTX-->
	<div class="p_right bgc_f6f6f6">
		<!-- right begin -->
		<div class="sp_h10"></div>

		<div class="Tit_07" id="blk_yxxwxskup_01">
			<div class="t_name"><a href="http://ka.sina.com.cn/" target="_blank">新手卡</a></div>
		</div>
		<div class="blk_64 link_c666" id="blk_yxxwxsk_01"  data-sudaclick="game2_03">
			<div class="b_bd"></div>
  <table class="table" border="0" cellpadding="0" cellspacing="0">
    <tr>
      <th>游戏产品库</th>
      <th>账号说明</th>
      <th>领卡</th>
      <th>淘号</th>
    </tr>
    <tr>

	        <td><a href="http://e.wan.weibo.com/act/moyu0517" target="_blank">魔域</a></td>
      <td><a href="http://e.wan.weibo.com/act/moyu0517" target="_blank">公测礼包</a></td>
      <td><a href="http://e.wan.weibo.com/act/moyu0517" target="_blank">领卡</a></td>
      <td><a href="http://e.wan.weibo.com/act/moyu0517" target="_blank">淘</a></td>
    </tr>

    <tr class="bg">
      <td><a href="http://ka.sina.com.cn/26825" target="_blank">武林外传官方手游</a></td>
      <td><a href="http://ka.sina.com.cn/26825" target="_blank">活动礼包</a></td>
      <td><a href="http://ka.sina.com.cn/26825" target="_blank">领卡</a></td>
      <td><a href="http://ka.sina.com.cn/26825" target="_blank">淘</a></td>
    </tr>

    <tr>
      <td><a href="http://ka.sina.com.cn/26714" target="_blank">问道</a></td>
      <td><a href="http://ka.sina.com.cn/26714" target="_blank">至尊礼包</a></td>
      <td><a href="http://ka.sina.com.cn/26714" target="_blank">领卡</a></td>
      <td><a href="http://ka.sina.com.cn/26714" target="_blank">淘</a></td>
    </tr>
  </table>
		</div>

		<div class="Tit_07" id="blk_yxxwwyphbup_01">
  <div class="t_name"><a href="http://top.sina.com.cn/" target="_blank">中国网游排行榜</a></div>
</div>

<div class="blk_65" id="blk_yxxwwyphb_01"  data-sudaclick="game2_04">
  <div class="ct_pt_06 clearfix">
    <div class="ct_pic"><a href="http://e.wan.weibo.com/act/moyu0517" target="_blank"><img data-src="http://n.sinaimg.cn/games/140/w80h60/20180518/Ev7c-fzrwiaz5563250.jpg" width="80" height="60" alt="魔域"></a></div>
    <div class="ct_txt">
      <h5><a href="http://e.wan.weibo.com/act/moyu0517" target="_blank">魔域</a></h5>
      <p>魔域弓之新秀成长包<a href="http://e.wan.weibo.com/act/moyu0517" target="_blank">[详细]</a></p>
    </div>
  </div>
</div>

		<div class="Tit_07" id="blk_yxxwztup_01">
  <div class="t_name"><a href="http://games.sina.com.cn/zt/" target="_blank">专题</a><span class="dot">·</span><a href="http://tan.weibo.com/" target="_blank">热门话题</a></div>
</div>

<div class="blk_65" id="blk_yxxwzt_01"  data-sudaclick="game2_05">
  <div class="ct_pt_06 clearfix">
    <div class="ct_pic"><a href="http://www.97973.com/zt/tom.shtml" target="_blank"><img data-src="http://n.sinaimg.cn/games/140/w80h60/20180428/5yab-fzvpatq4494786.jpg" width="80" height="60" alt="《猫和老鼠》手游"></a></div>
    <div class="ct_txt">
      <h5><a href="http://www.97973.com/zt/tom.shtml" target="_blank">《猫和老鼠》手游
</a></h5>
      <p>可以玩的动画片<a href="http://www.97973.com/zt/tom.shtml" target="_blank">[详细]</a></p>
    </div>
  </div>
</div>

		<!-- right end -->
	</div>
	<!--XBLK_ENDX-->
	<div class="p_bot"></div>
</div>
<!-- part_games end -->



<!-- AD tl08 begin -->
<!--XAD_STARTX-->
<div style="margin-top:10px;text-align:center;"><!--_SINA_ADS_BEGIN_--><!--ADS:begin=PDPS000000005511:{58EEC152-0908-40AE-AA7F-5E4DB267EC22}--><!--ADS:end--><!--_SINA_ADS_END_--></div>
<!--XAD_ENDX-->
<!-- AD tl08 end -->





<!-- part_ent begin -->
<div class="partTit_01" id="blk_yltltop_01"  data-sudaclick="ent2_tb">
  <div class="pT_name"><a href="http://ent.sina.com.cn/" target="_blank" class="titName ptn_44">娱乐新闻</a></div>
  <div class="pT_more"><a href="http://ent.sina.com.cn/zt_d/2017bestperformance/" target="_blank">最美表演</a> | <a href="http://k.sina.com.cn/index_ent.html" target="_blank">娱乐看点</a> | <a href="http://ent.sina.com.cn/zongyi" target="_blank">综艺</a> | <a href="http://ent.sina.com.cn/hr" target="_blank">红人</a> | <a href="http://ent.sina.com.cn/korea/" target="_blank">韩娱</a> | <a href="http://ent.sina.com.cn/app/download/" target="_blank">娱乐APP</a> | <a href="http://ent.sina.com.cn/f/v/sinatvrt/" target="_blank">收视报告</a>       <a href="http://ent.sina.com.cn/" target="_blank">更多></a></div>
</div>

<div class="part_02 clearfix">
  <div class="p_left">
  <!-- left begin -->
<div class="Tit_08" id="blk_ylxwylztup_01">
  <div class="t_p_name"><a href="http://ent.sina.com.cn/zt/" target="_blank" class="titName ptn_45">娱乐专题</a></div>
  <div class="t_more"><a href="http://ent.sina.com.cn/zt/" target="_blank">更多</a></div>
</div>

<div class="blk_66" id="blk_ylxwylzt_01" data-sudaclick="ent2_01">
<div class="ct_p_08 clearfix">
<div class="ct_box"><a  href="http://ent.sina.com.cn/zt_d/hmwedding" target="_blank"><img  width="160" height="90" src="http://n.sinaimg.cn/ent/transform/250/w160h90/20180521/2ipG-haturft6035987.jpg" /><span class="ct_txt">哈里王子梅根大婚</span></a></div><div class="ct_box"><a  href="http://ent.sina.com.cn/zt_d/fywedding" target="_blank"><img  width="160" height="90" src="http://n.sinaimg.cn/ent/transform/250/w160h90/20180525/XsGr-haysviy5651719.jpg" /><span class="ct_txt">付辛博颖儿大婚</span></a></div></div>
  <ul class="list_12 link_c666">
<li><a target="_blank" href="http://ent.sina.com.cn/zt_d/cannes71">第71届戛纳电影节</a> <a target="_blank" href="http://ent.sina.com.cn/zt_d/hkfa37">香港电影金像奖</a> <a target="_blank" href="http://ent.sina.com.cn/zt_d/huanzhugege20">《还珠》首播20周年</a></li>  </ul>
</div>

<div class="Tit_08" id="blk_ylxwmrqtup_01">
  <div class="t_p_name"><a href="http://slide.ent.sina.com.cn/" target="_blank" class="titName ptn_46">明星美图</a></div>
  <div class="t_more"><a href="http://slide.ent.sina.com.cn/" target="_blank">更多</a></div>
</div>

<div class="blk_66" id="blk_ylxwmrqt_01" data-sudaclick="ent2_02">
<div class="ct_p_08 ct_p_08_b clearfix"><div class="ct_box"><a  href="http://slide.ent.sina.com.cn/z/v/slide_4_704_280221.html" target="_blank"><img  width="160" height="90" alt="姚晨简洁大方秀长腿" src="http://n.sinaimg.cn/ent/250/w160h90/20180601/orWj-hcikcew1607355.jpg" /><span class="ct_txt">baby黑长直配齐刘海娇小清纯</span></a></div>
     <div class="ct_box"><a  href="http://slide.ent.sina.com.cn/z/v/slide_4_704_280278.html" target="_blank"><img  width="160" height="90" alt="柳岩低胸花裙秀性感" src="http://n.sinaimg.cn/ent/transform/250/w160h90/20180601/U50B-hcikcew1611207.jpg" /><span class="ct_txt">森碟长纱裙可爱俏皮似公主 </span></a></div></div><div class="ct_p_08 ct_p_08_b clearfix"><div class="ct_box"><a  href="http://slide.ent.sina.com.cn/y/slide_4_704_280260.html" target="_blank"><img  width="160" height="90" alt="陈慧琳开唱两儿子上台俏皮" src="http://n.sinaimg.cn/ent/transform/250/w160h90/20180601/vhL7-hcikcew1617706.jpg" /><span class="ct_txt">莫文蔚气色好亮片短裙秀美腿</span></a></div>
     <div class="ct_box"><a  href="http://slide.ent.sina.com.cn/y/slide_4_704_280200.html" target="_blank"><img  width="160" height="90" alt="胡杏儿大婚穿中式礼服" src="http://n.sinaimg.cn/ent/transform/250/w160h90/20180601/TtF_-hcikcew1623589.jpg" /><span class="ct_txt">蔡依林俏皮哪吒头劲歌热舞</span></a></div></div></div>

    <div class="sp_h15"></div>
    <!-- 博客 -->
<div class="TMenu_05" id="blk_ylxwblogup_01">
  <ul>
    <li id="tab_ylxw-blog_01" class="selected"><a href="http://blog.sina.com.cn/lm/ent/" target="_blank">博客</a></li>
    <li id="tab_ylxw-blog_02"><a href="http://ent.t.sina.com.cn/" target="_blank">微博</a></li>
  </ul>
  <div class="t_more"><a href="http://ent.sina.com.cn/" target="_blank">更多</a></div>
</div>
<div class="blk_32" id="blk_ylxwblog_01">
  <ul class="list_12 link_c666" data-sudaclick="ent2_06">

		<li><a href="http://blog.sina.com.cn/s/blog_7964e4ec0102y1sl.html" target="_blank">铁链锁脚吃狗食！明星的苦难童年戳泪点</a></li>		<li><a href="http://blog.sina.com.cn/s/blog_1515cbfd80102xh2j.html" target="_blank">杨超越的霸气回应道破偶像产业核心法则</a></li>		<li><a href="http://blog.sina.com.cn/s/blog_532b88150102xjwp.html" target="_blank">宋丹丹27年旧照曝光！韩式粗眉青涩漂亮</a></li>

  </ul>
</div>

<div class="blk_32" id="blk_ylxwblog_02" style="display:none">
  <ul class="list_12 link_c666" data-sudaclick="ent2_07">
<li><a target="_blank" href="http://ent.sina.com.cn/y/yneidi/2018-06-02/doc-ihcikcew7170084.shtml">NINE PERCENT成员信息遭曝光 发声明:侵犯隐私</a></li>


<li><a href="http://ent.sina.com.cn/music/zy/2018-06-02/doc-ihcikcew6622236.shtml" target="_blank">公司老板否认炒作王菊：想炒作但是炒不了那么大</a></li>


<li><a href="http://ent.sina.com.cn/y/yneidi/2018-06-02/doc-ihcikcew6492545.shtml" target="_blank">演唱会迟到只唱六首歌?GAI方声明:普通演出非个唱</a></li>  </ul>
</div>

    <script type="text/javascript">
       jsLoader(ARTICLE_JSS.common,function(){
          var subshow = new SubShowClass('none','onmouseover');
          subshow.addLabel('tab_ylxw-blog_01','blk_ylxwblog_01');
          subshow.addLabel('tab_ylxw-blog_02','blk_ylxwblog_02');
        
      });
    </script>
  <!-- left end -->
  </div>
  <div class="p_middle" data-sudaclick="ent2_list">
  <!-- middle begin -->

<div id="blk_lyxwyw_01">
  <div class="ct_t_01">
<h1><a target="_blank" href="http://ent.sina.com.cn/m/c/2018-06-04/doc-ihcmurvh2790054.shtml">崔永元再爆电视收视率造假 刘春力挺</a></h1>

<p>[<a target="_blank" href="http://slide.ent.sina.com.cn/y/slide_4_704_280483.html">柯震东李毓芬分手半年后首同台</a> <a target="_blank" href="http://ent.sina.com.cn/tv/zy/2018-06-04/doc-ihcmurvh1430863.shtml">颖儿力挺杨超越：喜欢你的真实</a>]</p>  </div>
  <div class="line_01"></div>
</div>
<!--中部列表自动begin-->
	  <!-- 明星八卦 -->
	<div class="Tit_06" id="blk_ylxwmxbgup_01">
	  <div class="t_name"><a href="http://ent.sina.com.cn/star/" target="_blank">明星八卦</a></div>
	  <div class="t_more"><a href="http://ent.sina.com.cn/" target="_blank">更多</a></div>
	</div>
	<div class="blk_67" id="blk_ylxwmxbg_01">
	  <ul class="list_14">
	    			<li><a href="http://ent.sina.com.cn/s/j/2018-06-04/doc-ihcmurvh3365240.shtml" target="_blank" >昔日当红韩女星患精神分裂症 家中塞满4吨垃圾</a><span class="time"> 10:48</span></li>			<li><a href="http://ent.sina.com.cn/s/m/2018-06-04/doc-ihcmurvh1456588.shtml" target="_blank" >董子健为孙怡庆生晚点 网友：你看看隔壁李荣浩</a><span class="time"> 01:08</span></li>			<li><a href="http://ent.sina.com.cn/s/m/2018-06-03/doc-ihcmurvh0557781.shtml" target="_blank" >范冰冰代言企业被查封数十亿元 集团多名高管被抓</a><span class="time"> 20:37</span></li>			<li><a href="http://ent.sina.com.cn/s/m/2018-06-02/doc-ihcmurvf5619417.shtml" target="_blank" >人民网评：明星片酬为啥屡“限”屡高？</a><span class="time"> 23:29</span></li>			<li><a href="http://ent.sina.com.cn/s/m/2018-06-02/doc-ihcikcew4217977.shtml" target="_blank" >岳云鹏儿童节晒仅有童年照 今养成为孩子拍照习惯</a><span class="time"> 00:05</span></li>	  </ul>
	</div>
	<!-- 热门影视 -->
	<div class="Tit_06" id="blk_ylxwrmysup_01">
	  <div class="t_name"><a href="http://ent.sina.com.cn/film/" target="_blank">电影</a><span class="dot">·</span><a href="http://ent.sina.com.cn/tv/" target="_blank">电视</a></div>
	  <div class="t_more"><a href="http://ent.sina.com.cn/" target="_blank">更多</a></div>
	</div>
	<div class="blk_67" id="blk_ylxwrmys_01">
	  <ul class="list_14">
				<li><a href="http://ent.sina.com.cn/v/m/2018-06-04/doc-ihcmurvh3754870.shtml" target="_blank" >中国版《未生》来了！观众：不要有感情戏</a><span class="time"> 11:35</span></li>			<li><a href="http://ent.sina.com.cn/v/m/2018-06-04/doc-ihcmurvh3588782.shtml" target="_blank" >小奶狗小狼狗物化男性？刘昊然：透露出不尊重</a><span class="time"> 11:15</span></li>			<li><a href="http://ent.sina.com.cn/m/c/2018-06-04/doc-ihcmurvh3005989.shtml" target="_blank" >明星纳税背后不能说的秘密:个人工作室成避税利器</a><span class="time"> 10:02</span></li>			<li><a href="http://ent.sina.com.cn/m/c/2018-06-04/doc-ihcmurvh2992632.shtml" target="_blank" >光线不给明细出品方要走法律途径:毕竟我们出了钱</a><span class="time"> 10:00</span></li>			<li><a href="http://ent.sina.com.cn/m/c/2018-06-04/doc-ihcmurvh2981332.shtml" target="_blank" >崔永元范冰冰互撕结局难料 可一个赢家已经产生</a><span class="time"> 09:59</span></li>	  </ul>
	</div>
	<!-- 音乐 戏剧 评论 -->
	<div class="Tit_06" id="blk_ylxwyyxjplup_01">
	  <div class="t_name"><a href="http://yue.sina.com.cn/" target="_blank">音乐</a><span class="dot">·</span><a href="http://ent.sina.com.cn/xiju/" target="_blank">戏剧</a><span class="dot">·</span><a href="http://roll.ent.sina.com.cn/s/channel.php?ch=04#col=88&spec=&type=&ch=04&k=&offset_page=0&offset_num=0&num=60&asc=&page=1" target="_blank">评论</a></div>
	  <div class="t_more"><a href="http://ent.sina.com.cn/" target="_blank">更多</a></div>
	</div>
	<div class="blk_67" id="blk_ylxwyyxjpl_01">
	  <ul class="list_14">
				<li><a href="http://ent.sina.com.cn/y/youmei/2018-06-04/doc-ihcmurvh5561894.shtml" target="_blank" >水果姐公然亲昵表白精灵王子 原来是她不小心..</a><span class="time"> 15:57</span></li>			<li><a href="http://ent.sina.com.cn/y/ygangtai/2018-06-04/doc-ihcmurvh5164608.shtml" target="_blank" >范玮琪晒照大秀细长直美腿 调侃自己好像有点帅</a><span class="time"> 15:07</span></li>			<li><a href="http://ent.sina.com.cn/y/youmei/2018-06-04/doc-ihcmurvh5049954.shtml" target="_blank" >霉霉演唱会发表演讲：每个人都可以充满爱的生活</a><span class="time"> 14:53</span></li>			<li><a href="http://ent.sina.com.cn/y/youmei/2018-06-04/doc-ihcmurvh4729694.shtml" target="_blank" >盆栽哥手拿玫瑰与贝拉逛街 不惧拍照笑容灿烂</a><span class="time"> 14:09</span></li>			<li><a href="http://ent.sina.com.cn/y/youmei/2018-06-04/doc-ihcmurvh4535241.shtml" target="_blank" >侃爷新专回应奴隶制风波 患躁郁症但自认是英雄</a><span class="time"> 13:37</span></li>	  </ul>
	</div>
<!--中部列表自动end-->
	  



  <!-- middle end -->
  </div>
<!--XBLK_STARTX-->
  <div class="p_right bgc_f6f6f6">
  <!-- right begin -->
    <!-- 海外娱乐 -->

<div class="Tit_07" id="blk_ylxwhwylup_01">
  <div class="t_name"><a href="http://ent.sina.com.cn/" target="_blank">海外娱乐</a></div>
  <div class="t_more"><a href="http://ent.sina.com.cn/" target="_blank">更多</a></div>
</div>

<div class="blk_68" id="blk_ylxwhwyl_01" data-sudaclick="ent2_03">
<div class="ct_p_02 clearfix"><div class="ct_box"><a  href="http://slide.ent.sina.com.cn/star/h/slide_4_704_280267.html" target="_blank"><img  width="110" height="82" src="http://n.sinaimg.cn/ent/transform/190/w110h80/20180601/dOBd-hcikcew1628487.jpg" /><span class="ct_txt">暮光女暴露发际线</span></a></div>

    <div class="ct_box"><a  href="http://slide.ent.sina.com.cn/y/slide_4_704_280216.html" target="_blank"><img  width="110" height="82" src="http://n.sinaimg.cn/ent/transform/190/w110h80/20180601/0NzK-hcikcew1634753.jpg" /><span class="ct_txt">A妹晒与新男友合照</span></a></div>

    <div class="ct_box"><a  href="http://slide.ent.sina.com.cn/star/h/slide_4_704_280213.html" target="_blank"><img  width="110" height="82" src="http://n.sinaimg.cn/ent/transform/190/w110h80/20180601/3_T7-hcikcew1638184.jpg" /><span class="ct_txt">吉吉·哈迪德秀水蛇腰</span></a></div>

    <div class="ct_box"><a  href="http://slide.ent.sina.com.cn/y/slide_4_704_280196.html" target="_blank"><img  width="110" height="82" src="http://n.sinaimg.cn/ent/transform/190/w110h80/20180601/SwaM-hcikcew1644426.jpg" /><span class="ct_txt">艾薇儿与男友热吻</span></a></div></div></div>

<div class="Tit_07" id="blk_xlspup_01">
  <div class="t_name"><a href="http://video.sina.com.cn/ent/" target="_blank">焦点视频</a></div>
  <div class="t_more"><a href="http://video.sina.com.cn/ent/" target="_blank">更多</a></div>
</div>

<div class="blk_69" id="blk_xlsp_01">
  <div class="ct_p_06 clearfix" data-sudaclick="ent2_04">

<div class="ct_box"><a  href="http://video.sina.com.cn/p/ent/doc/2018-06-01/110968674155.html" target="_blank"><img  width="110" height="82" alt="林志玲自嘲无人追" src="http://n.sinaimg.cn/ent/transform/280/w160h120/20180601/Pkaf-hcikcew0398196.jpg" /><span class="ct_txt">郑爽儿童节送祝福</span></a></div>

<div class="ct_box"><a  href="http://video.sina.com.cn/p/ent/doc/2018-06-01/104368673823.html" target="_blank"><img  width="110" height="82" alt="奶茶妹妹已顺利生产" src="http://n.sinaimg.cn/ent/transform/280/w160h120/20180601/ycsI-hcikcew0408010.jpg" /><span class="ct_txt">小S谢娜同框牵手</span></a></div>

<div class="ct_box"><a  href="http://video.sina.com.cn/p/ent/doc/2018-06-01/103468673677.html" target="_blank"><img  width="110" height="82" alt="杨谨华含泪宣布分手" src="http://n.sinaimg.cn/ent/transform/280/w160h120/20180601/wdgj-hcikcew0421854.jpg" /><span class="ct_txt">秋瓷炫平安产子</span></a></div>

<div class="ct_box"><a  href="http://video.sina.com.cn/p/ent/doc/2018-06-01/115168674743.html" target="_blank"><img  width="110" height="82" alt="曹格老婆遭泄隐私" src="http://n.sinaimg.cn/ent/transform/280/w160h120/20180601/AEKg-hcikcew0666708.jpg" /><span class="ct_txt">陈妍希美照曝光</span></a></div>
  </div>
</div>


<!--t id="news_web_get_gspsdata" pid="1" tid="843" did="1" fid="sp_f20588" cname="娱乐通栏_乐库"-->
<div class="Tit_07" id="blk_xlspykup_01"><div class="t_name"><a href="http://ent.sina.com.cn/ku/" target="_blank">娱乐资料库</a></div>
  <div class="t_more"><a href="http://ent.sina.com.cn/ku/" target="_blank">更多</a></div>
</div>

<div class="blk_69" id="blk_xlspyk_01"><ul class="list_12 link_c666" data-sudaclick="ent2_05"><li><a href="http://ent.sina.com.cn/ku/movie_info_index.d.html?type=movie&id=fysvmcn4493890" target="_blank">哆啦A梦：大雄的金银岛</a> <a href="http://ent.sina.com.cn/ku/movie_info_index.d.html?type=movie&id=fysuuya6134966" target="_blank">超时空同居</a></li>

    <li><a href="http://ent.sina.com.cn/ku/movie_info_index.d.html?type=movie&id=fyhmpew3485917" target="_blank">复仇者联盟3：无限战争</a> <a href="http://ent.sina.com.cn/ku/movie_info_index.d.html?type=movie&id=fyrmfmc2093494" target="_blank">潜艇总动员</a></li>

    <li><a href="http://ent.sina.com.cn/ku/movie_info_index.d.html?type=movie&id=fypvuqf2525354" target="_blank">厕所英雄</a> <a href="http://ent.sina.com.cn/ku/movie_info_index.d.html?type=movie&id=fynhhay8231966" target="_blank">深海越狱</a> <a target="_blank" href="http://ent.sina.com.cn/ku/movie_info_index.d.html?type=movie&id=fyhmpew3484982">幸福马上来</a></li></ul>
</div>
  <!-- right end -->
  </div>
<!--XBLK_ENDX-->
</div>
<!-- part_ent end -->






<!-- part_society begin -->
<div class="partTit_01" id="blk_shtltop_01" data-sudaclick="sh2_tb">
<!-- publish_helper name='news_38_社会二类_栏目条' p_id='1' t_id='908' d_id='38' -->
  <div class="pT_name"><a href="http://news.sina.com.cn/society/" target="_blank" class="titName ptn_47">社会新闻</a></div>
  <div class="pT_more"><a href="http://news.sina.com.cn/zt/col_society/" target="_blank">新闻专题</a> | <a href="http://slide.news.sina.com.cn/s/" target="_blank">新闻图片</a> &nbsp;&nbsp&nbsp;&nbsp;<a href="http://news.sina.com.cn/society/" target="_blank">更多&gt;</a></div>
</div>

<div class="part_04 clearfix">
  <div class="p_left">
  <!-- left begin -->
    <div class="sp_h5"></div>
    <!-- 趣图 -->
<div class="Tit_08 t_mr0" id="blk_shxwqtup_01">
  <div class="t_name"><a href="http://slide.news.sina.com.cn/s/" target="_blank">图片</a></div>
  <div class="t_more"><a href="http://slide.news.sina.com.cn/s/" target="_blank">更多</a></div>
</div>
<div class="blk_70" id="blk_shxwqt_01">
  <div class="b_cont">
    <div class="ct_p_05 clearfix" id="scrPic_shxw_01"  data-sudaclick="sh2_pic">
		<!--t id="news_web_get_gspsdata" pid="1" tid="908" did="39" fid="sp_f23233" cname="社会二类滚动图"-->
				<div class="ct_pic"><a href="//slide.news.sina.com.cn/s/slide_1_2841_258627.html" target="_blank"><img src="//k.sinaimg.cn/n/news/transform/200/w600h400/20180418/XqRH-fytnfyp7049866.jpg/w340h190f4f.jpg" width="340" height="190" alt=""><span class="ct_txt">女老师为高三学生跪着讲课</span></a></div>
		<div class="ct_pic"><a href="//slide.news.sina.com.cn/s/slide_1_2841_258617.html" target="_blank"><img src="//k.sinaimg.cn/n/news/transform/200/w600h400/20180418/BWZQ-fytnfyp7008255.jpg/w340h190205.jpg" width="340" height="190" alt=""><span class="ct_txt">重庆现“桥洞茶馆” 临江纳凉宛如“神仙居”</span></a></div>
		<div class="ct_pic"><a href="//slide.news.sina.com.cn/s/slide_1_2841_258442.html" target="_blank"><img src="//k.sinaimg.cn/n/news/transform/200/w600h400/20180417/MhDh-fytnfyp6627626.jpg/w340h190395.jpg" width="340" height="190" alt=""><span class="ct_txt">尽孝谋生两不误 成都一货郎驮着92岁老母讨生活</span></a></div>
		<div class="ct_pic"><a href="//slide.news.sina.com.cn/s/slide_1_2841_258392.html" target="_blank"><img src="//k.sinaimg.cn/n/news/1_img/vcg/c4b46437/190/w1024h766/20180417/K413-fzihnen8460592.jpg/w340h19036b.jpg" width="340" height="190" alt=""><span class="ct_txt">西安：轿车停在铁道旁 火车被逼停堵了半个多小时</span></a></div>
		<div class="ct_pic"><a href="//slide.news.sina.com.cn/s/slide_1_2841_258381.html" target="_blank"><img src="//k.sinaimg.cn/n/news/1_img/upload/c4b46437/748/w930h618/20180417/6WRo-fzihnen8132742.jpg/w340h1900b7.jpg" width="340" height="190" alt=""><span class="ct_txt">江西老人上交寿棺 500口寿棺回炉焚烧发电</span></a></div>	</div>
    <a href="javascript:void(0)" class="scrArrAbsLeft" id="scrArrLeft_shxw_01"></a>
    <a href="javascript:void(0)" class="scrArrAbsRight" id="scrArrRight_shxw_01"></a>
  </div>
  <div class="b_cons">
    <span class="scrDotList" id="scrDotList_shxw_01">
      <span></span>
    </span>
  </div>
</div>

<script type="text/javascript">
   jsLoader(ARTICLE_JSS.common,function(){
      var focusScroll = new ScrollPic();
      focusScroll.scrollContId  = "scrPic_shxw_01"; //内容容器ID

      focusScroll.dotListId   = "scrDotList_shxw_01";//点列表ID
      focusScroll.dotClassName  = "";//点className
      focusScroll.dotOnClassName = "on";//当前点className
      focusScroll.listType  = "";//列表类型(number:数字，其它为空)
      focusScroll.listEvent = "onmouseover"; //切换事件

      focusScroll.frameWidth  = 340;//显示框宽度
      focusScroll.pageWidth = 340; //翻页宽度
      focusScroll.upright = false; //垂直滚动
      focusScroll.speed   = 10; //移动速度(单位毫秒，越小越快)
      focusScroll.space   = 40; //每次移动像素(单位px，越大越快)
      focusScroll.autoPlay  = false; //自动播放
      focusScroll.autoPlayTime = 5; //自动播放间隔时间(秒)
      focusScroll.circularly = true;
      focusScroll.initialize(); //初始化
      document.getElementById('scrArrLeft_shxw_01').onmousedown = function(){
        focusScroll.pre();
        return false;
      }
      document.getElementById('scrArrRight_shxw_01').onmousedown = function(){
        focusScroll.next();
        return false;
      }

  });
</script>

<div id="tianyi_society">
    <div class="Tit_08 t_mr0" id="blk_shxwspup_01">
      <div class="t_name"><a href="http://news.video.sina.com.cn" target="_blank">视频</a></div>
      <div class="t_more"><a href="http://news.video.sina.com.cn" target="_blank">更多</a></div>
    </div>

    <div class="blk_02" id="blk_shxwsp_01">
		<style type="text/css">
			#blk_shxwsp_01 .ct_p_01 .ct_box a{
				display: block;
				width: 160px;
				height: 112px;
				background-color: #000;
				overflow: hidden;
			}
		</style>
        <div class="ct_p_01 clearfix" id="blk_xlsp_01" data-sudaclick="sh2_video">
            
        </div>

        <ul class="list_12 link_c666" id="blk_sxad_2">
            
        </ul>
    </div>
    <script type="text/javascript" src="//simg.sinajs.cn/products/news/items/2017/tianyi/js/tianyiData-1.js?ver=1.0"></script>
    <script type="text/javascript">
      jsLoader(ARTICLE_JSS.jq,function(){
          (function($){
              $(function(){

                  getTianYiData(societyObj);
              })
          })(jQuery)
      })

    </script>
</div>


  <!-- left end -->
  </div>
  <div class="p_middle">
  <!-- middle begin -->
<div class="blk_71" id="blk_shxwlist_01"  data-sudaclick="sh2_list">
<!--t id="news_web_get_gspsdata" pid="1" tid="908" did="41" fid="sp_f23233" cname="社会二类中部列表" -->
		<ul class="list_14">
				<li><a href="http://news.sina.com.cn/s/2018-06-04/doc-ihcmurvh7872613.shtml" target="_blank" >巨额片酬逃哪去了？明星原来有这么多种避税方法</a><span class="time"> 21:47</span></li>			<li><a href="http://news.sina.com.cn/o/2018-06-04/doc-ihcmurvh7929494.shtml" target="_blank" >小威宣布退出法网 她和莎娃的宿命对决又要延后了</a><span class="time"> 21:42</span></li>			<li><a href="http://news.sina.com.cn/s/2018-06-04/doc-ihcmurvh7825946.shtml" target="_blank" >长安剑：莫焕晶死刑 法律当给善良以力量</a><span class="time"> 21:38</span></li>			<li><a href="http://news.sina.com.cn/o/2018-06-04/doc-ihcmurvh7812070.shtml" target="_blank" >范冰冰资本征途：5家公司法人 7家公司股东等等</a><span class="time"> 21:34</span></li>			<li><a href="http://news.sina.com.cn/o/2018-06-04/doc-ihcmurvh7595437.shtml" target="_blank" >范冰冰参股唐德影视发声:不存在签阴阳合同偷漏税</a><span class="time"> 20:59</span></li>			<li><a href="http://news.sina.com.cn/o/2018-06-04/doc-ihcmurvh7544643.shtml" target="_blank" >云南勐海“找到200多块陨石” 现场售价1克超两千</a><span class="time"> 20:56</span></li>
	</ul><div class="line_01"></div>	<ul class="list_14">
				<li><a href="http://news.sina.com.cn/o/2018-06-04/doc-ihcmurvh7471251.shtml" target="_blank" >明星阴阳合同逃税?亿万收入适用税率或比普通人低</a><span class="time"> 20:43</span></li>			<li><a href="http://news.sina.com.cn/o/2018-06-04/doc-ihcmurvh7470444.shtml" target="_blank" >这两座六线城市 为何让范冰冰们趋之若鹜？</a><span class="time"> 20:42</span></li>			<li><a href="http://news.sina.com.cn/s/2018-06-04/doc-ihcmurvh7853498.shtml" target="_blank" >熟客冒充交警可帮销违章 敲诈网咖老板万元还网贷</a><span class="time"> 20:40</span></li>			<li><a href="http://news.sina.com.cn/s/2018-06-04/doc-ihcmurvh7359101.shtml" target="_blank" >男子陷传销向父亲要钱被拒跳楼 民警拽住悬半空</a><span class="time"> 20:12</span></li>			<li><a href="http://news.sina.com.cn/s/2018-06-04/doc-ihcmurvh7295099.shtml" target="_blank" >5网民编造传播恐怖分子到青岛安放炸弹 警方刑拘</a><span class="time"> 20:11</span></li>			<li><a href="http://news.sina.com.cn/o/2018-06-04/doc-ihcmurvh7163337.shtml" target="_blank" >自称美到窒息实际像菜地 安徽一薰衣草庄园被立案</a><span class="time"> 19:55</span></li>
	</ul><div class="line_01"></div>	<ul class="list_14">
				<li><a href="http://news.sina.com.cn/s/2018-06-04/doc-ihcmurvh7148181.shtml" target="_blank" >饭店老板养2只绿海龟被拘 警方:国家二级保护动物</a><span class="time"> 19:41</span></li>			<li><a href="http://news.sina.com.cn/o/2018-06-04/doc-ihcmurvh7153705.shtml" target="_blank" >推特执行最严年龄禁令：创建账户必须年满13岁</a><span class="time"> 19:36</span></li>			<li><a href="http://news.sina.com.cn/o/2018-06-04/doc-ihcmurvh7153723.shtml" target="_blank" >农具修理店老板造枪网上售卖被抓:每支几千至几万</a><span class="time"> 19:32</span></li>			<li><a href="http://news.sina.com.cn/s/2018-06-04/doc-ihcmurvh7305976.shtml" target="_blank" >民宅设淫窝60块嫖一次 2失足女确认感染艾滋病毒</a><span class="time"> 19:31</span></li>			<li><a href="http://news.sina.com.cn/o/2018-06-04/doc-ihcmurvh6814610.shtml" target="_blank" >外卖小哥凌晨被困电梯却遭客户调侃:那就睡里边吧</a><span class="time"> 18:53</span></li>			<li><a href="http://news.sina.com.cn/o/2018-06-04/doc-ihcmurvh6829213.shtml" target="_blank" >“中华香烟”做啤酒？工商:初步判断涉不正当竞争</a><span class="time"> 18:43</span></li>
	</ul></div>

  <!-- middle end -->
  </div>
<!--XBLK_STARTX-->
	<div class="p_right bgc_f6f6f6">
  <!-- right begin -->
    <!-- 心情排行榜 -->
    <div class="sp_h5"></div>
<div class="Tit_07" id="blk_shxwxqphbth_01">
  <div class="t_name"><a href="http://news.sina.com.cn/society/moodrank/" target="_blank">心情排行榜</a></div>
</div>
<div class="TMenu_07x t_size_03" id="blk_shxwxqphbup_01">
  <ul>
    <li id="tab_shxw-xqphb_01" class="">感动</li>
    <li id="tab_shxw-xqphb_02" class="">震惊</li>
    <li id="tab_shxw-xqphb_03" class="">新奇</li>
    <li id="tab_shxw-xqphb_04" class="">愤怒</li>
    <li id="tab_shxw-xqphb_05" class="">搞笑</li>
    <li id="tab_shxw-xqphb_06" class="selected">难过</li>
  </ul>
</div>
<!-- 1 -->
<div class="blk_72" id="blk_shxwxqphb_01" style="display: none;">
  <ol class="topList_12 link_c666" id="blk_shxwxqphb_011" data-sudaclick="sh2_hot01">

  <li><a target="_blank" href="http://news.sina.com.cn/o/2017-01-06/doc-ifxzkfuh5593296.shtml">鸿雁离别与伴侣对望亲吻 主人被感动决定</a></li>

  <li><a target="_blank" href="http://news.sina.com.cn/s/wh/2017-01-06/doc-ifxzkfuk2419157.shtml">家中起火丈夫不愿独自逃命 为救瘫痪妻双</a></li>

  <li><a target="_blank" href="http://news.sina.com.cn/o/2017-01-06/doc-ifxzkfvn0502967.shtml">救护车内用餐遭检举 消防员：已经饿得受</a></li>

  <li><a target="_blank" href="http://news.sina.com.cn/s/pa/2016-08-25/doc-ifxvixeq0424901.shtml">医生受贿546万：我不收钱就便宜了药贩子</a></li>

  <li><a target="_blank" href="http://news.sina.com.cn/c/2016-08-24/doc-ifxvixsh6539912.shtml">老虎咬死女游客涉事公园明日恢复开园</a></li>

  <li><a target="_blank" href="http://news.sina.com.cn/s/wh/2017-01-06/doc-ifxzkssy1008701.shtml">网传雾霾吸入身体永远排不出去 协和专家</a></li>

  <li><a target="_blank" href="http://news.sina.com.cn/s/wh/2017-01-06/doc-ifxzkfuh5728142.shtml">刑警追捕嫌犯掉下高桥 醒来给妻子发信：</a></li>

  <li><a target="_blank" href="http://news.sina.com.cn/s/pa/2016-08-24/doc-ifxvixeq0401461.shtml">数人为劫夺被押亲戚 高速上将警方车辆撞</a></li>

  </ol>


</div>
<!-- 2 -->
<div class="blk_72" id="blk_shxwxqphb_02">
  <ol class="topList_12 link_c666" id="blk_shxwxqphb_012" data-sudaclick="sh2_hot02">

  <li><a target="_blank" href="http://news.sina.com.cn/s/wh/2017-01-06/doc-ifxzkfuh5655520.shtml">公司买8吨重大鲸鱼喂狗 宰杀现场血腥(图</a></li>

  <li><a target="_blank" href="http://news.sina.com.cn/s/wh/2017-01-06/doc-ifxzkfuk2399518.shtml">老人取款时拉住银行保安：我被威胁了 快</a></li>

  <li><a target="_blank" href="http://news.sina.com.cn/o/2017-01-06/doc-ifxzkfuk2465268.shtml">女研究生反驳男学霸观点遭尾随暴打 校方</a></li>

  <li><a target="_blank" href="http://news.sina.com.cn/s/wh/2017-01-06/doc-ifxzkssy1008701.shtml">网传雾霾吸入身体永远排不出去 协和专家</a></li>

  <li><a target="_blank" href="http://news.sina.com.cn/s/wh/2017-01-06/doc-ifxzkfuk2445347.shtml">老夫妻晚餐遭投毒阴阳相隔 幕后黑手是亲</a></li>

  <li><a target="_blank" href="http://news.sina.com.cn/s/wh/2016-08-25/doc-ifxvixeq0408347.shtml">女生被骗学费离世 父亲:她倒三轮车里身</a></li>

  <li><a target="_blank" href="http://news.sina.com.cn/o/2016-08-25/doc-ifxvixsh6559906.shtml">村支书伪造材料骗518万拆迁款 为儿子买</a></li>

  <li><a target="_blank" href="http://news.sina.com.cn/s/wh/2017-01-06/doc-ifxzkfuh5678402.shtml">小伙给外公守灵只顾玩手机 遭表哥拳打脚</a></li>

  </ol>


</div>
<!-- 3 -->
<div class="blk_72" id="blk_shxwxqphb_03">
  <ol class="topList_12 link_c666" id="blk_shxwxqphb_013" data-sudaclick="sh2_hot03">

  <li><a target="_blank" href="http://news.sina.com.cn/s/pa/2016-08-25/doc-ifxvixeq0438143.shtml">老汉撞死人将三轮车拆零藏匿被6岁孙女拆</a></li>

  <li><a target="_blank" href="http://news.sina.com.cn/s/pa/2016-08-24/doc-ifxvixeq0401461.shtml">数人为劫夺被押亲戚 高速上将警方车辆撞</a></li>

  <li><a target="_blank" href="http://news.sina.com.cn/s/wh/2016-08-25/doc-ifxvixeq0413891.shtml">男子伤人致死潜逃9年 酒后吐真言被女友</a></li>

  <li><a target="_blank" href="http://news.sina.com.cn/o/2017-01-06/doc-ifxzkfuh5593296.shtml">鸿雁离别与伴侣对望亲吻 主人被感动决定</a></li>

  <li><a target="_blank" href="http://news.sina.com.cn/s/wh/2017-01-06/doc-ifxzkfuk2399518.shtml">老人取款时拉住银行保安：我被威胁了 快</a></li>

  <li><a target="_blank" href="http://news.sina.com.cn/s/pa/2016-08-25/doc-ifxvixeq0424901.shtml">医生受贿546万：我不收钱就便宜了药贩子</a></li>

  <li><a target="_blank" href="http://news.sina.com.cn/o/2016-08-25/doc-ifxvitex8871639.shtml">女大学生接航班取消短信 6100元学费被转</a></li>

  <li><a target="_blank" href="http://news.sina.com.cn/s/wh/2016-08-25/doc-ifxvixeq0411471.shtml">路人吐槽“最窄人行道”:比平衡木都难走</a></li>

  </ol>


</div>
<!-- 4 -->
<div class="blk_72" id="blk_shxwxqphb_04">
  <ol class="topList_12 link_c666" id="blk_shxwxqphb_014" data-sudaclick="sh2_hot04">

  <li><a target="_blank" href="http://news.sina.com.cn/s/wh/2017-01-06/doc-ifxzkssy1008701.shtml">网传雾霾吸入身体永远排不出去 协和专家</a></li>

  <li><a target="_blank" href="http://news.sina.com.cn/o/2016-08-25/doc-ifxvixsh6559906.shtml">村支书伪造材料骗518万拆迁款 为儿子买</a></li>

  <li><a target="_blank" href="http://news.sina.com.cn/s/wh/2017-01-06/doc-ifxzkfuk2445347.shtml">老夫妻晚餐遭投毒阴阳相隔 幕后黑手是亲</a></li>

  <li><a target="_blank" href="http://news.sina.com.cn/s/wh/2016-08-25/doc-ifxvixeq0428551.shtml">兰州交通大学博文学院被曝曾开除多名患</a></li>

  <li><a target="_blank" href="http://news.sina.com.cn/o/2017-01-06/doc-ifxzkfvn0502967.shtml">救护车内用餐遭检举 消防员：已经饿得受</a></li>

  <li><a target="_blank" href="http://news.sina.com.cn/s/wh/2017-01-06/doc-ifxzkfuh5599864.shtml">男子筹款13万救儿被证明有3套房 称想留</a></li>

  <li><a target="_blank" href="http://news.sina.com.cn/s/wh/2017-01-06/doc-ifxzkfuh5678402.shtml">小伙给外公守灵只顾玩手机 遭表哥拳打脚</a></li>

  <li><a target="_blank" href="http://news.sina.com.cn/o/2017-01-06/doc-ifxzkfuh5585423.shtml">母亲1句话致女儿离家近3年:就知道窝家里</a></li>

  </ol>


</div>
<!-- 5 -->
<div class="blk_72" id="blk_shxwxqphb_05">
  <ol class="topList_12 link_c666" id="blk_shxwxqphb_015" data-sudaclick="sh2_hot05">

  <li><a target="_blank" href="http://news.sina.com.cn/s/wh/2017-01-06/doc-ifxzkfuk2399518.shtml">老人取款时拉住银行保安：我被威胁了 快</a></li>

  <li><a target="_blank" href="http://news.sina.com.cn/s/wh/2017-01-06/doc-ifxzkfuh5678402.shtml">小伙给外公守灵只顾玩手机 遭表哥拳打脚</a></li><li><a target="_blank" href="http://news.sina.com.cn/s/wh/2017-01-06/doc-ifxzkssy1008701.shtml">网传雾霾吸入身体永远排不出去 协和专家</a></li>

  <li><a target="_blank" href="http://news.sina.com.cn/s/wh/2016-08-25/doc-ifxvixeq0439030.shtml">女孩花7000元定制“挽回前男友” 对方却</a></li>

  <li><a target="_blank" href="http://news.sina.com.cn/s/pa/2016-08-25/doc-ifxvixeq0438143.shtml">老汉撞死人将三轮车拆零藏匿被6岁孙女拆</a></li>

  <li><a target="_blank" href="http://news.sina.com.cn/o/2016-08-25/doc-ifxvitex8871639.shtml">女大学生接航班取消短信 6100元学费被转</a></li><li><a target="_blank" href="http://news.sina.com.cn/o/2016-08-25/doc-ifxvitex8871228.shtml">男子4200元买气枪打鸟 鸟没打着人被拘</a></li>

  <li><a target="_blank" href="http://news.sina.com.cn/s/wh/2016-08-25/doc-ifxvixsh6576792.shtml">大学校园流浪狗被人用箭射穿肚子(图)</a></li>

  </ol>


</div>
<!-- 6 -->
<div class="blk_72" id="blk_shxwxqphb_06">
  <ol class="topList_12 link_c666" id="blk_shxwxqphb_016" data-sudaclick="sh2_hot06">

  <li><a target="_blank" href="http://news.sina.com.cn/o/2017-01-06/doc-ifxzkfuh5585423.shtml">母亲1句话致女儿离家近3年:就知道窝家里</a></li>

  <li><a target="_blank" href="http://news.sina.com.cn/o/2017-01-06/doc-ifxzkfvn0502967.shtml">救护车内用餐遭检举 消防员：已经饿得受</a></li>

  <li><a target="_blank" href="http://news.sina.com.cn/s/wh/2017-01-06/doc-ifxzkssy1008701.shtml">网传雾霾吸入身体永远排不出去 协和专家</a></li>

  <li><a target="_blank" href="http://news.sina.com.cn/o/2016-08-25/doc-ifxvixsh6555460.shtml">步行街塌陷夫妻俩落坑 女方已怀孕7个月</a></li>

  <li><a target="_blank" href="http://news.sina.com.cn/s/pa/2016-08-25/doc-ifxvixeq0438143.shtml">老汉撞死人将三轮车拆零藏匿被6岁孙女拆</a></li>

  <li><a target="_blank" href="http://news.sina.com.cn/s/wh/2016-08-25/doc-ifxvixeq0413891.shtml">男子伤人致死潜逃9年 酒后吐真言被女友</a></li>

  <li><a target="_blank" href="http://news.sina.com.cn/o/2016-08-24/doc-ifxvitex8833084.shtml">孕妇保胎被注射过期盐水 1月后双胞胎胎</a></li>

  <li><a target="_blank" href="http://news.sina.com.cn/s/wh/2017-01-06/doc-ifxzkfuk2419157.shtml">家中起火丈夫不愿独自逃命 为救瘫痪妻双</a></li>

  </ol>


</div>


<script type="text/javascript">
   jsLoader(ARTICLE_JSS.common,function(){
      var subshow = new SubShowClass('none','onmouseover');
      subshow.addLabel('tab_shxw-xqphb_01', 'blk_shxwxqphb_01', '', '');
      subshow.addLabel('tab_shxw-xqphb_02', 'blk_shxwxqphb_02', '', '');
      subshow.addLabel('tab_shxw-xqphb_03', 'blk_shxwxqphb_03', '', '');
      subshow.addLabel('tab_shxw-xqphb_04', 'blk_shxwxqphb_04', '', '');
      subshow.addLabel('tab_shxw-xqphb_05', 'blk_shxwxqphb_05', '', '');
      subshow.addLabel('tab_shxw-xqphb_06', 'blk_shxwxqphb_06', '', '');
      subshow.random(1,1,1,1,1,1);

  });
</script>

<div class="Tit_07" id="blk_wrxwhgup_01">
  <div class="t_name"><a href="http://news.sina.com.cn/society/" target="_blank">往日新闻回顾</a></div>
</div>

    <div class="blk_73" id="blk_wrxwhg_01">
      <ul class="list_12 link_c666" id="blk_wrxwhg_011" data-sudaclick="sh2_01">


<!-- blk_sxad_3 勿删 begin -->


<li><a href="http://news.sina.com.cn/s/wh/2017-01-06/doc-ifxzkssy1008701.shtml" target="_blank">网传雾霾吸入身体永远排不出去 协和专家辟谣</a></li>

<li><a href="http://news.sina.com.cn/s/wh/2017-01-06/doc-ifxzkssy0985886.shtml" target="_blank">江西村民哄抢出土铜钱 官方：都要给国家 </a></li>

<li><a href="http://news.sina.com.cn/o/2017-01-06/doc-ifxzkfuk2465268.shtml" target="_blank">女研究生反驳男学霸观点遭尾随暴打 校方回应</a></li>

<li><a href="http://news.sina.com.cn/s/wh/2017-01-06/doc-ifxzkfuh5678809.shtml" target="_blank">地税局副局长被查 托人铲事被骗710万</a></li>

<li><a href="http://news.sina.com.cn/s/wh/2017-01-06/doc-ifxzkfuh5678402.shtml" target="_blank">小伙给外公守灵只顾玩手机 遭表哥拳打脚踢</a></li>

<li><a href="http://news.sina.com.cn/s/wh/2017-01-06/doc-ifxzkfuh5655520.shtml" target="_blank">公司买8吨重大鲸鱼喂狗 宰杀现场血腥(图)</a></li>

<li><a href="http://news.sina.com.cn/s/wh/2017-01-06/doc-ifxzkfuh5641270.shtml" target="_blank">小伙瀑布前浪漫求婚 幸福拥吻后戒指不慎落水</a></li>

<li><a href="http://news.sina.com.cn/s/wh/2017-01-06/doc-ifxzkfuk2419157.shtml" target="_blank">家中起火丈夫不愿独自逃命 为救瘫痪妻双双离世</a></li>



		  
<!-- blk_sxad_3 勿删 end -->

      </ul>
    </div>

  <!-- right end -->
  </div><!--XBLK_ENDX-->
</div>
<!-- part_society end -->




	
<script>
    (function (d, s, id) {
        var n = d.getElementsByTagName(s)[0];
        if (d.getElementById(id)) return;
        s = d.createElement(s);
        s.id = id;
        s.setAttribute('charset', 'utf-8');
        s.src = '//d' + Math.floor(0 + Math.random() * (9 - 0 + 1)) + '.sina.com.cn/litong/zhitou/sinaads/test/e-recommendation/release/sinaere.js';
        n.parentNode.insertBefore(s, n);
    })(document, 'script', 'sinaere-script');
</script>
<!-- 底部推荐 begin -->
<div style="margin-top:15px;">
  <ins class="sinaere" data-tpl="3" data-pos="P_N_H_3" data-w="1000" data-h="100" data-num="3" data-channel="news"></ins>
  <script>
      //推荐启动代码
      (sinaere = window.sinaere || []).push({});
  </script>
</div>
<!-- 底部推荐 end -->

	

<!-- 合作媒体 begin -->
<div class="blk_74" id="blk_hzmt_01">
  <h4><span class="titName ptn_48">合作媒体</span></h4>
  <div class="b_cont"  data-sudaclick="blk_hzmt">
<p><a href="http://www.gov.cn/" target="_blank">中国政府网</a> | <a href="http://www.china.com.cn" target="_blank">中国网</a> | <a href="http://www.people.com.cn/" target="_blank">人民网</a> | <a href="http://www.xinhuanet.com/" target="_blank">新华网</a> | <a href="http://www.chinanews.com/" target="_blank">中新网</a> | <a href="http://www.cctv.com/default.shtml" target="_blank">央视网</a> | <a href="http://www.cnr.cn/" target="_blank">中广网</a> |  <a href="http://www.chinadaily.com.cn/" target="_blank">中国日报</a> | <a href="http://www.cyol.net/node/index.htm" target="_blank">中青在线</a> | <a href="http://www.gmw.cn/" target="_blank">光明网</a> | <a href="http://www.chinamil.com.cn/" target="_blank">解放军报</a> | <a href="http://www.legaldaily.com.cn/" target="_blank">法制日报</a> | <a href="http://www.taiwan.cn/" target="_blank">中国台湾网</a> | <a href="http://www.ce.cn/" target="_blank">中经网</a> | <a href="http://www.nfcmag.com/" target="_blank">南风窗</a></p>
  <p><a href="http://www.chinaweekly.cn/" target="_blank">中国周刊</a> | <a href="http://www.lifeweek.com.cn/" target="_blank">三联生活周刊</a> | <a href="http://www.ynet.com/" target="_blank">北青网</a> | <a href="http://www.dayoo.com/" target="_blank">大洋网</a> | <a href="http://www.nanfangdaily.com.cn" target="_blank">南方报业</a> | <a href="http://www.ycwb.com/" target="_blank">金羊网</a> | <a href="http://www.southcn.com/" target="_blank">南方网</a> | <a href="http://www.eastday.com" target="_blank">东方网</a> | <a href="http://www.21dnn.com/" target="_blank">千龙网</a> | <a href="http://www.thebeijingnews.com/" target="_blank">新京报</a> | <a href="http://epaper.jinghua.cn/" target="_blank">京华时报</a>| <a href="http://www.rednet.com.cn/" target="_blank">红网</a> | <a href="http://workercn.cn/" target="_blank">工人日报</a> | <a href="http://www.inewsweek.cn/" target="_blank">中国新闻周刊</a> | <a href="http://www.cankaoxiaoxi.com/" target="_blank">参考消息</a></p>
  <p><a href="http://www.neweekly.com.cn" target="_blank">新周刊</a> | <a href="http://www.dahe.cn/" target="_blank">大河网</a> | <a href="http://www.chinapeace.org.cn/" target="_blank">中国长安网</a> | <a href="http://www.huanqiu.com/" target="_blank">环球网</a> | <a href="http://www.newssc.org" target="_blank">四川新闻网</a> | <a href="http://www.morningpost.com.cn/" target="_blank">北晨网</a> | <a href="http://www.zjol.com.cn/" target="_blank">浙江在线</a> | <a href="http://gb.cri.cn/" target="_blank">国际在线</a> | <a href="http://www.e23.cn/" target="_blank">舜网</a> | <a href="http://www.xkb.com.cn./index.php" target="_blank">新快网</a> | <a href="http://www.jxcn.cn/" target="_blank">中国江西网</a> | <a href="http://www.yunnan.cn" target="_blank">云南网</a> | <a href="http://www.szed.com/" target="_blank">深圳新闻网</a> | <a href="http://www.anhuinews.com/" target="_blank">中安在线</a> | <a href="http://www.xwh.cn/" target="_blank">新文化网</a></p>
  <p><a href="http://www.ts.cn/" target="_blank">天山网</a> | <a href="http://www.iyaxin.com/" target="_blank">亚心网</a> | <a href="http://www.dzwww.com/" target="_blank">大众网</a> | <a href="http://www.jxnews.com.cn/" target="_blank">大江网</a> | <a href="http://www.hsw.cn/" target="_blank">华商网</a> | <a href="http://www.chinaxiaokang.com/" target="_blank">中国小康网</a> | <a href="http://www.jxcbw.cn/" target="_blank">江西晨报网</a> | <a href="http://xmzk.xinminweekly.com.cn/" target="_blank">新民周刊</a> | <a href="http://www.fjsen.com/" target="_blank">东南网</a> | <a href="http://www.sdnews.com.cn/" target="_blank">山东新闻网</a> | <a href="http://www.xinjiangnet.com.cn/" target="_blank">新疆网</a> | <a href="http://www.cqnews.net/" target="_blank">华龙网</a> | <a href="http://news.cnhubei.com/" target="_blank">荆楚网</a> | <a href="http://www.ahwang.cn/" target="_blank">安徽网</a> | <a href="http://news.sina.com.cn/media.html" target="_blank">媒体大全</a></p>
  </div>
</div>
<!-- 合作媒体 end -->


<div style="margin-top:10px;text-align:center;"><!--_SINA_ADS_BEGIN_--><!--ADS:begin=PDPS000000016991:{96F4570B-DC25-4B55-9DA0-D643F7CE19C7}-->
<!--ADS:end--><!--_SINA_ADS_END_--></div>

<!-- footer begin -->
<div class="footer" id="blk_footer_01">
  <p>24小时客户服务热线：4006900000 010-82623378 <a target="_blank" href="http://tech.sina.com.cn/focus/sinahelp.shtml">常见问题解答</a> <a target="_blank" href="http://www.12377.cn/">互联网违法和不良信息举报</a></p>
  <p>违法和不良信息举报电话：010-62675637 举报邮箱：<a href="mailto:jubao@vip.sina.com">jubao@vip.sina.com</a></p>
  <p><a target="_blank" href="http://news.sina.com.cn/feedback/post.html">新闻中心意见反馈留言板</a></p>
  <p><a href="http://corp.sina.com.cn/chn/">新浪简介</a> | <a href="http://corp.sina.com.cn/eng/">About Sina</a> | <a href="http://emarketing.sina.com.cn/">广告服务</a> | <a href="http://www.sina.com.cn/contactus.html">联系我们</a> | <a href="http://corp.sina.com.cn/chn/sina_job.html">招聘信息</a> | <a href="http://www.sina.com.cn/intro/lawfirm.shtml">网站律师</a> | <a href="http://english.sina.com">SINA English</a> | <a href="https://login.sina.com.cn/signup/signup.php">通行证注册</a> | <a href="http://help.sina.com.cn/">产品答疑</a></p>
  <p>Copyright &copy; 1996-2018 SINA Corporation, All Rights Reserved</p>
  <p>新浪公司 <a href="http://www.sina.com.cn/intro/copyright.shtml">版权所有</a></p>
</div>

<!-- footer end -->

</div>


<script>
//右侧锚点导航
jsLoader(ARTICLE_JSS.jq, function() {
	var $ = window.jQuery;
	var maxSize = 1230;
	var doc = document,
	side = (function() {
		var body = doc.body,
		firstChild = body.firstChild,
		wrap = doc.createElement('div');
		wrap.className = 'nav_fix';
		wrap.style.display = 'none';
		wrap.innerHTML = ['<span class="nav_fixlst">',
			'      <a href="javascript:void(0);" to="#new_pics">图片</a>',
			'      <a href="javascript:void(0);" to="#blk_shup_01">万象</a>',
			'      <a href="javascript:void(0);" to="#blk_gjxwup_01">国际</a>',
			'  </span>'].join('');
		firstChild ? firstChild.parentNode.insertBefore(wrap, firstChild) : body.appendChild(wrap);
		return wrap;
	})(),
	clz = side.className,
	lnks = side.getElementsByTagName('a'),
	toggle = function(dis) {
		side.style.display = dis;
	}, 
	resize = function() {
		var body = doc.documentElement || doc.body;
		if (!body) {
			return;
		}
		var width = body.offsetWidth;
		if (width < maxSize) {
			toggle('none');
		} else {
			toggle('block')
		}
	};
	toggle('block');
	resize();
	$(window).on('resize', resize);
	$(side).on('click', '.nav_fixlst a', function(evt){
		var target = $(evt.target);
		var scrollToEl = $(target.attr('to'));	
		$(window).scrollTop(scrollToEl.offset().top);
	})

});
</script>

<script type="text/javascript" src="//i1.sinaimg.cn/unipro/pub/suda_m_v629.js"></script>
<script type="text/javascript">suds_init(90,100.00,1015,2);</script>

	
<script type="text/javascript" src="//sjs.sinajs.cn/products/news/public/log/js/suda_log_1459340870608.js"></script>
 <script type="text/javascript">__suda_log_init(91,100,1015,2);</script>
	
<script>
var isIE6 = navigator.appVersion.indexOf("MSIE 6") != -1 ? true: false;
//图片滚动加载
~function() {var d = document, w = this, b = document.body, h = document.documentElement, p = [], eventFunc = function() {scrollLoader.scroll() }, bH = -1, timer, bT, bVH, iTotal = d.images.length; var sina = {$: function(objName) {if (d.getElementById) {return d.getElementById(objName) } else {return d.all[objName] } }, addEvent: function(obj, eventType, func) {if (obj.attachEvent) {obj.attachEvent("on" + eventType, func) } else {obj.addEventListener(eventType, func, false) } }, delEvent: function(obj, eventType, func) {if (obj.detachEvent) {obj.detachEvent("on" + eventType, func) } else {obj.removeEventListener(eventType, func, false) } }, absPosition: function(obj, parentObj) {var left = obj.offsetLeft; var top = obj.offsetTop; var tempObj = obj.offsetParent; try {while (tempObj != b && tempObj != d.documentElement && tempObj != parentObj && tempObj != null) {left += tempObj.offsetLeft; top += tempObj.offsetTop; tempObj = tempObj.offsetParent } } catch (e) {}; return {left: left, top: top } } }; var scrollLoader = {version: '1.1.0', status: "complete", mult: 2, init: function(ele) {var that = this, imgs, num = 0; if (ele && ele.getElementsByTagName) {imgs = ele.getElementsByTagName('img') } else {imgs = d.images }; for (var i = 0; i < imgs.length; i++) {if (imgs[i].getAttribute("data-src") && !imgs[i].__isSL) {if (imgs[i].offsetWidth == 0 && imgs[i].offsetHeight == 0) {imgs[i].__pObj = imgs[i].parentNode; while (imgs[i].__pObj.offsetWidth == 0 && imgs[i].__pObj.offsetHeight == 0) {imgs[i].__pObj = imgs[i].__pObj.parentNode } }; imgs[i].__isSL = true; p.push(imgs[i]); num++ } }; if (num > 0) {if (this.status != 'scrolling') {sina.addEvent(w, "scroll", eventFunc); this.status = "scrolling"; timer = setInterval(function() {that.timer() }, 200) }; this.scroll() } }, timer: function() {if (iTotal !== d.images.length) {iTotal = d.images.length; this.init() }; var vh = Math.min(h.clientHeight, b.clientHeight); var vt = (w.pageYOffset || b.scrollTop || h.scrollTop) - Math.round(vh * (this.mult - 1) / 2); var vb = vt + Math.round(vh * ((this.mult - 1) / 2 + 1)); if (bT !== vt || vb !== bVH) {this.scroll() } }, showImg: function(img) {if (img.getAttribute("data-src")) { img.removeAttribute("data-top"); img.__pObj = null; img.__isSL = null;img.src = img.getAttribute("data-src"); if(isIE6){return false;} } }, scroll: function() {if (this.status != "scrolling") {return }; var cache = 0; if (bH == d.body.scrollHeight) {cache = 1 } else {bH = d.body.scrollHeight }; var vh = Math.min(h.clientHeight, b.clientHeight); var vt = (w.pageYOffset || b.scrollTop || h.scrollTop) - Math.round(vh * (this.mult - 1) / 2); var vb = vt + Math.round(vh * ((this.mult - 1) / 2 + 1)); bT = vt; bVH = vb; var s = 0, posTop, obj; for (var i = 0; i < p.length; i++) {if (!p[i].getAttribute("data-src")) {continue }; s++; if (!cache) {if (p[i].offsetWidth == 0 && p[i].offsetHeight == 0) {p[i].__pObj = p[i].parentNode; if (!p[i].__pObj) {this.showImg(p[i]); continue }; while ( !! p[i].__pObj && p[i].__pObj.offsetWidth == 0 && p[i].__pObj.offsetHeight == 0) {p[i].__pObj = p[i].__pObj.parentNode } }; obj = p[i].__pObj || p[i]; posTop = sina.absPosition(obj, b).top; p[i].setAttribute("data-top", posTop) } else {posTop = p[i].getAttribute("data-top") } if (posTop >= vt && posTop <= vb) {this.showImg(p[i]) } }; if (s == 0) {this.status = "complete"; sina.delEvent(w, "scroll", eventFunc); clearInterval(timer) } } }; this.scrollLoader = scrollLoader }(); scrollLoader.init();

</script>

<!--XAD_STARTX-->
<!--_SINA_ADS_BEGIN_-->
<!-- gsps body广告 -->
<!--XAD_STARTX-->
<!--_SINA_ADS_BEGIN_-->
<!-- 控制脚本顶 请勿修改或移动 -->
<script language="javascript" type="text/javascript">function ADFunc(sFuncName){this.sFuncName = sFuncName;};function ADFuncSeq(){this.aryFunc = new Array();this.push = function(sFuncName){try{this.aryFunc.push(new ADFunc(sFuncName));}catch(e){}};this.shift = function(){try{return this.aryFunc.shift();}catch(e){}};};var arryADSeq = new ADFuncSeq();function nextAD(){var oFunAD = arryADSeq.shift();if (oFunAD != null){try{eval(oFunAD.sFuncName);}catch(e){}}};</script>
<!-- 控制脚本顶 请勿修改或移动-->

<!--加载全屏 begin-->
<!--新闻首页动态全屏开始-->
<!--新闻首页动态全屏结束-->
<script async charset="utf-8" src="http://d9.sina.com.cn/litong/zhitou/sinaads/release/sinaads.js"></script><ins class="sinaads" data-ad-pdps="PDPS000000047195" data-ad-type="fullscreen"></ins><script>(sinaads = window.sinaads || []).push({});</script>
<!--加载全屏 end-->

<!--加载流媒体 begin-->
<ins class="sinaads" data-ad-pdps="PDPS000000059668" data-ad-type="stream"></ins><script>(sinaads = window.sinaads || []).push({});</script>
<!--加载流媒体 end-->

<!--加载跨栏 begin-->
<span id="CoupletMediaWrap"></span>
<script async charset="utf-8" src="http://d7.sina.com.cn/litong/zhitou/sinaads/release/sinaads.js"></script><ins class="sinaads" data-ad-pdps="PDPS000000047198" data-ad-type="couplet"></ins><script>(sinaads = window.sinaads || []).push({params:{sinaads_couple_top:46}});</script>
<!--加载跨栏 end-->

<!--新闻中心调研开始-->

<!--新闻中心调研结束-->

<!--新闻中心前弹出窗口开始-->

<!--新闻中心前弹出窗口结束-->

<!--新闻中心二轮播背投广告开始-->

<!--新闻中心二轮播背投广告结束-->

<!--icast,请勿调整放置顺序-->

<!--icast开始-->
<!-- 视窗和浮层 300*250 请求两个 渲染一个 by jiliang1 2017-09-19 start-->
<span id="videoWindowWrap"></span>
<ins class="sinaads" data-ad-pdps="PDPS000000056023,PDPS000000057465" data-pop-position = "right bottom"></ins>
<script>
(sinaads = window.sinaads || []).push({
    params:{
        sinaads_ad_delay: 5,
        sinaads_pop_position:"right bottom",
    }
});
</script>
<!-- 视窗和浮层 300*250 请求两个 渲染一个 end -->

<!-- 控制脚本尾 请勿修改或移动 -->
<script type="text/javascript" charset="gb2312" src="http://d1.sina.com.cn/rwei/news2013/newsbottom.js"></script>
<script language="javascript" type="text/javascript">try{nextAD();}catch(e){}</script>
<!-- 控制脚本尾 请勿修改或移动-->


<!--_SINA_ADS_END_-->
<!--XAD_ENDX-->
<!--_SINA_ADS_END_-->
<!--XAD_ENDX-->

<script type="text/javascript" src="//news.sina.com.cn/js/iframe/ad/directAd_gn.js" charset="gbk"></script> 

<script type="text/javascript" src="//d2.sina.com.cn/d1images/sinaads_entry/sinaads_entry_news.js" charset="gbk"></script>

<!-- 二维码 begin -->
	<style type="text/css">
	.side-btns-2w {width:110px;top: 200px;_top:expression(documentElement.scrollTop + 200);left: 50%;margin: 0 0 0 505px;position: fixed;_position:absolute;z-index: 0;overflow: hidden; font: 12px/22px Arial;color:#333;}

	.side-btns-2w a{color:#333;}
	.side-btns-2w em,.side-btns-2w span{font-style: normal;font-weight: normal;line-height: 27px;}
	.side-btns-2w-img{ display:block;width:110px;background: #EBEBEB;line-height: 0;text-align: center;position: relative;zoom:1;}
	.side-btns-2w-img:link,.side-btns-2w-img:visited{color:#333;text-decoration: none;}
	.side-btns-2w-img:hover,.side-btns-2w-img:active{color:#333;text-decoration: none;background: #ebebeb;}
	.side-btns-2w img{border: 0;display: block; margin:0 auto;padding: 0;}
	.side-btns-2w-close{width:40px;height: 18px;line-height: 80px;margin:0 0 0 70px;display:block;overflow: hidden;background: url(http://i0.sinaimg.cn/dy/deco/2013/0912/close.png) no-repeat;}
	.side-btns-2w-resize{display: none !important;}
	</style>

	<script type="text/javascript">
	(function(aClz,maxSize,co) {
	var doc = document,
		side = (function() {
			var body = doc.body,
				firstChild = body.firstChild,
				wrap = doc.createElement('div');
			wrap.className = 'side-btns-2w';
			wrap.style.display = 'none';
			wrap.innerHTML = '<a href="javascript:void(0)" class="side-btns-2w-img" title="新浪新闻公众号" suda-uatrack="key=qr_code&value=news_index_qrcode" style="cursor:default;"><em>新浪新闻公众号</em> <img src="http://i0.sinaimg.cn/dy/main/other/qrcode_indexright_90.jpg" width="90"> <span style="cursor:default;">扫描二维码关注</span> </a> <a href="javascript:;" class="side-btns-2w-close" title="关闭" suda-uatrack="key=qr_code&value=news_index_qrcode_close" >关闭</a>';
			firstChild ? firstChild.parentNode.insertBefore(wrap, firstChild) : body.appendChild(wrap);
			return wrap;
		})(),
		clz = side.className,
		nClz = clz + ' ' + aClz,
		cookieName = co.name || 'TDCDIS',
		domain = co.domain || 'news.sina.com.cn',
		lnks = side.getElementsByTagName('a'),
		close = lnks[lnks.length-1],
		toggle = function(dis) {
			side.style.display = dis;
		}, addEvent = function(o, s, fn) {
			if (o.attachEvent) {
				o.attachEvent('on' + s, fn);
			} else {
				o.addEventListener(s, fn, false);
			}
			return o;
		}, resize = function() {
			var body = doc.documentElement || doc.body;
			if (!body) {
				return;
			}
			var width = body.offsetWidth;
			if (width < maxSize) {
				side.className = nClz;
			} else {
				side.className = clz;
			}
		};
		// name, value, expire(hour), path, domain, secure
		var cookie = (function() {var co = {}; co.getCookie = function(name) {name = name.replace(/([\.\[\]\$])/g, '\\\$1'); var rep = new RegExp(name + '=([^;]*)?;', 'i'); var co = document.cookie + ';'; var res = co.match(rep); if (res) {return unescape(res[1]) || ""; } else {return ""; } }; co.setCookie = function(name, value, expire, path, domain, secure) {var cstr = []; cstr.push(name + '=' + escape(value)); if (expire) {var dd = new Date(); var expires = dd.getTime() + expire * 3600000; dd.setTime(expires); cstr.push('expires=' + dd.toGMTString()); } if (path) {cstr.push('path=' + path); } if (domain) {cstr.push('domain=' + domain); } if (secure) {cstr.push(secure); } document.cookie = cstr.join(';'); }; co.deleteCookie = function(name) {document.cookie = name + '=;' + 'expires=Fri, 31 Dec 1999 23:59:59 GMT;'; }; return co; })();
		var display = cookie.getCookie(cookieName);
		if(display!=''){
			toggle('none');
			return;
		}
		toggle('block');
		resize();
		addEvent(window, 'resize', resize);
		addEvent(close,'click',function(e){
			toggle('none');
			cookie.setCookie(cookieName,'1',15*24,'/',domain);
			if(window.event){
				window.event.returnValue = false;
			}else{
				e.preventDefault();
			}
		});

	})('side-btns-2w-resize',1230,{
		name:'TDCDIS',				//cookie名
		domain:'news.sina.com.cn'		//domain 根据频道不同
	});
	</script>
<!-- 二维码 end -->

<!-- 随屏 新闻中心首页两轮播随屏对联 -->
<ins class="sinaads" data-ad-pdps="PDPS000000054492"></ins>
<script>
    (sinaads = window.sinaads || []).push({
        params : {
            sinaads_float_show_pos: 800,  //随屏对联
            sinaads_float_top : 46
        }
    });
</script>

<!--随行按钮 leitao End-->
<ins class="sinaads" data-ad-pdps="PDPS000000057533" data-followbutton-position = "left bottom"></ins>
<script>(sinaads = window.sinaads || []).push({
    params:{
        sinaads_followbutton_show_pos:1700,
        sinaads_followbutton_position:"left bottom"
    }
})
</script>
<!--随行按钮 leitao End-->

<!--车展早晚报 start-->
		<!--车展早晚报 end-->

<!-- body code begin -->
<script type="text/javascript">
(function(){
    if(window.top !== window.self || window._thereIsNoRealTimeMessage){return};
    var script = document.createElement('script');
    script.setAttribute('charset', 'gb2312');
    script.src = '//news.sina.com.cn/js/694/2012/0830/realtime.js?ver=1.5.1';
    document.getElementsByTagName('head')[0].appendChild(script);
})();
</script>

<!-- SSO_UPDATECOOKIE_START -->
<script type="text/javascript">var sinaSSOManager=sinaSSOManager||{};sinaSSOManager.q=function(b){if(typeof b!="object"){return""}var a=new Array();for(key in b){a.push(key+"="+encodeURIComponent(b[key]))}return a.join("&")};sinaSSOManager.es=function(f,d,e){var c=document.getElementsByTagName("head")[0];var a=document.getElementById(f);if(a){c.removeChild(a)}var b=document.createElement("script");if(e){b.charset=e}else{b.charset="gb2312"}b.id=f;b.type="text/javascript";d+=(/\?/.test(d)?"&":"?")+"_="+(new Date()).getTime();b.src=d;c.appendChild(b)};sinaSSOManager.doCrossDomainCallBack=function(a){sinaSSOManager.crossDomainCounter++;document.getElementsByTagName("head")[0].removeChild(document.getElementById(a.scriptId))};sinaSSOManager.crossDomainCallBack=function(a){if(!a||a.retcode!=0){return false}var d=a.arrURL;var b,f;var e={callback:"sinaSSOManager.doCrossDomainCallBack"};sinaSSOManager.crossDomainCounter=0;if(d.length==0){return true}for(var c=0;c<d.length;c++){b=d[c];f="ssoscript"+c;e.scriptId=f;b=b+(/\?/.test(b)?"&":"?")+sinaSSOManager.q(e);sinaSSOManager.es(f,b)}};sinaSSOManager.updateCookieCallBack=function(c){var d="ssoCrossDomainScriptId";var a="http://login.sina.com.cn/sso/crossdomain.php";if(c.retcode==0){var e={scriptId:d,callback:"sinaSSOManager.crossDomainCallBack",action:"login",domain:"sina.com.cn"};var b=a+"?"+sinaSSOManager.q(e);sinaSSOManager.es(d,b)}else{}};sinaSSOManager.updateCookie=function(){var g=1800;var p=7200;var b="ssoLoginScript";var h=3600*24;var i="sina.com.cn";var m=1800;var l="http://login.sina.com.cn/sso/updatetgt.php";var n=null;var f=function(e){var r=null;var q=null;switch(e){case"sina.com.cn":q=sinaSSOManager.getSinaCookie();if(q){r=q.et}break;case"sina.cn":q=sinaSSOManager.getSinaCookie();if(q){r=q.et}break;case"51uc.com":q=sinaSSOManager.getSinaCookie();if(q){r=q.et}break}return r};var j=function(){try{return f(i)}catch(e){return null}};try{if(g>5){if(n!=null){clearTimeout(n)}n=setTimeout("sinaSSOManager.updateCookie()",g*1000)}var d=j();var c=(new Date()).getTime()/1000;var o={};if(d==null){o={retcode:6102}}else{if(d<c){o={retcode:6203}}else{if(d-h+m>c){o={retcode:6110}}else{if(d-c>p){o={retcode:6111}}}}}if(o.retcode!==undefined){return false}var a=l+"?callback=sinaSSOManager.updateCookieCallBack";sinaSSOManager.es(b,a)}catch(k){}return true};sinaSSOManager.updateCookie();</script>
<!-- SSO_UPDATECOOKIE_END -->

<!-- start dmp -->
<script type="text/javascript">
(function(d, s, id) {
var n = d.getElementsByTagName(s)[0];
if (d.getElementById(id)) return;
s = d.createElement(s);
s.id = id;
s.setAttribute('charset', 'utf-8');
s.src = '//d' + Math.floor(0 + Math.random() * (8 - 0 + 1)) + '.sina.com.cn/litong/zhitou/sinaads/src/spec/sinaads_ck.js';
n.parentNode.insertBefore(s, n);
})(document, 'script', 'sinaads-ck-script');
</script>
<!-- end dmp -->

<!-- body code end -->
</body>
</html>
        
        '''
        # htmltext=etree.HTML(mainPage.text)
        htmltext = etree.HTML(contexthtml)


        #要闻
        news1=htmltext.xpath('//*[@id="syncad_1"]/*/a')
        for c in news1:
            print c.xpath('./@href')[0],c.text


        news2=htmltext.xpath('//*[@id="ad_entry_b2"]/ul/li/a')
        for c in news2:
            print c.xpath('./@href')[0],c.text

        news3 = htmltext.xpath('// *[ @ id = "blk_sh_011"]/li/a')
        for c in news3:
            print c.xpath('./@href')[0], c.text

        news4 = htmltext.xpath('// *[ @ id = "blk_ndxw_01"] / ul/li/a')
        for c in news4:
            print c.xpath('./@href')[0], c.text




        return 0

if __name__ == '__main__':
    sinaInstance=sina()
    print sinaInstance.getNews()