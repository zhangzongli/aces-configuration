#!/usr/bin/env python
# _*_ coding:utf-8 _*_

import os
import pymysql
import eum_config
import configparser

config = configparser.ConfigParser()
config.read("db.config")
dbinfo = config.sections()[0]
host = config.get(dbinfo, "host")
port = config.get(dbinfo, "port")
user = config.get(dbinfo, "user")
passwd = config.get(dbinfo, "passwd")
db = config.get(dbinfo, "db")
charset = config.get(dbinfo, "charset")

# 目标数据库链接
db = pymysql.Connect(
    host=host,
    port=port,
    user=user,
    passwd=passwd,
    db=db,
    charset=charset
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

    cursor.close()
    db.close()

# 代码文件，若存在则删除
def removeExists():
    path = "./code"
    if (os.path.exists(path)):
        os.remove(path)

# 生成组态图代码
def generateConfiguration():
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
    # codeStr += """<li class="configuration_li current">
    # <div class="configuration_img">
    #     <img src="images/configuration/${backgroundImag}" alt="" width="1220" height="732" usemap="#Map6"/>
    #     <map name="Map6">
    #         <%--左侧水泵--%>"""
    # # 拼接图片map的设备触发区域
    # for num in range(1, chilledPump):
    #     codeStr += """<area class=\""""+ eum_config.getName(chillerNum) +"""_bqjwm_area01" shape="rect" coords="88,350,180,400" href="#">"""



    file = open("code", "x", encoding = 'utf-8')
    file.write(codeStr)
    file.close()



if __name__ == "__main__" :
    print("info: 组态图代码生成开始")
    removeExists()
    getBasicData()
    generateConfiguration()
    print("info: 组态图代码生成成功")

