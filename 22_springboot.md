# 1springboot配置

## 1.1 环境准备

jdk1.8: 推荐使用jbk1.8及以上;

maven3.x：，maven3.3以上版本;

lnteliJIDE2019

springBoot 2.3.0.REKEASE

## 1.2 MAVEN 配置阿里云镜像

[下载地址](https://maven.apache.org/download.cgi)





## 1.3 创建一个mven父工程 tx_sboot(pom)

[springboot官网](https://docs.spring.io/spring-boot/docs/2.4.3/reference/html/getting-started.html#getting-started-introducing-spring-boot)



## 1.4默认扫描器basepackage

```java
@SpringBootApplication  //启动类 
public class FirstSpringApplication {
    public static void main(String[] args) {

        SpringApplication.run(FirstSpringApplication.class, args);
    }
}

```

![2021-03-10 21-44-41 的屏幕截图](/home/yyc/图片/2021-03-10 21-44-41 的屏幕截图.png)

默认的扫描会在main函数所在的，cn.tx.sboot这个包里面扫描.

这个包外面的找不到127.0.0.1:8080/hello   就可以找到

```java
package cn.tx.sboot;


import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class TestController {

    @RequestMapping("hello")
    public String hello(){
        return "hello word!!";
    }
}

```

# 2 springbootp配置

配置文件在resources下

 里面创建一个application.properties

server.port=8088  // 配置项目端口

## 2.1 配置文件位置

springboot 启动会扫描以下位置的application.properties 或者 application.yml文件作为springboot 的默认配置文件

-file:./config/  #  项目当前文件下的config文件夹里面找

-file:./  # 项目当前目录， 如果当前项目有父工程，需要在父工程当前目录下

-classpath:/config/  # 类当前目录下的config文件夹里面

-classpath:/  # 类当前目录

以上为优先级高低。。。

## 2.2 yaml

yml是YAML 语言的文件，一数据为中心，比properties更合适做配置文件。

```yml
environments:
	dev:
		url: https://dev.example.com
		name: Developer Setup
	prod: 
		url: https://another.example.com
		name: My Cool App
	
```

## 2.3yml语法

```yam
yaml:
	str: 字符串不需要加双引号
	num: 666
	Dnum: 666.88
	birth: 2000/12/12 12:23:34
```

```yaml
yaml:
	level:
        str: 字符串不需要加双引号
        specialStr: "特殊字符\n要加双引号，这样就能换行"
        num: 666
        Dnum: 666.88
        birth: 2000/12/12 12:23:34
    list:
    	- one
    	- two # 这个会变成一个列表["one", "two"]
    list: [one, two]  # 一样的效果
    set: [1, 2 ,3 ]
    
    map: [key1: valuel, key2: valuel2]
    users:  # 对象
    	- name: zhamgshang
    	  salary: 123.8
    	- mane: lisi
    	  salary: 888.00
```



想要取上面的值需要在类上面给一个注解@

@ConfigurationProperties(prefix = "yaml")

注意 prefix 的值需要想取的数据的上一个层级就是yaml

如果还有上级需要指出prefix = "yaml.level"。才可以找到

* 字面值: 



# 3 构造器绑定

@Comcnent 是让这个作为一个组件加入到spring ...容器中，现在不需要了

需要加注解@ConstructorBinding

把配置文件中属性绑定

要提供构造器

构造器的 类需要配置这个注解@EnableConfigurationProperties(FirstSpringApplication.class)

哪个地方需要用就要用这个注解，参数是要开启的属性类是什么



