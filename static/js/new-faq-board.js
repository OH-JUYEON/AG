const $question = $(".faq-question");
const $answer = $(".faq-answer");

$question.click(function() {
	$(this).addClass("selected");
	$answer.show("slow");
})

$question.off('click');