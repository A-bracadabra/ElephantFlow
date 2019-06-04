
register bf1_reg_1 {
	width: 1;
	instance_count: REG_MAX_LEN;
}
register bf1_reg_2 {
	width: 1;
	instance_count: REG_MAX_LEN;
}
register bf1_reg_3 {
	width: 1;
	instance_count: REG_MAX_LEN;
}
register bf1_reg_4 {
	width: 1;
	instance_count: REG_MAX_LEN;
}
blackbox stateful_alu stateful_bf1_reg_1 {
	reg: bf1_reg_1;
	update_lo_1_value: set_bit;
	output_value: alu_lo;
	output_dst: md.bf1_1;
}
blackbox stateful_alu stateful_bf1_reg_2 {
	reg: bf1_reg_2;
	update_lo_1_value: set_bit;
	output_value: alu_lo;
	output_dst: md.bf1_2;
}
blackbox stateful_alu stateful_bf1_reg_3 {
	reg: bf1_reg_3;
	update_lo_1_value: set_bit;
	output_value: alu_lo;
	output_dst: md.bf1_3;
}
blackbox stateful_alu stateful_bf1_reg_4 {
	reg: bf1_reg_4;
	update_lo_1_value: set_bit;
	output_value: alu_lo;
	output_dst: md.bf1_4;
}
table bf1_table_1 {
	actions {
		bf1_act_1;
	}
}
table bf1_table_2 {
	actions {
		bf1_act_2;
	}
}
table bf1_table_3 {
	actions {
		bf1_act_3;
	}
}
table bf1_table_4 {
	actions {
		bf1_act_4;
	}
}
action bf1_act_1 (){
	stateful_bf1_reg_1.execute_stateful_alu(md.index11);
}
action bf1_act_2 (){
	stateful_bf1_reg_2.execute_stateful_alu(md.index12);
}
action bf1_act_3 (){
	stateful_bf1_reg_3.execute_stateful_alu(md.index13);
}
action bf1_act_4 (){
	stateful_bf1_reg_4.execute_stateful_alu(md.index14);
}
table set_bf1_nop_table {
	actions {
		set_bf1_nop_act;
	}
}
table set_bf1_update_table {
	actions {
		set_bf1_update_act;
	}
}
action set_bf1_nop_act (){
	modify_field(md.bf1, 1);
}
action set_bf1_update_act (){
	modify_field(md.bf1, 0);
}
control bf1 {
    apply(bf1_table_1);
    apply(bf1_table_2);
    apply(bf1_table_3);
    apply(bf1_table_4);
    if (md.bf1_1 == 1 and md.bf1_2 == 1 and md.bf1_3 == 1 and md.bf1_4 == 1) {
    	apply(set_bf1_nop_table);
    }
    else apply(set_bf1_update_table);
}
