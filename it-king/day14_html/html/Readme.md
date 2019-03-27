### 标签分类
#### 块标签  
+ p(段落之间有间距)
+ h系列(加大加粗)
+ div（白板)
#### 行内标签
+ span(白板)
> 标签之间可以嵌套、标签存在的意义，css操作，js操作
#### input系列 + form标签
+ `input type='text'     - name属性，value="赵凡" `
+ `input type='password' - name属性，value="赵凡" `
+ `input type='submit'   - value='提交' 提交按钮，表单`
+ `input type='button'   - value='登录' 按钮`

+ `input type='radio'    - 单选框 value，checked="checked"，name属性（name相同则互斥）`
+ `input type='checkbox' - 复选框 value, checked="checked"，name属性（批量获取数据）`
+ `input type='file'     - 依赖form表单的一个属性 enctype="multipart/form-data"`
+ `input type='rest'     - 重置`

+ `<textarea >默认值</textarea>  - name属性`
+ `select标签            - name,内部option value, 提交到后台，size，multiple`

## css
### 边框
- 宽度，样式，颜色  (border: 4px dotted red;)
- border-left
### 
+ height，         高度 百分比
+ width，          宽度 像素，百分比
+ text-align:ceter, 水平方向居中
+ line-height，垂直方向根据标签高度
+ color、     字体颜色
+ font-size、 字体大小
+ font-weight 字体加粗
### display
display: none; -- 让标签消失
display: inline;
display: block;
display: inline-block;
         具有inline,默认自己有多少占多少
         具有block，可以设置高度，宽度，padding  margin
******
行内标签：无法设置高度，宽度，padding  margin
块级标签：设置高度，宽度，padding  margin
### Refer
[tornado](http://www.cnblogs.com/wupeiqi/articles/5702910.html)
