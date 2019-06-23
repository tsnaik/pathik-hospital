$findId = $('#find-id');
$idError = $('#id-error');
$findPatient = $('#find-patient');
$regPatient = $('#reg-patient');

$('#reg-button').click(function () {
    $findPatient.hide();
    $regPatient.show();
});

$('#find-button').click(function () {
    $regPatient.hide();
    $findPatient.show();
});

$findId.click(function () {
    findById($('#pid').val().trim())
});
$('#pid').keypress(function (event) {
    if (event.keyCode === 13 && !$('#find-id').is(":disabled")) {
        findById($('#pid').val().trim())
    }
});


function findById(pid) {
    console.log("searched: " + pid);

    // validation
    if (isNaN(pid)) {
        $idError.html(`Invalid patient number.`);
        $idError.show();
        return;
    }

    $idError.hide();
    $findId.prop("disabled", true);
    $findId.html(
        `<span class="spinner-grow spinner-grow-sm" role="status" aria-hidden="true"></span> Finding..`
    );
    $.ajax({
        url: window.findPatientByIdURL,
        data: {pid},
        success: [function () {
            window.location.href = window.viewPatientURL.replace(999, pid);

        }],
        error: [function () {
            $idError.html(`Entry does not exist. Please check Patient number.`);
            $idError.show();

            $findId.prop("disabled", false);
            $findId.html(`Find`);
        }]
    })
}