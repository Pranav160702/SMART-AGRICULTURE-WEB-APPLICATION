<?php
include ('fsession.php');
ini_set('memory_limit', '-1');

if(!isset($_SESSION['farmer_login_user'])){
    header("location: ../index.php");
}

$query4 = "SELECT * from farmerlogin where email='$user_check'";
$ses_sq4 = mysqli_query($conn, $query4);
$row4 = mysqli_fetch_assoc($ses_sq4);
$para1 = $row4['farmer_id'];
$para2 = $row4['farmer_name'];

?>

<!DOCTYPE html>
<html>
    <?php include ('fheader.php'); ?>

    <body class="bg-white" id="top">

        <?php include ('fnav.php'); ?>

        <section class="section section-shaped section-lg">
            <div class="shape shape-style-1 shape-primary">
                <span></span>
                <span></span>
                <span></span>
                <span></span>
                <span></span>
                <span></span>
                <span></span>
                <span></span>
                <span></span>
                <span></span>
            </div>

            <div class="container ">

                <div class="row">
                    <div class="col-md-8 mx-auto text-center">
                        <span class="badge badge-danger badge-pill mb-3">Prediction</span>
                    </div>
                </div>

                <div class="row row-content">
                    <div class="col-md-12 mb-3">

                        <div class="card text-white bg-gradient-success mb-3">
                            <form role="form" action="#" method="post" enctype="multipart/form-data">
                                <div class="card-header">
                                    <span class=" text-info display-4"> Crop Disease Prediction </span>

                                </div>

                                <div class="card-body text-dark">
                                    <input type="file" name="image" accept="image/*" class="form-control mb-3" required>
                                    <button type="submit" value="Disease_Predict" name="Disease_Predict" class="btn btn-success btn-submit">Predict Disease</button>
                                </div>
                            </form>
                        </div>

                        <div class="card text-white bg-gradient-success mb-3">
                            <div class="card-header">
                                <span class=" text-success display-4"> Result </span>
                            </div>

                            <h4>
                            <?php
                                // Check if the "image" key exists and is not null
                                if(isset($_FILES["image"]) && $_FILES["image"]["tmp_name"] !== null) {
                                    // Command to run the Python script
                                    $command = "python ML/crop_disease_detection/crop_disease_call.py";

                                    // Create pipes for communication
                                    $descriptorspec = array(
                                        0 => array("pipe", "r"), // stdin: pipe that the child will read from
                                        1 => array("pipe", "w"), // stdout: pipe that the child will write to (for Python script output)
                                        2 => array("pipe", "w"), // stderr: pipe that the child will write to (for error messages)
                                    );

                                    // Start the Python process
                                    $process = proc_open($command, $descriptorspec, $pipes);

                                    // Check if process started successfully
                                    if (is_resource($process)) {
                                        // Read image file data
                                        $imageData = file_get_contents($_FILES["image"]["tmp_name"]);

                                        // Write image data to the input pipe
                                        fwrite($pipes[0], $imageData);
                                        fclose($pipes[0]); // Close input pipe to signal end of input

                                        // Read output from the Python script
                                        $output = stream_get_contents($pipes[1]);
                                        fclose($pipes[1]); // Close stdout pipe

                                        // Read error messages, if any
                                        $error_output = stream_get_contents($pipes[2]);
                                        fclose($pipes[2]); // Close stderr pipe

                                        // Close the process and get the exit code
                                        $return_value = proc_close($process);

                                        // Output Python script output and exit code
                                        echo $output;
                                        // Optionally, you can handle error output as well
                                        if(!empty($error_output)) {
                                            echo "Error output: " . $error_output;
                                        }
                                        // echo "Exit code: " . $return_value . "\n";
                                    } else {
                                        // Failed to start the process
                                        echo "Failed to start Python process.";
                                    }
                                } else {
                                    // Handle the case where the "image" key is not set or is null
                                    echo "Error: Image not uploaded yet.";
                                }
                                ?>

                            </h4>
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <?php require("footer.php");?>

    </body>
</html>
