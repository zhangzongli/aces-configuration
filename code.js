//冷却塔js拼接----------复制至loadcoolingTower(arr,chillerNum)方法
else if (g_configurationPicFlag=="flow-flow-hxwm") { //惠新物美
        $(".three_hxwm_fan01 .total_run_time").html(toFix(arr[0].total_run_time)); //电流
        $(".three_hxwm_fan00 .drain_pan_water_level").html(toFix(arr[0].drain_pan_water_level)); //电压
        $(".three_hxwm_fan00 .fans_frequency_feedback").html(toFix(arr[0].fans_frequency_feedback)); //功率
        $(".three_hxwm_fan00 .fans_run_state").html(getRunState(arr[0].fans_run_state+"",arr[0].fans_fault_alarm+"")); //累计能耗
        $(".three_hxwm_fan00_states").css("background",getTowerStatePicPosition(arr[0].fans_run_state+"",arr[0].fans_fault_alarm+"","00"));//冷却塔颜色
        $(".three_hxwm_fan02 .total_run_time").html(toFix(arr[1].total_run_time)); //电流
        $(".three_hxwm_fan01 .drain_pan_water_level").html(toFix(arr[1].drain_pan_water_level)); //电压
        $(".three_hxwm_fan01 .fans_frequency_feedback").html(toFix(arr[1].fans_frequency_feedback)); //功率
        $(".three_hxwm_fan01 .fans_run_state").html(getRunState(arr[1].fans_run_state+"",arr[1].fans_fault_alarm+"")); //累计能耗
        $(".three_hxwm_fan01_states").css("background",getTowerStatePicPosition(arr[1].fans_run_state+"",arr[1].fans_fault_alarm+"","01"));//冷却塔颜色
        $(".three_hxwm_fan03 .total_run_time").html(toFix(arr[2].total_run_time)); //电流
        $(".three_hxwm_fan02 .drain_pan_water_level").html(toFix(arr[2].drain_pan_water_level)); //电压
        $(".three_hxwm_fan02 .fans_frequency_feedback").html(toFix(arr[2].fans_frequency_feedback)); //功率
        $(".three_hxwm_fan02 .fans_run_state").html(getRunState(arr[2].fans_run_state+"",arr[2].fans_fault_alarm+"")); //累计能耗
        $(".three_hxwm_fan02_states").css("background",getTowerStatePicPosition(arr[2].fans_run_state+"",arr[2].fans_fault_alarm+"","02"));//冷却塔颜色
}
//冷冻水泵js拼接--------复制至loadChilledPump(arr,chillerNum)方法
else if (g_configurationPicFlag=="flow-hxwm") { //惠新物美
var divArr = ["01","02","03"];
        for(var i = 0; i < arr.length; i++) {
            if(i > 2) {
                continue;
            }
            $(".three_hxwm_left_waterbump"+divArr[i]+" .total_run_time").html(toFix(arr[i].total_run_time||""));
            $(".three_hxwm_left_waterbump"+divArr[i]+" .frequency_feedback").html(toFix(arr[i].frequency_feedback||""));
            $(".three_hxwm_left_waterbump"+divArr[i]+" .run_state").html(getRunState(arr[i].run_state, ""));
            $(".three_hxwm_left_waterbump"+divArr[i]+" .fault_alarm").html(getRunState(arr[i].run_state, arr[i].fault_alarm));
            $(".three_hxwm_left_waterbump"+divArr[i]+" .hands_auto").html(getIsNo(arr[i].hands_auto));
            $(".three_hxwm_left_waterbump"+divArr[i]+" .input_power").html(toFix(arr[i].input_power||""));
            $(".three_hxwm_left_waterbump"+divArr[i]+"_states").css("background",getChilledPumpStatePic(arr[i].run_state,arr[i].fault_alarm,divArr[i]));
        }
	}
//冷却泵js拼接-----------复制至loadCoolingPump(arr,chillerNum)方法
else if (g_configurationPicFlag == "flow-hxwm") { //惠新物美
var divArr = ["01","02","03"];
for(var i=0; i<arr.length;i++) {
            if(i > 2) {
                continue;
            }
            $(".three_hxwm_right_waterbump"+divArr[i]+" .total_run_time").html(toFix(arr[i].total_run_time||""));
            $(".three_hxwm_right_waterbump"+divArr[i]+" .frequency_feedback").html(toFix(arr[i].frequency_feedback||""));
            $(".three_hxwm_right_waterbump"+divArr[i]+" .run_state").html(getRunState(arr[i].run_state, ""));
            $(".three_hxwm_right_waterbump"+divArr[i]+" .fault_alarm").html(getRunState(arr[i].run_state, arr[i].fault_alarm));
            $(".three_hxwm_right_waterbump"+divArr[i]+" .hands_auto").html(getIsNo(arr[i].hands_auto));
            $(".three_hxwm_right_waterbump"+divArr[i]+" .input_power").html(toFix(arr[i].input_power||""));
            $(".three_hxwm_right_waterbump"+divArr[i]+"_states").css("background",getCoolingPumpStatePic(arr[i].run_state,arr[i].fault_alarm,divArr[i]));
        }
	}
//主机js拼接---------复制至loadChiller(arr, chillerEnableArr,chillerNum)方法
else if (g_configurationPicFlag == "flow-hxwm") { //惠新物美
var divArr = ["01","02","03",        for(var i=0; i<arr.length;i++) {
            if(i>2) {
                continue;
            }
            $(".three_hxwm_cooler"+divArr[i]+" .total_run_time").html(toFix(arr[i].total_run_time)); //总累计运行时间	total_run_time
            $(".three_hxwm_cooler"+divArr[i]+" .input_power").html(toFix(arr[i].input_power||"")); //输入功率
            $(".three_hxwm_cooler"+divArr[i]+"_states").css("background",getChillerStatePicPosition(i+1,arr[i].run_state,arr[i].alarm_state, divArr[i]));
        }
	}
//设置偏移量代码 去各自方法复制粘贴即可