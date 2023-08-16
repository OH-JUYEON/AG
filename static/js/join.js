/*function nicknameF() {
	$.ajax({
		url: "checkNicknameOk.member",
		type: "post",
		data: { memberNickname: $("input[name=memberNickname]").val() },
		async: false,
		success: function(result) {
			$invalid_feeback = $(".invalid-feedback");
			checkNickname = false;
			result = JSON.parse(result);
			$invalid_feeback.eq(0).css("display", "block");
			if (result.check) {
				if (result.length > 1) {
					$invalid_feeback.eq(0).css("color", "#71cd6a");
					$invalid_feeback.eq(0).text("사용가능한 닉네임 입니다");
					checkNickname = true;
				} else {
					$invalid_feeback.eq(0).css("color", "#fa5963");
					$invalid_feeback.eq(0).text("닉네임은 두글자 이상입니다");
					checkNickname = false;
				}
			} else {
				$invalid_feeback.eq(0).css("color", "#fa5963");
				$invalid_feeback.eq(0).text("이미 사용중인 닉네임입니다");
				checkNickname = false;
			}
		}

	})
}*/



/*function emailF() {
	$.ajax({
		url: "checkEmailOk.member",
		type: "post",
		data: { memberEmail: $("input[name=memberEmail]").val() },
		async: false,
		success: function(result) {
			$invalid_feeback = $(".invalid-feedback");
			checkEmail = false;
			result = JSON.parse(result);
			$invalid_feeback.eq(1).css("display", "block");
			if (result.check) {
				if (!result.length == 0) {
					$invalid_feeback.eq(1).css("color", "#71cd6a");
					$invalid_feeback.eq(1).text("사용가능한 이메일 입니다");
					checkEmail = true;
				} else {
					$invalid_feeback.eq(1).css("color", "#fa5963");
					$invalid_feeback.eq(1).text("이메일을 입력해주세요");
					checkEmail = false;
				}
			} else {
				$invalid_feeback.eq(1).css("color", "#fa5963");
				$invalid_feeback.eq(1).text("이미 사용중인 이메일입니다");
				checkEmail = false;
			}
		}

	})
}*/

let checkNickname = false;
let checkEmail = false;


$("input[name=memberNickname]").on("blur", function() {
	$.ajax({
		url: "checkNicknameOk.member",
		type: "post",
		data: { memberNickname: $("input[name=memberNickname]").val() },
		async: false,
		success: function(result) {
			$invalid_feeback = $(".invalid-feedback");
			checkNickname = false;
			result = JSON.parse(result);
			$invalid_feeback.eq(0).css("display", "block");
			if (result.check) {
				if (result.length > 1) {
					$invalid_feeback.eq(0).css("color", "#71cd6a");
					$invalid_feeback.eq(0).text("사용가능한 닉네임 입니다");
					checkNickname = true;
				} else {
					$invalid_feeback.eq(0).css("color", "#fa5963");
					$invalid_feeback.eq(0).text("닉네임은 두글자 이상입니다");
					checkNickname = false;
				}
			} else {
				$invalid_feeback.eq(0).css("color", "#fa5963");
				$invalid_feeback.eq(0).text("이미 사용중인 닉네임입니다");
				checkNickname = false;
			}
		}

	})
});

$("input[name=memberEmail]").on("blur", function() {
	$.ajax({
		url: "checkEmailOk.member",
		type: "post",
		data: { memberEmail: $("input[name=memberEmail]").val() },
		async: false,
		success: function(result) {
			$invalid_feeback = $(".invalid-feedback");
			checkEmail = false;
			result = JSON.parse(result);
			$invalid_feeback.eq(1).css("display", "block");
			if (result.check) {
				if (!result.length == 0) {
					$invalid_feeback.eq(1).css("color", "#71cd6a");
					$invalid_feeback.eq(1).text("사용가능한 이메일 입니다");
					checkEmail = true;
				} else {
					$invalid_feeback.eq(1).css("color", "#fa5963");
					$invalid_feeback.eq(1).text("이메일을 입력해주세요");
					checkEmail = false;
				}
			} else {
				$invalid_feeback.eq(1).css("color", "#fa5963");
				$invalid_feeback.eq(1).text("이미 사용중인 이메일입니다");
				checkEmail = false;
			}
		}

	})
});


function send() {
	if(!checkNickname) {
		return;
	} else if(!checkEmail){
		return;
	}
	document.join.submit();
}




