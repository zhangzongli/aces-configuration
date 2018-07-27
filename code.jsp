<%@ page language="java" import="java.util.*" pageEncoding="UTF-8"%>
<!doctype html>
<html>
<head>
    <style type="text/css">
        <link type="text/css" rel="stylesheet" href="<%=request.getContextPath()%>/zdmonitor/css/configuration.css">
        <script type="text/javascript" src="<%=request.getContextPath()%>/zdmonitor/js/configuration.js"></script>
    </style>
</head>
<!--3台主机代码(惠新物美)--><li class="configuration_li current">
    <div class="configuration_img">
        <img src="images/configuration/${backgroundImag}" alt="" width="1220" height="732" usemap="#Map6"/>
        <map name="Map6">
            <%--左侧水泵--%>
            <area class="three_hxwm_area01" shape="rect" coords="88,350,180,400" href="#">
            <area class="three_hxwm_area02" shape="rect" coords="88,350,180,400" href="#">
            <area class="three_hxwm_area03" shape="rect" coords="88,350,180,400" href="#">
            <%--右侧水泵--%>
            <area class="three_hxwm_area04" shape="rect" coords="88,350,180,400" href="#">
            <area class="three_hxwm_area05" shape="rect" coords="88,350,180,400" href="#">
            <area class="three_hxwm_area06" shape="rect" coords="88,350,180,400" href="#">
            <%--中间机组--%>
            <area class="three_hxwm_area07" shape="rect" coords="88,350,180,400" href="<%=request.getContextPath()%>/zdmonitor/EnergyAnalysis.action?tabId=3&objId=1&typeId=1">
            <area class="three_hxwm_area08" shape="rect" coords="88,350,180,400" href="<%=request.getContextPath()%>/zdmonitor/EnergyAnalysis.action?tabId=3&objId=2&typeId=1">
            <area class="three_hxwm_area09" shape="rect" coords="88,350,180,400" href="<%=request.getContextPath()%>/zdmonitor/EnergyAnalysis.action?tabId=3&objId=3&typeId=1">
            <%--右上风机--%>
            <area class="three_hxwm_area10" shape="rect" coords="88,350,180,400" href="#">
            <area class="three_hxwm_area11" shape="rect" coords="88,350,180,400" href="#">
            <area class="three_hxwm_area12" shape="rect" coords="88,350,180,400" href="#">
        </map>
    </div>
    <div class="configuration_alertmsg">
        <!--左侧水泵鼠标移上弹出-->
        <div class="three_hxwm_left_waterbump01">
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
        </div>
        <div class="three_hxwm_left_waterbump02">
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
        </div>
        <div class="three_hxwm_left_waterbump03">
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
        </div>
        <!--右侧水泵鼠标移上弹出-->
        <div class="three_hxwm_right_waterbump01">
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
        </div>
        <div class="three_hxwm_right_waterbump02">
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
        </div>
        <div class="three_hxwm_right_waterbump03">
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
        </div>
        <!--中间机组鼠标移上弹出-->
        <div class="three_hxwm_cooler01">
            <span class="configuration_alertmsg_top"></span>
            <div class="configuration_alertmsg_center">
                <p>累计运行时间：<span class="total_run_time"></span>h</p>
                <p>输入功率：<span class="input_power"></span>Kw</p>
            </div>
            <span class="configuration_alertmsg_down"></span>
        </div>
        <div class="three_hxwm_cooler02">
            <span class="configuration_alertmsg_top"></span>
            <div class="configuration_alertmsg_center">
                <p>累计运行时间：<span class="total_run_time"></span>h</p>
                <p>输入功率：<span class="input_power"></span>Kw</p>
            </div>
            <span class="configuration_alertmsg_down"></span>
        </div>
        <div class="three_hxwm_cooler03">
            <span class="configuration_alertmsg_top"></span>
            <div class="configuration_alertmsg_center">
                <p>累计运行时间：<span class="total_run_time"></span>h</p>
                <p>输入功率：<span class="input_power"></span>Kw</p>
            </div>
            <span class="configuration_alertmsg_down"></span>
        </div>
        <!--上方风机鼠标移上弹出-->
        <div class="three_hxwm_fan01">
            <span class="configuration_alertmsg_top"></span>
            <div class="configuration_alertmsg_center">
                <p>累计运行时间：<span class="total_run_time"></span>h</p>
                <p>集水盘水液位：<span class="drain_pan_water_level"></span></p>
                <p>风机频率反馈：<span class="fans_frequency_feedback"></span></p>
                <p>风机运行状态：<span class="fans_run_state"></span></p>
                <p>输入功率：<span class="input_power"></span>kw</p>
            </div>
            <span class="configuration_alertmsg_down"></span>
        </div>
        <div class="three_hxwm_fan02">
            <span class="configuration_alertmsg_top"></span>
            <div class="configuration_alertmsg_center">
                <p>累计运行时间：<span class="total_run_time"></span>h</p>
                <p>集水盘水液位：<span class="drain_pan_water_level"></span></p>
                <p>风机频率反馈：<span class="fans_frequency_feedback"></span></p>
                <p>风机运行状态：<span class="fans_run_state"></span></p>
                <p>输入功率：<span class="input_power"></span>kw</p>
            </div>
            <span class="configuration_alertmsg_down"></span>
        </div>
        <div class="three_hxwm_fan03">
            <span class="configuration_alertmsg_top"></span>
            <div class="configuration_alertmsg_center">
                <p>累计运行时间：<span class="total_run_time"></span>h</p>
                <p>集水盘水液位：<span class="drain_pan_water_level"></span></p>
                <p>风机频率反馈：<span class="fans_frequency_feedback"></span></p>
                <p>风机运行状态：<span class="fans_run_state"></span></p>
                <p>输入功率：<span class="input_power"></span>kw</p>
            </div>
            <span class="configuration_alertmsg_down"></span>
        </div>
    </div>
    <div class="one_bqjwm_configuration_text">
        <div class="num01"><p class="temperature" id="chilled_water_main_pipe_state__return_water_temperature" title="冷冻总管回水温度" unit="℃"><span></span>℃</p><p class="pressure" id="chilled_water_main_pipe_state__return_water_pressure" title="冷冻总管回水压强" unit="MPa"><span></span>MPa</p></div>
        <div class="num02"><p class="temperature" id="chilled_water_main_pipe_state__supply_water_temperature" title="冷冻总管供水温度" unit="℃"><span></span>℃</p><p class="pressure" id="chilled_water_main_pipe_state__supply_water_pressure" title="冷冻总管供水压强"  unit="MPa"><span></span>MPa</p><p class="flow"  id="chilled_water_main_pipe_state__flow" title="冷冻总管流量" unit="T/h"><span></span>T/h</p></div>
        <div class="num03"><p class="temperature" id="cooling_main_pipe_state__supply_water_temperature" title="冷却总管供水温度" unit="℃"><span></span>℃</p><!-- <p class="flow"  id="cooling_main_pipe_state__flow" title="冷却总管流量" unit="T/h"><span></span>T/h</p> --></div>
        <div class="num04"><p class="temperature" id="cooling_main_pipe_state__return_water_temperature" title="冷却总管回水温度" unit="℃"><span></span>℃</p><%--<p class="pressure" id="cooling_main_pipe_state__return_water_pressure" title="冷却总管回水压强"><span></span>MPa</p>--%></div>
    </div>
    <div class="configuration_states">
        <!--左侧冷冻泵水泵的状态-->
        <span class="three_hxwm_left_waterbump01_states"></span>
        <span class="three_hxwm_left_waterbump02_states"></span>
        <span class="three_hxwm_left_waterbump03_states"></span>
        <!--右侧冷冻泵水泵的状态-->
        <span class="three_hxwm_right_waterbump01_states"></span>
        <span class="three_hxwm_right_waterbump02_states"></span>
        <span class="three_hxwm_right_waterbump03_states"></span>
        <!--主机的状态-->
        <span class="three_hxwm_cooler01_states"></span>
        <span class="three_hxwm_cooler02_states"></span>
        <span class="three_hxwm_cooler03_states"></span>
        <!--风机的状态-->
       <span class="three_hxwm_fan01_states"></span>
       <span class="three_hxwm_fan02_states"></span>
       <span class="three_hxwm_fan03_states"></span>
    </div>
