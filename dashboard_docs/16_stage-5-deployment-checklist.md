# Stage 5 Deployment and Hardening Checklist

## Completed

- [x] Added deployment readiness contract module
- [x] Added deployment readiness API route
- [x] Added API and kiosk systemd unit files
- [x] Added startup scripts for API and kiosk processes
- [x] Added deployment smoke-check script
- [x] Added environment template for Pi runtime
- [x] Added Stage 5 unit and integration tests

## Validation

- [x] Scripts are executable in repository checkout
- [x] Full tests pass with Stage 5 additions (`22 passed`)

## Remaining for Stage 5 Exit

- [ ] Validate systemd install/enable workflow on Raspberry Pi target
- [ ] Validate smoke checks after cold boot and service restart
- [ ] Document rollback and recovery steps for failed startup
