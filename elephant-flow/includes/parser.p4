parser start {
	return parser_eth;
}
parser parser_eth {
	extract(eth);
	return select(latest.ethtype) {
		ETH_ETHTYPES_IPV4 : parser_ipv4;
		ADD_ETHTYPES_VALUE : parser_add_header;
		default : ingress;
	}
}
parser parser_add_header {
	extract(ad);
	return select(latest.ethtype) {
		ETH_ETHTYPES_IPV4 : parser_ipv4;
		default : ingress;
	}
}

parser parser_ipv4 {
	extract(ipv4);
	set_metadata(md_hash_1.srcAddr, latest.srcAddr);
	set_metadata(md_hash_2.dstAddr, latest.dstAddr);
	return ingress;
}