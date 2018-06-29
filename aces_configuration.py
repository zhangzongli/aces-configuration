#!/usr/bin/env python
# _*_ coding:utf-8 _*_

import os
import pymysql
import eum_config
import configparser
import common

# 读取配置文件
config = configparser.ConfigParser()
config.read("db.cfg")
dbinfo = config.sections()[0]
host = config.get(dbinfo, "host")
port = config.getint(dbinfo, "port")
user = config.get(dbinfo, "user")
passwd = config.get(dbinfo, "passwd")
db = config.get(dbinfo, "db")
# charset = config.getint(dbinfo, "charset")

parameter = config.sections()[1]
project_short = config.get(parameter, "project_short")

# 目标数据库链接
db = pymysql.Connect(
    host=host,
    port=port,
    user=user,
    passwd=passwd,
    db=db,
    charset='utf8'
)

# 获取游标
cursor = db.cursor()

# 项目名称
projectName = ""
# 项目主机数
chillerNum = 0
# 冷冻泵数目
chilledPump = 0
# 冷却泵数目
coolingPump = 0
# 冷却塔数目
coolingTower = 0
# 项目标志位
project_flag = ""

# 主机数(英文) + 项目名
# two_bqjwm
base_numAndName = ""

# 获取项目基本信息
def getBasicData():
    # 获取项目名称
    sqlOfProjectName = "select name from building limit 1"
    cursor.execute(sqlOfProjectName)
    resultOfProjectName = cursor.fetchall()
    if not resultOfProjectName:
        print("error: 该项目building表中无数据")
        exit()
    global projectName
    projectName = str(resultOfProjectName[0][0])
    print("info: 项目名为" + projectName)

    # 获取项目主机数
    sqlOfChillerNum = "select count(1) from chiller_config"
    cursor.execute(sqlOfChillerNum)
    resultOfChillerNum = cursor.fetchall()
    if not resultOfChillerNum:
        print("error: 该项目chiller_config表中无数据")
        exit()
    global chillerNum
    chillerNum = resultOfChillerNum[0][0]
    print("info: 主机数为" + str(chillerNum))

    # 获取冷冻泵数目
    sqlOfChilledPumpNum = "select count(1) from water_pump_config where water_pump_type_id = 1"
    cursor.execute(sqlOfChilledPumpNum)
    resultOfChilledPumpNum = cursor.fetchall()
    if not resultOfChilledPumpNum:
        print("error: 该项目water_pump_config表中无冷冻泵数据")
        exit()
    global chilledPump
    chilledPump = resultOfChilledPumpNum[0][0]
    print("info: 冷冻泵数为" + str(chilledPump))

    # 获取冷却泵数目
    sqlOfCoolingPumpNum = "select count(1) from water_pump_config where water_pump_type_id = 2"
    cursor.execute(sqlOfCoolingPumpNum)
    resultOfCoolingPumpNum = cursor.fetchall()
    if not resultOfCoolingPumpNum:
        print("error: 该项目water_pump_config表中无冷却泵数据")
        exit()
    global coolingPump
    coolingPump = resultOfCoolingPumpNum[0][0]
    print("info: 冷却泵数为" + str(coolingPump))

    # 获取冷却塔数目
    sqlOfCoolingTowerNum = "select count(1) from cooling_tower_config"
    cursor.execute(sqlOfCoolingTowerNum)
    resultOfCoolingTowerNum = cursor.fetchall()
    if not resultOfCoolingTowerNum:
        print("error: 该项目water_pump_config表中无冷却泵数据")
        exit()
    global coolingTower
    coolingTower = resultOfCoolingTowerNum[0][0]
    print("info: 冷却塔数为" + str(coolingTower))

    # 拼接主机数+项目名
    global base_numAndName
    base_numAndName = eum_config.getName(str(chillerNum)) + "_" + project_short

    # 获取项目标志位
    sqlOfProjectFlag = "select `value` from sys_param_config where `code` = \"CONFIGURATION_PIC_FLAG\""
    cursor.execute(sqlOfProjectFlag)
    resultOfProjectFlag = cursor.fetchall()
    if not resultOfProjectFlag:
        print("error: 该项目sys_param_config表中无组态图标记")
        exit()
    global project_flag
    project_flag = resultOfProjectFlag[0][0]
    print("info: 组态图标记为" + project_flag)

    cursor.close()
    db.close()

