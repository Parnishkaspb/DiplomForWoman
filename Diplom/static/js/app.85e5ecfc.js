(self.webpackChunk=self.webpackChunk||[]).push([[143],{4692:(t,e,n)=>{var r={"./charts_controller.js":9568};function o(t){var e=i(t);return n(e)}function i(t){if(!n.o(r,t)){var e=new Error("Cannot find module '"+t+"'");throw e.code="MODULE_NOT_FOUND",e}return r[t]}o.keys=function(){return Object.keys(r)},o.resolve=i,t.exports=o,o.id=4692},8205:(t,e,n)=>{"use strict";n.d(e,{Z:()=>r});const r={"symfony--ux-chartjs--chart":Promise.resolve().then(n.bind(n,5806))}},9568:(t,e,n)=>{"use strict";n.r(e),n.d(e,{default:()=>l});n(8304),n(4812),n(489),n(1539),n(2419),n(8011),n(9070),n(2526),n(1817),n(2165),n(6992),n(8783),n(3948);function r(t){return r="function"==typeof Symbol&&"symbol"==typeof Symbol.iterator?function(t){return typeof t}:function(t){return t&&"function"==typeof Symbol&&t.constructor===Symbol&&t!==Symbol.prototype?"symbol":typeof t},r(t)}function o(t,e){if(!(t instanceof e))throw new TypeError("Cannot call a class as a function")}function i(t,e){for(var n=0;n<e.length;n++){var r=e[n];r.enumerable=r.enumerable||!1,r.configurable=!0,"value"in r&&(r.writable=!0),Object.defineProperty(t,r.key,r)}}function c(t,e){return c=Object.setPrototypeOf?Object.setPrototypeOf.bind():function(t,e){return t.__proto__=e,t},c(t,e)}function u(t){var e=function(){if("undefined"==typeof Reflect||!Reflect.construct)return!1;if(Reflect.construct.sham)return!1;if("function"==typeof Proxy)return!0;try{return Boolean.prototype.valueOf.call(Reflect.construct(Boolean,[],(function(){}))),!0}catch(t){return!1}}();return function(){var n,r=f(t);if(e){var o=f(this).constructor;n=Reflect.construct(r,arguments,o)}else n=r.apply(this,arguments);return a(this,n)}}function a(t,e){if(e&&("object"===r(e)||"function"==typeof e))return e;if(void 0!==e)throw new TypeError("Derived constructors may only return object or undefined");return function(t){if(void 0===t)throw new ReferenceError("this hasn't been initialised - super() hasn't been called");return t}(t)}function f(t){return f=Object.setPrototypeOf?Object.getPrototypeOf.bind():function(t){return t.__proto__||Object.getPrototypeOf(t)},f(t)}var l=function(t){!function(t,e){if("function"!=typeof e&&null!==e)throw new TypeError("Super expression must either be null or a function");t.prototype=Object.create(e&&e.prototype,{constructor:{value:t,writable:!0,configurable:!0}}),Object.defineProperty(t,"prototype",{writable:!1}),e&&c(t,e)}(f,t);var e,n,r,a=u(f);function f(){return o(this,f),a.apply(this,arguments)}return e=f,(n=[{key:"connect",value:function(){this.element.addEventListener("chartjs:pre-connect",this._onPreConnect)}},{key:"disconnect",value:function(){this.element.removeEventListener("chartjs:pre-connect",this._onPreConnect)}},{key:"_onPreConnect",value:function(t){t.detail.options.plugins.tooltip.callbacks={label:function(t){return t.label||""}}}}])&&i(e.prototype,n),r&&i(e,r),Object.defineProperty(e,"prototype",{writable:!1}),f}(n(6599).Qr)},2758:(t,e,n)=>{"use strict";n(9554),n(1539),n(4747);var r=n(5088),o=(n(4450),n(3778),n(9145),{name:"titleAttribute",defaultValue:!0,fn:function(){return{onCreate:function(t){if(t.props.titleAttribute){var e=t.reference.getAttribute("title");e&&(t.setContent(e),t.reference.removeAttribute("title"))}},onShow:function(t){if(t.props.titleAttribute){var e=t.reference.getAttribute("title");e&&(t.setContent(e),t.reference.removeAttribute("title"))}}}}});n(2564),n(9826);var i=n(9755);var c=n(9755);(0,n(2192).x)(n(4692)),n(7327);var u=n(9755);var a=n(9755);n.g.$=n.g.jQuery=a,n(6468),n(686),a.fn.select2.amd.define("select2/i18n/ru",[],n(4551));window.addEventListener("load",(function(){var t;document.querySelectorAll("[title]").forEach((function(t){(0,r.ZP)(t,{theme:"material",animation:"scale",allowHTML:!0,arrow:!0,plugins:[o]})})),t=document.querySelectorAll('[type="submit"]'),window.addEventListener("submit",(function(e){var n=e.composedPath()[0];"_blank"!=(null==n?void 0:n.target)&&t.forEach((function(t){t.getAttribute("data-not-disable")||(t.disabled=!0)}))})),c(".suai-copy-to-clipboard").on("click",(function(t){var e=c(t.currentTarget).data("copy-target");navigator.clipboard.writeText(c(e).text())})),u(".suai-dep-select").on("change",(function(){var t=u('.suai-dep-select-child[data-select-parent="#'+u(this).attr("id")+'"]'),e=u(this).val();t.hide(),t.find("select, textarea, input").prop("disabled",!0),(t=t.filter((function(t,n){return String(u(n).data("selectValue"))===String(e)}))).show(),t.find("select, textarea, input").prop("disabled",!1)})),u(".suai-dep-select").change()})),document.addEventListener("DOMContentLoaded",(function(){!function(){var t=i(".nav-tabs.tabs-animate");if(t.length){var e=function(){var e=t.find(".active"),n=e.innerWidth(),r=e.innerHeight(),o=e.position();t.find(".tab").css({left:o.left+"px",width:n+"px",height:r+"px",top:o.top+"px"})};i(window).resize((function(){e()})),i("#menu-burger").click((function(){setTimeout((function(){e()}),400)})),i(".nav-tabs").on("click","a",(function(t){t.preventDefault();var e=i(this).innerWidth(),n=i(this).position();i(".tab").css({left:n.left+"px",top:n.top+"px",width:e+"px"})})),e()}}()}))},5806:(t,e,n)=>{"use strict";n.r(e),n.d(e,{default:()=>p});n(9753),n(8304),n(4812),n(489),n(6992),n(1539),n(3948),n(2419),n(8011),n(9070),n(2526),n(1817),n(2165),n(8783);var r=n(6599),o=n(5538);function i(t){return i="function"==typeof Symbol&&"symbol"==typeof Symbol.iterator?function(t){return typeof t}:function(t){return t&&"function"==typeof Symbol&&t.constructor===Symbol&&t!==Symbol.prototype?"symbol":typeof t},i(t)}function c(t,e){if(!(t instanceof e))throw new TypeError("Cannot call a class as a function")}function u(t,e){for(var n=0;n<e.length;n++){var r=e[n];r.enumerable=r.enumerable||!1,r.configurable=!0,"value"in r&&(r.writable=!0),Object.defineProperty(t,r.key,r)}}function a(t,e){return a=Object.setPrototypeOf?Object.setPrototypeOf.bind():function(t,e){return t.__proto__=e,t},a(t,e)}function f(t){var e=function(){if("undefined"==typeof Reflect||!Reflect.construct)return!1;if(Reflect.construct.sham)return!1;if("function"==typeof Proxy)return!0;try{return Boolean.prototype.valueOf.call(Reflect.construct(Boolean,[],(function(){}))),!0}catch(t){return!1}}();return function(){var n,r=s(t);if(e){var o=s(this).constructor;n=Reflect.construct(r,arguments,o)}else n=r.apply(this,arguments);return l(this,n)}}function l(t,e){if(e&&("object"===i(e)||"function"==typeof e))return e;if(void 0!==e)throw new TypeError("Derived constructors may only return object or undefined");return function(t){if(void 0===t)throw new ReferenceError("this hasn't been initialised - super() hasn't been called");return t}(t)}function s(t){return s=Object.setPrototypeOf?Object.getPrototypeOf.bind():function(t){return t.__proto__||Object.getPrototypeOf(t)},s(t)}var p=function(t){!function(t,e){if("function"!=typeof e&&null!==e)throw new TypeError("Super expression must either be null or a function");t.prototype=Object.create(e&&e.prototype,{constructor:{value:t,writable:!0,configurable:!0}}),Object.defineProperty(t,"prototype",{writable:!1}),e&&a(t,e)}(l,t);var e,n,r,i=f(l);function l(){return c(this,l),i.apply(this,arguments)}return e=l,(n=[{key:"connect",value:function(){if(!(this.element instanceof HTMLCanvasElement))throw new Error("Invalid element");var t=this.viewValue;Array.isArray(t.options)&&0===t.options.length&&(t.options={}),this._dispatchEvent("chartjs:pre-connect",{options:t.options});var e=this.element.getContext("2d");if(!e)throw new Error("Could not getContext() from Element");var n=new o.Z(e,t);this._dispatchEvent("chartjs:connect",{chart:n})}},{key:"_dispatchEvent",value:function(t,e){this.element.dispatchEvent(new CustomEvent(t,{detail:e}))}}])&&u(e.prototype,n),r&&u(e,r),Object.defineProperty(e,"prototype",{writable:!1}),l}(r.Qr);p.values={view:Object}}},t=>{t.O(0,[755,139,257,952,171],(()=>{return e=2758,t(t.s=e);var e}));t.O()}]);