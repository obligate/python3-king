/**
 * 解决变量作用域的问题，避免变量冲突
 * 因为js的变量作用域以函数为快.
 */
(function (arg) {

    var status = 1;

    arg.extend({
       'wangsen': function () {
           return 'sb';
       }
    });

})(jQu$ery);