# 代码文件，若存在则删除
def removeExists():
    pathOfJsp = "./code.jsp"
    if (os.path.exists(pathOfJsp)):
        os.remove(pathOfJsp)
    pathOfCss = "./code.css"
    if (os.path.exists(pathOfCss)):
        os.remove(pathOfCss)
    pathOfJs = "./code.js"
    if (os.path.exists(pathOfJs)):
        os.remove(pathOfJs)

# 生成组态图jsp代码
def generateJsp():
    # configuration_XXX.jsp html
    # 头部开始
    codeStr = """<%@ page language="java" import="java.util.*" pageEncoding="UTF-8"%>
<!doctype html>
<html>
<head>
    <style type="text/css">
        <link type="text/css" rel="stylesheet" href="<%=request.getContextPath()%>/zdmonitor/css/configuration.css">
        <script type="text/javascript" src="<%=request.getContextPath()%>/zdmonitor/js/configuration.js"></script>
    </style>
</head>\n"""
    # 头部结束
    # 项目注释添加
    codeStr += """<!--""" + str(chillerNum) + """台主机代码(""" + projectName + """)-->"""
    codeStr += """<li class="configuration_li current">
    <div class="configuration_img">
        <img src="images/configuration/${backgroundImag}" alt="" width="1220" height="732" usemap="#Map6"/>
        <map name="Map6">
            <%--左侧水泵--%>\n"""
    # 拼接图片map的设备触发区域
    # 拼接左侧冷冻水泵
    for num in range(chilledPump):
        codeStr += """            <area class=\""""+ base_numAndName +"""_area"""+ common.intToStr(num+1) +"""\" shape="rect" coords="88,350,180,400" href="#">\n"""
    # 拼接右侧冷却水泵
    codeStr += """            <%--右侧水泵--%>\n"""
    for num in range(chilledPump, chilledPump + coolingPump):
        codeStr += """            <area class=\""""+ base_numAndName +"""_area"""+ common.intToStr(num+1) +"""\" shape="rect" coords="88,350,180,400" href="#">\n"""
    # 拼接中间主机
    codeStr += """            <%--中间机组--%>\n"""
    for num in range(chilledPump + coolingPump, chilledPump + coolingPump + chillerNum):
        codeStr += """            <area class=\""""+ base_numAndName +"""_area"""+ common.intToStr(num+1) +"""\" shape="rect" coords="88,350,180,400" """
        codeStr += """href="<%=request.getContextPath()%>/zdmonitor/EnergyAnalysis.action?tabId=3&objId="""+ str(num + 1 - (chilledPump + coolingPump)) +"""&typeId=1">\n"""
    # 拼接上方冷却塔
    codeStr += """            <%--右上风机--%>\n"""
    for num in range(chilledPump + coolingPump + chillerNum, chilledPump + coolingPump + chillerNum + coolingTower):
        codeStr += """            <area class=\""""+ base_numAndName +"""_area"""+ common.intToStr(num+1) +"""\" shape="rect" coords="88,350,180,400" href="#">\n"""
    codeStr += """        </map>
    </div>\n"""
    # map拼接结束

    # 弹框拼接开始
    codeStr += """    <div class="configuration_alertmsg">\n"""
    # 左侧冷冻泵拼接开始
    codeStr += """        <!--左侧水泵鼠标移上弹出-->\n"""
    for num in range(chilledPump):
        codeStr += """        <div class=\""""+ base_numAndName +"""_left_waterbump"""+ common.intToStr(num+1) +"""\">
            <span class="configuration_alertmsg_top"></span>
            <div class="configuration_alertmsg_center">
                <p>累计运行时间：<span class="total_run_time"></span>h</p>
                <p>频率反馈：<span class="frequency_feedback"></span>Hz</p>
                <p>运行状态：<span class="run_state"></span></p>
                <p>故障报警：<span class="fault_alarm"></span></p>
                <p>自动：<span class="hands_auto"></span></p>
                <p>输入功率：<span class="input_power"></span>kw</p>
            </div>
            <span class="configuration_alertmsg_down"></span>
        </div>\n"""
    # 右侧冷冻泵开始
    codeStr += """        <!--右侧水泵鼠标移上弹出-->\n"""
    for num in range(coolingPump):
        codeStr += """        <div class=\""""+ base_numAndName +"""_right_waterbump"""+ common.intToStr(num+1) +"""\">
            <span class="configuration_alertmsg_top"></span>
            <div class="configuration_alertmsg_center">
                <p>累计运行时间：<span class="total_run_time"></span>h</p>
                <p>频率反馈：<span class="frequency_feedback"></span>Hz</p>
                <p>运行状态：<span class="run_state"></span></p>
                <p>故障报警：<span class="fault_alarm"></span></p>
                <p>自动：<span class="hands_auto"></span></p>
                <p>输入功率：<span class="input_power"></span>kw</p>
            </div>
            <span class="configuration_alertmsg_down"></span>
        </div>\n"""
    # 中间机组开始
    codeStr += """        <!--中间机组鼠标移上弹出-->\n"""
    for num in range(chillerNum):
        codeStr += """        <div class=\""""+ base_numAndName +"""_cooler"""+ common.intToStr(num+1) +"""\">
            <span class="configuration_alertmsg_top"></span>
            <div class="configuration_alertmsg_center">
                <p>累计运行时间：<span class="total_run_time"></span>h</p>
                <p>输入功率：<span class="input_power"></span>Kw</p>
            </div>
            <span class="configuration_alertmsg_down"></span>
        </div>\n"""
    # 上方冷却塔
    codeStr += """        <!--上方风机鼠标移上弹出-->\n"""
    for num in range(coolingTower):
        codeStr += """        <div class=\""""+ base_numAndName +"""_fan"""+ common.intToStr(num+1) +"""\">
            <span class="configuration_alertmsg_top"></span>
            <div class="configuration_alertmsg_center">
                <p>累计运行时间：<span class="total_run_time"></span>h</p>
                <p>集水盘水液位：<span class="drain_pan_water_level"></span></p>
                <p>风机频率反馈：<span class="fans_frequency_feedback"></span></p>
                <p>风机运行状态：<span class="fans_run_state"></span></p>
                <p>输入功率：<span class="input_power"></span>kw</p>
            </div>
            <span class="configuration_alertmsg_down"></span>
        </div>\n"""
    codeStr += """    </div>\n"""
    # 弹框拼接结束

    # 温度、压强、流量等拼接
    codeStr += """    <div class="one_bqjwm_configuration_text">
        <div class="num01"><p class="temperature" id="chilled_water_main_pipe_state__return_water_temperature" title="冷冻总管回水温度" unit="℃"><span></span>℃</p><p class="pressure" id="chilled_water_main_pipe_state__return_water_pressure" title="冷冻总管回水压强" unit="MPa"><span></span>MPa</p></div>
        <div class="num02"><p class="temperature" id="chilled_water_main_pipe_state__supply_water_temperature" title="冷冻总管供水温度" unit="℃"><span></span>℃</p><p class="pressure" id="chilled_water_main_pipe_state__supply_water_pressure" title="冷冻总管供水压强"  unit="MPa"><span></span>MPa</p><p class="flow"  id="chilled_water_main_pipe_state__flow" title="冷冻总管流量" unit="T/h"><span></span>T/h</p></div>
        <div class="num03"><p class="temperature" id="cooling_main_pipe_state__supply_water_temperature" title="冷却总管供水温度" unit="℃"><span></span>℃</p><!-- <p class="flow"  id="cooling_main_pipe_state__flow" title="冷却总管流量" unit="T/h"><span></span>T/h</p> --></div>
        <div class="num04"><p class="temperature" id="cooling_main_pipe_state__return_water_temperature" title="冷却总管回水温度" unit="℃"><span></span>℃</p><%--<p class="pressure" id="cooling_main_pipe_state__return_water_pressure" title="冷却总管回水压强"><span></span>MPa</p>--%></div>
    </div>\n"""

    # 状态图拼接
    codeStr += """    <div class="configuration_states">\n"""
    # 左侧冷冻泵拼接
    codeStr += """        <!--左侧冷冻泵水泵的状态-->\n"""
    for num in range(chilledPump):
        codeStr += """        <span class=\""""+ base_numAndName +"""_left_waterbump"""+ common.intToStr(num+1) +"""_states"></span>\n"""
    # 右侧冷却泵拼接
    codeStr += """        <!--右侧冷冻泵水泵的状态-->\n"""
    for num in range(coolingPump):
        codeStr += """        <span class=\""""+ base_numAndName +"""_right_waterbump"""+ common.intToStr(num+1) +"""_states"></span>\n"""
    # 中间主机拼接
    codeStr += """        <!--主机的状态-->\n"""
    for num in range(chillerNum):
        codeStr += """        <span class=\""""+ base_numAndName +"""_cooler"""+ common.intToStr(num+1) +"""_states"></span>\n"""
    # 上方冷却塔拼接
    codeStr += """        <!--风机的状态-->\n"""
    for num in range(coolingTower):
        codeStr += """       <span class="one_bqjwm_fan01_states"></span>\n"""
    codeStr += """    </div>
</li>\n"""

    # 隐藏区域触发悬浮窗js拼接
    codeStr += """<script type="text/javascript">
    $(function(){\n"""
    # 左侧冷冻泵拼接
    for num in range(chilledPump):
        codeStr += """        $('."""+ base_numAndName +"""_area"""+ common.intToStr(num+1) +"""\').hover(function(e) {
            $('."""+ base_numAndName +"""_left_waterbump"""+ common.intToStr(num+1) +"""\').toggle();
        });\n"""
    # 右侧冷却泵拼接
    for num in range(chilledPump, chilledPump + coolingPump):
        codeStr += """        $('."""+ base_numAndName +"""_area"""+ common.intToStr(num+1) +"""\').hover(function(e) {
            $('."""+ base_numAndName +"""_right_waterbump"""+ common.intToStr(num+1-chilledPump) +"""\').toggle();
        });\n"""
    # 中间主机拼接
    for num in range(chilledPump + coolingPump, chilledPump + coolingPump + chillerNum):
        codeStr += """        $('."""+ base_numAndName +"""_area"""+ common.intToStr(num+1) +"""\').hover(function(e) {
            $('."""+ base_numAndName +"""_cooler"""+ common.intToStr(num+1-chilledPump-coolingPump) +"""\').toggle();
        });\n"""
    # 上方冷却塔拼接
    for num in range(chilledPump + coolingPump + chillerNum, chilledPump + coolingPump + chillerNum + coolingTower):
        codeStr += """        $('."""+ base_numAndName +"""_area"""+ common.intToStr(num+1) +"""\').hover(function(e) {
            $('."""+ base_numAndName +"""_fan"""+ common.intToStr(num+1-chilledPump-coolingPump-chillerNum) +"""\').toggle();
        });\n"""
    codeStr += """    });
</script>"""

    file = open("code.jsp", "x", encoding = 'utf-8')
    file.write(codeStr)
    file.close()

