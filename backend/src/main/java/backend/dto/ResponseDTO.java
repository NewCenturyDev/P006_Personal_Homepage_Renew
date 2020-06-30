package backend.dto;

public class ResponseDTO {
    protected Boolean success;
    protected String error;

    public Boolean getSuccess() {
        return success;
    }
    public String getError() {
        return error;
    }
    public void setSuccess(Boolean success) {
        this.success = success;
    }
    public void setError(String error) {
        this.error = error;
    }
}
