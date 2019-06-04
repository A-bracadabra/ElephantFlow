
register bf2_reg_1 {
	width: 1;
	instance_count: REG_MAX_LEN;
}
register bf2_reg_2 {
	width: 1;
	instance_count: REG_MAX_LEN;
}
register bf2_reg_3 {
	width: 1;
	instance_count: REG_MAX_LEN;
}
register bf2_reg_4 {
	width: 1;
	instance_count: REG_MAX_LEN;
}
blackbox stateful_alu stateful_bf2_reg_1 {
	reg: bf2_reg_1;
	update_lo_1_value: set_bit;
	output_value: alu_lo;
	output_dst: md.bf2_1;
}
blackbox stateful_alu stateful_bf2_reg_2 {
	reg: bf2_reg_2;
	update_lo_1_value: set_bit;
	output_value: alu_lo;
	output_dst: md.bf2_2;
}
blackbox stateful_alu stateful_bf2_reg_3 {
	reg: bf2_reg_3;
	update_lo_1_value: set_bit;
	output_value: alu_lo;
	output_dst: md.bf2_3;
}
blackbox stateful_alu stateful_bf2_reg_4 {
	reg: bf2_reg_4;
	update_lo_1_value: set_bit;
	output_value: alu_lo;
	output_dst: md.bf2_4;
}
table bf2_table_1 {
	actions {
		bf2_act_1;
	}
}
table bf2_table_2 {
	actions {
		bf2_act_2;
	}
}
table bf2_table_3 {
	actions {
		bf2_act_3;
	}
}
table bf2_table_4 {
	actions {
		bf2_act_4;
	}
}
action bf2_act_1 (){
	stateful_bf2_reg_1.execute_stateful_alu(md.index21);
}
action bf2_act_2 (){
	stateful_bf2_reg_2.execute_stateful_alu(md.index22);
}
action bf2_act_3 (){
	stateful_bf2_reg_3.execute_stateful_alu(md.index23);
}
action bf2_act_4 (){
	stateful_bf2_reg_4.execute_stateful_alu(md.index24);
}
table set_bf2_nop_table {
	actions {
		set_bf2_nop_act;
	}
}
table set_bf2_update_table {
	actions {
		set_bf2_update_act;
	}
}
action set_bf2_nop_act (){
	modify_field(md.bf2, 1);
}
action set_bf2_update_act (){
	modify_field(md.bf2, 0);
}
control bf2 {
    apply(bf2_table_1);
    apply(bf2_table_2);
    apply(bf2_table_3);
    apply(bf2_table_4);
    if (md.bf2_1 == 1 and md.bf2_2 == 1 and md.bf2_3 == 1 and md.bf2_4 == 1) {
    	apply(set_bf2_nop_table);
    }
    else apply(set_bf2_update_table);
}