# 生成css代码
def generateCss():

    cssStr = """/*--------""" + str(chillerNum) + """台机组样式(""" + projectName + """)--------*/\n"""

    # 左侧冷冻泵悬浮窗css拼接
    for num in range(chilledPump):
        cssStr += """."""+ base_numAndName +"""_left_waterbump"""+ common.intToStr(num+1) +"""{
	width:225px;
	height:auto;
	overflow:hidden;
	position:absolute;
	top:170px;
	left:20px;
	display:none;
}\n"""
    # 右侧冷却泵悬浮窗css拼接
    for num in range(coolingPump):
        cssStr += """."""+ base_numAndName +"""_right_waterbump"""+ common.intToStr(num+1) +"""{
	width:225px;
	height:auto;
	overflow:hidden;
	position:absolute;
	top:170px;
	right:110px;
	display:none;
}\n"""
    # 中间机组悬浮窗css拼接
    for num in range(chillerNum):
        cssStr += """."""+ base_numAndName +"""_cooler"""+ common.intToStr(num+1) +"""{
	width:225px;
	height:auto;
	overflow:hidden;
	position:absolute;
	top:300px;
	left:530px;
	display:none;
}\n"""
    # 上方冷却塔悬浮窗css拼接
    for num in range(coolingTower):
        cssStr += """."""+ base_numAndName +"""_fan"""+ common.intToStr(num+1) +"""{
	width:225px;
	height:auto;
	overflow:hidden;
	position:absolute;
	top:0px;
	left:750px;
	display:none;
}\n"""
    # 左侧冷冻泵状态图css拼接
    for num in range(chilledPump):
        cssStr += """/*偏移量 -XXpx*/
."""+ base_numAndName +"""_left_waterbump"""+ common.intToStr(num+1) +"""_states{
	width:33px;
	height:14px;
	position:absolute;
	left:103px;
	top:347px;
	background:url(../images/configuration/"""+ project_short +"""/"""+ project_short +"""_left_waterpumb"""+ common.intToStr(num+1) +"""_states.png) no-repeat center 0;
}\n"""
    # 右侧冷却泵状态图css拼接
    for num in range(coolingPump):
        cssStr += """/*偏移量 -XXpx*/
."""+ base_numAndName +"""_right_waterbump"""+ common.intToStr(num+1) +"""_states{
	width:30px;
	height:14px;
	position:absolute;
	right:105px;
	top:350px;
	background:url(../images/configuration/"""+ project_short +"""/"""+ project_short +"""_right_waterpumb"""+ common.intToStr(num+1) +"""_states.png) no-repeat center 0;
}\n"""

    # 中间主机状态图css拼接
    for num in range(chillerNum):
        cssStr += """/*偏移量 -XX*/
."""+ base_numAndName +"""_cooler"""+ common.intToStr(num+1) +"""_states{
	width:39px;
	height:23px;
	background:url(../images/configuration/"""+ project_short +"""/"""+ project_short +"""_cooler"""+ common.intToStr(num+1) +"""_states.png) no-repeat center 0;
	position:absolute;
	left:684px;
	top:440px;
}\n"""
    # 上方冷却塔状态图css拼接
    for num in range(coolingTower):
        cssStr += """/*偏移量 -XXpx*/
."""+ base_numAndName +"""_fan"""+ common.intToStr(num+1) +"""_states{
	width:84px;
	height:43px;
	background:url(../images/configuration/"""+ project_short +"""/"""+ project_short +"""_fan"""+ common.intToStr(num+1) +"""_states.png) no-repeat center 0;
	position:absolute;
	left:952px;
	top:47px;
}\n"""

    # 温度、压强、流量等css拼接
    cssStr += """.one_bqjwm_configuration_text .num01{
	position:absolute;
	left:260px;
	top:200px;
}
.one_bqjwm_configuration_text .num02{
	position:absolute;
	left:450px;
	top:200px;
}
.one_bqjwm_configuration_text .num03{
	position:absolute;
	left:760px;
	top:200px;
}
.one_bqjwm_configuration_text .num04{
	position:absolute;
	right:220px;
	top:200px;
}\n"""
    cssStr += """/*--------""" + str(chillerNum) + """台机组样式(""" + projectName + """)--------*/"""
    file = open("code.css", "x", encoding = 'utf-8')
    file.write(cssStr)
    file.close()

