from __future__ import unicode_literals

from djblets.util.compat import six
from djblets.util.compat.six.moves import http_client
from djblets.util.compat.six.moves.urllib.error import HTTPError, URLError
                                            RepositoryError,
                                            TwoFactorAuthCodeRequiredError)
from reviewboard.scmtools.errors import (FileNotFoundError,
                                         InvalidChangeNumberError,
                                         SCMError)
    supports_two_factor_auth = True
            if six.text_type(e) == 'Not Found':
                  two_factor_auth_code=None, local_site_name=None,
                  *args, **kwargs):
            headers = {}

            if two_factor_auth_code:
                headers['X-GitHub-OTP'] = two_factor_auth_code

                headers=headers,
        except (HTTPError, URLError) as e:
                response_info = e.info()
                x_github_otp = response_info.get('X-GitHub-OTP', '')

                if x_github_otp.startswith('required;'):
                    raise TwoFactorAuthCodeRequiredError(
                        _('Enter your two-factor authentication code '
                          'and re-enter your password to link your account. '
                          'This code will be sent to you by GitHub.'))

                raise AuthorizationError(six.text_type(e))
        except (URLError, HTTPError):
        except (URLError, HTTPError):
            try:
                commit = self._api_get(url)[0]
            except Exception as e:
                raise SCMError(six.text_type(e))
        try:
            comparison = self._api_get(url)
        except Exception as e:
            raise SCMError(six.text_type(e))
            try:
                patch = file['patch']
            except KeyError:
                continue
        elif 'errors' in rsp and status_code == http_client.UNPROCESSABLE_ENTITY:
                                  owner, repo_name)
        except (URLError, HTTPError) as e:
                raise Exception(six.text_type(e))