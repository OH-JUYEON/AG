let checkEmail = false;
let checkPassword = false;

$("input[name=memberEmail]").on("blur", function() {
	$invalid_feeback = $(".invalid-feedback");
	checkEmail = false;
	if (!$(this).val().length == 0) {
		$invalid_feeback.eq(0).css("display", "none");
		checkEmail = true;
	} else {
		$invalid_feeback.eq(0).css("display", "block");
		checkEmail = false;
	}
});

$("input[name=memberPassword]").on("blur", function() {
	$invalid_feeback = $(".text-invalid");
	checkPassword = false;
	if (!$(this).val().length == 0) {
		$invalid_feeback.eq(0).css("display", "none");
		checkPassword = true;
	} else {
		$invalid_feeback.eq(0).css("display", "block");
		checkPassword = false;
	}
});

function send() {
	if(!checkEmail) {
		return;
	} else if(!checkPassword){
		return;
	}
	document.login.submit();
}