def generateJs():
    # 冷却塔js拼接----------复制至loadcoolingTower(arr,chillerNum)方法
    jsStr = """//冷却塔js拼接----------复制至loadcoolingTower(arr,chillerNum)方法\n"""
    jsStr += """else if (g_configurationPicFlag=="flow-mlmhlgd") { //""" + projectName + """\n"""
    for num in range(coolingTower):
        jsStr += """        $("."""+ base_numAndName +"""_fan"""+ common.intToStr(num+1) +""" .total_run_time").html(toFix(arr["""+ str(num+1) +"""].total_run_time)); //电流
        $("."""+ base_numAndName +"""_fan"""+ common.intToStr(num+1) +""" .drain_pan_water_level").html(toFix(arr["""+ str(num+1) +"""].drain_pan_water_level)); //电压
        $("."""+ base_numAndName +"""_fan"""+ common.intToStr(num+1) +""" .fans_frequency_feedback").html(toFix(arr["""+ str(num+1) +"""].fans_frequency_feedback)); //功率
        $("."""+ base_numAndName +"""_fan"""+ common.intToStr(num+1) +""" .fans_run_state").html(getRunState(arr["""+ str(num+1) +"""].fans_run_state+"",arr["""+ str(num+1) +"""].fans_fault_alarm+"")); //累计能耗
        $("."""+ base_numAndName +"""_fan"""+ common.intToStr(num+1) +"""_states").css("background",getTowerStatePicPosition(arr["""+ str(num+1) +"""].fans_run_state+"",arr["""+ str(num+1) +"""].fans_fault_alarm+"",\""""+ common.intToStr(num+1) +"""\"));//冷却塔颜色\n"""

    jsStr += """}\n"""
    # 冷冻水泵js拼接--------复制至loadChilledPump(arr,chillerNum)方法
    jsStr += """//冷冻水泵js拼接--------复制至loadChilledPump(arr,chillerNum)方法\n"""
    jsStr += """else if (g_configurationPicFlag==\""""+ project_flag +"""\") { //"""+ projectName + """\n"""
    jsStr += """var divArr = ["""
    i = 1
    for num in range(chilledPump):
        if i != chilledPump:
            jsStr += """\"""" + common.intToStr(num + 1) + """\","""
        else:
            jsStr += """\"""" + common.intToStr(num + 1) + """\"];\n"""
        i += 1

    jsStr += """        for(var i = 0; i < arr.length; i++) {\n"""
    jsStr += """            if(i > """+ str(chilledPump-1) +""") {
                continue;
            }
            $("."""+ base_numAndName +"""_left_waterbump"+divArr[i]+" .total_run_time").html(toFix(arr[i].total_run_time||""));
            $("."""+ base_numAndName +"""_left_waterbump"+divArr[i]+" .frequency_feedback").html(toFix(arr[i].frequency_feedback||""));
            $("."""+ base_numAndName +"""_left_waterbump"+divArr[i]+" .run_state").html(getRunState(arr[i].run_state, ""));
            $("."""+ base_numAndName +"""_left_waterbump"+divArr[i]+" .fault_alarm").html(getRunState(arr[i].run_state, arr[i].fault_alarm));
            $("."""+ base_numAndName +"""_left_waterbump"+divArr[i]+" .hands_auto").html(getIsNo(arr[i].hands_auto));
            $("."""+ base_numAndName +"""_left_waterbump"+divArr[i]+" .input_power").html(toFix(arr[i].input_power||""));
            $("."""+ base_numAndName +"""_left_waterbump"+divArr[i]+"_states").css("background",getChilledPumpStatePic(arr[i].run_state,arr[i].fault_alarm,divArr[i]));
        }\n"""
    jsStr += """	}\n"""

    # 冷却泵js拼接-----------复制至loadCoolingPump(arr,chillerNum)方法
    jsStr += """//冷却泵js拼接-----------复制至loadCoolingPump(arr,chillerNum)方法\n"""
    jsStr += """else if (g_configurationPicFlag == \""""+ project_flag +"""\") { //""" + projectName + """\n"""
    jsStr += """var divArr = ["""
    j = 1
    for num in range(coolingPump):
        if j != coolingPump:
            jsStr += """\"""" + common.intToStr(num + 1) + """\","""
        else:
            jsStr += """\"""" + common.intToStr(num + 1) + """\"];\n"""
        j += 1

    jsStr += """for(var i=0; i<arr.length;i++) {\n"""
    jsStr += """            if(i > """+ str(coolingPump - 1) +""") {
                continue;
            }
            $("."""+ base_numAndName +"""_right_waterbump"+divArr[i]+" .total_run_time").html(toFix(arr[i].total_run_time||""));
            $("."""+ base_numAndName +"""_right_waterbump"+divArr[i]+" .frequency_feedback").html(toFix(arr[i].frequency_feedback||""));
            $("."""+ base_numAndName +"""_right_waterbump"+divArr[i]+" .run_state").html(getRunState(arr[i].run_state, ""));
            $("."""+ base_numAndName +"""_right_waterbump"+divArr[i]+" .fault_alarm").html(getRunState(arr[i].run_state, arr[i].fault_alarm));
            $("."""+ base_numAndName +"""_right_waterbump"+divArr[i]+" .hands_auto").html(getIsNo(arr[i].hands_auto));
            $("."""+ base_numAndName +"""_right_waterbump"+divArr[i]+" .input_power").html(toFix(arr[i].input_power||""));
            $("."""+ base_numAndName +"""_right_waterbump"+divArr[i]+"_states").css("background",getCoolingPumpStatePic(arr[i].run_state,arr[i].fault_alarm,divArr[i]));
        }\n"""
    jsStr += """	}\n"""

    # 主机js拼接---------复制至loadChiller(arr, chillerEnableArr,chillerNum)方法
    jsStr += """//主机js拼接---------复制至loadChiller(arr, chillerEnableArr,chillerNum)方法\n"""
    jsStr += """else if (g_configurationPicFlag == \"""" + project_flag + """\") { //""" + projectName + """\n"""
    jsStr += """var divArr = ["""
    n = 1
    for num in range(chillerNum):
        if j != coolingPump:
            jsStr += """\"""" + common.intToStr(num + 1) + """\","""
        else:
            jsStr += """\"""" + common.intToStr(num + 1) + """\"];\n"""
            n += 1
    jsStr += """        for(var i=0; i<arr.length;i++) {\n"""
    jsStr += """            if(i>"""+ str(chillerNum - 1) +""") {
                continue;
            }
            $("."""+ base_numAndName +"""_cooler"+divArr[i]+" .total_run_time").html(toFix(arr[i].total_run_time)); //总累计运行时间	total_run_time
            $("."""+ base_numAndName +"""_cooler"+divArr[i]+" .input_power").html(toFix(arr[i].input_power||"")); //输入功率
            $("."""+ base_numAndName +"""_cooler"+divArr[i]+"_states").css("background",getChillerStatePicPosition(i+1,arr[i].run_state,arr[i].alarm_state, divArr[i]));
        }\n"""
    jsStr += """	}\n"""

    jsStr += """//设置偏移量代码 去各自方法复制粘贴即可"""

    file = open("code.js", "x", encoding = 'utf-8')
    file.write(jsStr)
    file.close()

if __name__ == "__main__" :
    print("info: 组态图代码生成开始")
    removeExists()
    getBasicData()
    generateJsp()
    generateCss()
    generateJs()
    print("info: 组态图代码生成成功")

