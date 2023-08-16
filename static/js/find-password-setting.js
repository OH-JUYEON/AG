function send() {
	if ($("input[name=memberPassword]").val() == $("input[name=memberPasswordCheck]").val()) {
		
		$(".hide-text").eq(0).css("display", "none");
		document.setting.submit();
		return;
	} else {
		$(".hide-text").eq(0).css("display", "block");
		return;
	}
}