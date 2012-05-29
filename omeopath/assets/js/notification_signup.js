var nsjs = new function() {
    var that = this;
    
    var alert_error_sel = $("#notification_signup div.alert-error");
    var alert_success_sel = $("#notification_signup div.alert-success");
    var email_input_sel = $("#notification_signup input[name=email]");
    this.submit_button_sel = $("#notification_signup button[type=submit]");
    
    this.get_email_input = function() {
        return email_input_sel.val();
    };
    
    this.validate = function() {
        /* client-side validation of user input email address, return error message */
        if (vljs.email(that.get_email_input())) {
            return '<ul class="errorlist"><li>email<ul class="errorlist"><li>Please enter a valid email address.</li></ul></li></ul>';
        } else {
            return '';
        }
    };
    
    this.show_error = function(msg_html) {
        /* display the error message on UI */
        if(typeof(msg_html)==='undefined') {
            msg_html='<ul class="errorlist"><li>An unknown error has occurred. Please try again later or feedback to us.</li></ul>';
        }
        
        alert_error_sel.find("ul.errorlist").remove();  //delete previous error message
        alert_error_sel.append(msg_html).removeClass("hide");
        alert_success_sel.addClass("hide");
    };
    
    this.disable_input = function() {
        that.submit_button_sel.attr('disabled', 'disabled');
        email_input_sel.attr('disabled', 'disabled');
    };
    
    this.enable_input = function() {
        that.submit_button_sel.removeAttr("disabled");
        email_input_sel.removeAttr("disabled");
    };
    
    this.show_success = function() {
        /* display the success message on UI */
        alert_error_sel.addClass("hide");
        alert_success_sel.removeClass("hide");
    };
    
    this.ajax_success = function(data) {
        /* for when ajax call returns success, data returned is an error message */
        if (data) {
            that.show_error(data);
            that.enable_input();
        } else {
            that.show_success();
        }
    };
    
    this.ajax_error = function() {
        /* for when ajax call returns error */
        that.show_error();
        that.enable_input();
    };
    
}();