</li>
<script type="text/javascript">
    $(function(){
        $('.three_hxwm_area01').hover(function(e) {
            $('.three_hxwm_left_waterbump01').toggle();
        });
        $('.three_hxwm_area02').hover(function(e) {
            $('.three_hxwm_left_waterbump02').toggle();
        });
        $('.three_hxwm_area03').hover(function(e) {
            $('.three_hxwm_left_waterbump03').toggle();
        });
        $('.three_hxwm_area04').hover(function(e) {
            $('.three_hxwm_right_waterbump01').toggle();
        });
        $('.three_hxwm_area05').hover(function(e) {
            $('.three_hxwm_right_waterbump02').toggle();
        });
        $('.three_hxwm_area06').hover(function(e) {
            $('.three_hxwm_right_waterbump03').toggle();
        });
        $('.three_hxwm_area07').hover(function(e) {
            $('.three_hxwm_cooler01').toggle();
        });
        $('.three_hxwm_area08').hover(function(e) {
            $('.three_hxwm_cooler02').toggle();
        });
        $('.three_hxwm_area09').hover(function(e) {
            $('.three_hxwm_cooler03').toggle();
        });
        $('.three_hxwm_area10').hover(function(e) {
            $('.three_hxwm_fan01').toggle();
        });
        $('.three_hxwm_area11').hover(function(e) {
            $('.three_hxwm_fan02').toggle();
        });
        $('.three_hxwm_area12').hover(function(e) {
            $('.three_hxwm_fan03').toggle();
        });
    });
</script>