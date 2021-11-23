// Role | policy attached to the step function
resource "aws_iam_role" "lmu_sfn" {
    name = "sfn_lmu_role"
    assume_role_policy = file("./files/roles/sfn_lmu_role.json")
}

resource "aws_iam_policy" "lmu_sfn_policy" {
    name = "lmu_sfn_policy"
    description = "A policy for the step function"

    policy = file("./files/policies/sfn_lmu.json")
}
    
resource "aws_iam_policy_attachment" "lmu_sfn_policy" {
    name = "lmu_sfn_policy_attachment"
    roles = [aws_iam_role.lmu_sfn.name]
    policy_arn = aws_iam_policy.lmu_sfn_policy.arn
}

// Role | Policy used by the step function to export

resource "aws_iam_role" "sfn_export" {
    name = "sfn_export_role"
    assume_role_policy = file("./files/roles/sfn_export_role.json")
}

resource "aws_iam_policy" "sfn_export_policy" {
    name = "sfn_export_policy"
    description = "Role used in paramater for the S3 export"

    policy = file("./files/policies/sfn_export_policy.json")
}

