$(document).ready(function() {
    $('#analyzeButton').click(function() {
        let review = $('#reviewInput').val();
        if (review.trim() === '') {
            alert('Please enter a review!');
            return;
        }

        $.ajax({
            url: '/analyze',
            type: 'POST',
            contentType: 'application/json',
            data: JSON.stringify({ review: review }),
            success: function(response) {
                $('#result').html(`
                    <p><strong>Sentiment:</strong> ${response.sentiment}</p>
                    <p><strong>Polarity:</strong> ${response.polarity.toFixed(2)}</p>
                    <p><strong>Subjectivity:</strong> ${response.subjectivity.toFixed(2)}</p>
                `);
            },
            error: function(error) {
                $('#result').html('<p class="text-danger">Error analyzing sentiment</p>');
            }
        });
    });
});
