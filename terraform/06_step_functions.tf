resource "aws_sfn_state_machine" "sfn_state_machine" {
    name = "lmu_datalake"
    role_arn = aws_iam_role.lmu_sfn.arn

    type = "STANDARD"

    definition = file("./files/step_functions/sfn_lmu_export.json")
}