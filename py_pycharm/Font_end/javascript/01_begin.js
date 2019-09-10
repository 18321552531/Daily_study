/*在html中用<script>...</script>之间包含的代码就是javascript代码*/

// alert('Hello word!')

// var x = 1;
// var y = 2;
// if (x>y){
//     alert(x)
//     }



/*javascript中的数据类型：
 *1.number 不区分整数和浮点数，统一用number表示
 */
// a = 12; //整数
// a = 0.12; //浮点数
// a = 1.3e3; //相当于1.3*1000
// a = -99; //负数
// a = NaN; //表示Not a number,当无法计算时用NaN表示
// a = Infinty; //表示无限大

// 四则运算（+，-，*，/)
// 字符串 单或者双引号括起来的任意字符，

var b = 'asd';


// 布尔运算 其值之后true 和 false两种
// && 与运算，所有为true，结果为true
// || 或运算，其中有一个为true，结果为true
// ! 非运算，把true变为false，把false变为true

// 比较运算符 （>,<,=)
// javascript 可以做任意数据类型的比较
// alert(false == 0);
// alert(false === 0);



// 数组
var arr = [1,2,3,'aa',null,true]


// 对象
var person = {
    name:'sam',
    age:19,
    score:88,
    tags:['student','web','art'],
    city:'zhejiang'
};

alert(person.tags[2]);

